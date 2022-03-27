from google.cloud.bigquery_reservation_v1.services import reservation_service
from google.cloud.bigquery_reservation_v1.types import reservation as reservation_types
from google.protobuf import field_mask_pb2

class BigQueryReservation():
    def __init__(self, admin_project, assignee_project, location, reservation, commitment_slot_count, reservation_slot_count):
        self._admin_project = admin_project
        self._assignee_project = assignee_project
        self._location = location
        self._reservation = reservation
        self._commitment_slot_count = commitment_slot_count
        self._reservation_slot_count = reservation_slot_count
        self._parent = f'projects/{self._admin_project}/locations/{self._location}'
        self._reservation_client = reservation_service.ReservationServiceClient()

    def upgrade_bigquery_slot_capacity(self):
        self._create_capacity_commitment(plan='FLEX', slot_count=self._commitment_slot_count)
        state = self._fetch_commitment_state(plan='FLEX', slot_count=self._commitment_slot_count)
        if state == reservation_types.CapacityCommitment.State.ACTIVE:
            self._update_reservation(slot_capacity=self._reservation_slot_count)
        elif state == reservation_types.CapacityCommitment.State.PENDING:
            # use ondemand paln could be took several hours until flex slots buying
            # https://techblog.zozo.com/entry/bigquery-flex-slots
            assignment_id = self._fetch_assignment_id()
            self._delete_assignment(assignment_id)
            commitment_id = self._fetch_commitment_id(plan='FLEX', slot_count=self._commitment_slot_count)
            self._delete_capacity_commitment(commitment_id)
            # set ondemand_plan for digdag slack notice. cloud be delay batch
        else:
            commitment_id = self._fetch_commitment_id(plan='FLEX', slot_count=self._commitment_slot_count)
            if len(commitment_id) != 0:
                # not to delete before create capacity commitment. other team could be buy and use same amount of flex slots
                self._delete_capacity_commitment(commitment_id)
            raise Exception(f'failed to buy commitment')

    def downgrade_bigquery_slot_capacity(self):
        assignment_id = self._fetch_assignment_id()
        if len(assignment_id) == 0:
            # revert ondemand to  reservation
            self._create_assignment()
        self._update_reservation(slot_capacity=self._reservation_slot_count)
        commitment_id = self._fetch_commitment_id(plan='FLEX', slot_count=self._commitment_slot_count)
        if len(commitment_id) != 0:
            self._delete_capacity_commitment(commitment_id)

    def _create_capacity_commitment(self, plan, slot_count):
        commit_config = reservation_types.CapacityCommitment(plan=plan, slot_count=slot_count)
        self._reservation_client.create_capacity_commitment(parent=self._parent,capacity_commitment=commit_config)

    def _create_assignment(self):
        assign_config = reservation_types.Assignment(job_type='QUERY',assignee=f'projects/{self._assignee_project}')
        assign = self._reservation_client.create_assignment(parent=f'{self._parent }/reservations/{self._reservation}', assignment=assign_config)

    def _update_reservation(self, slot_capacity):
        reservation_name = self._reservation_client.reservation_path(project=self._admin_project, location=self._location, reservation=self._reservation)
        reservation = reservation_types.Reservation(name=reservation_name, slot_capacity=slot_capacity)
        field_mask = field_mask_pb2.FieldMask(paths=["slot_capacity"])
        self._reservation_client.update_reservation(reservation=reservation, update_mask=field_mask)

    def _to_commitment_plan(self, plan):
        if plan == 'FLEX':
            return reservation_types.CapacityCommitment.CommitmentPlan.FLEX
        elif plan == 'MONTHLY':
            return reservation_types.CapacityCommitment.CommitmentPlan.MONTHLY
        elif plan == 'ANNUAL':
            return reservation_types.CapacityCommitment.CommitmentPlan.ANNUAL
        else:
            raise Exception(f'plan is not match {plan}')

    def _fetch_commitment_id(self, plan, slot_count):
        commitments = self._reservation_client.list_capacity_commitments(parent=self._parent)
        commitment_id = [ commitment.name for commitment in commitments if commitment.plan == self._to_commitment_plan(plan) and commitment.slot_count == slot_count ]
        if len(commitment_id) != 0:
            commitment_id = commitment_id[0]
        return commitment_id

    def _fetch_commitment_state(self, plan, slot_count):
        commitments = self._reservation_client.list_capacity_commitments(parent=self._parent)
        commitment_state = [ commitment.state for commitment in commitments if commitment.plan == self._to_commitment_plan(plan) and commitment.slot_count == slot_count ]
        if len(commitment_state) != 0:
            commitment_state = commitment_state[0]
        return commitment_state

    def _fetch_assignment_id(self):
        assignments = self._reservation_client.list_assignments(parent=f'{self._parent }/reservations/{self._reservation}')
        assignment_id = [ assignment.name for assignment in assignments if assignment.assignee == f'projects/{self._assignee_project}']
        if len(assignment_id) != 0:
            assignment_id = assignment_id[0]
        return assignment_id

    def _delete_assignment(self, assignment):
        self._reservation_client.delete_assignment(name=assignment)

    def _delete_capacity_commitment(self, commitment_id):
        self._reservation_client.delete_capacity_commitment(name=commitment_id)

def main():
    bigquery_reservation_config = 'bigquery_reservation'
    admin_project = 'admin_project'
    assignee_project = 'assignee_project'
    location = 'location'
    reservation = 'reservation'
    commitment_slot_count = 100
    reservation_slot_count = 100
    bigquery_reservation = BigQueryReservation(
        admin_project=admin_project,
        assignee_project=assignee_project,
        location=location,
        reservation=reservation,
        commitment_slot_count=commitment_slot_count,
        reservation_slot_count=reservation_slot_count
    )
    bigquery_reservation.upgrade_bigquery_slot_capacity()
    bigquery_reservation.downgrade_bigquery_slot_capacity()

if __name__ == "__main__":
        main()
