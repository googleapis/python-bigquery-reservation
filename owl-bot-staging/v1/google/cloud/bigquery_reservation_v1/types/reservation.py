# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from typing import MutableMapping, MutableSequence

import proto  # type: ignore

from google.protobuf import field_mask_pb2  # type: ignore
from google.protobuf import timestamp_pb2  # type: ignore
from google.rpc import status_pb2  # type: ignore


__protobuf__ = proto.module(
    package='google.cloud.bigquery.reservation.v1',
    manifest={
        'Reservation',
        'CapacityCommitment',
        'CreateReservationRequest',
        'ListReservationsRequest',
        'ListReservationsResponse',
        'GetReservationRequest',
        'DeleteReservationRequest',
        'UpdateReservationRequest',
        'CreateCapacityCommitmentRequest',
        'ListCapacityCommitmentsRequest',
        'ListCapacityCommitmentsResponse',
        'GetCapacityCommitmentRequest',
        'DeleteCapacityCommitmentRequest',
        'UpdateCapacityCommitmentRequest',
        'SplitCapacityCommitmentRequest',
        'SplitCapacityCommitmentResponse',
        'MergeCapacityCommitmentsRequest',
        'Assignment',
        'CreateAssignmentRequest',
        'ListAssignmentsRequest',
        'ListAssignmentsResponse',
        'DeleteAssignmentRequest',
        'SearchAssignmentsRequest',
        'SearchAllAssignmentsRequest',
        'SearchAssignmentsResponse',
        'SearchAllAssignmentsResponse',
        'MoveAssignmentRequest',
        'UpdateAssignmentRequest',
        'TableReference',
        'BiReservation',
        'GetBiReservationRequest',
        'UpdateBiReservationRequest',
    },
)


class Reservation(proto.Message):
    r"""A reservation is a mechanism used to guarantee slots to
    users.

    Attributes:
        name (str):
            The resource name of the reservation, e.g.,
            ``projects/*/locations/*/reservations/team1-prod``. The
            reservation_id must only contain lower case alphanumeric
            characters or dashes. It must start with a letter and must
            not end with a dash. Its maximum length is 64 characters.
        slot_capacity (int):
            Minimum slots available to this reservation. A slot is a
            unit of computational power in BigQuery, and serves as the
            unit of parallelism.

            Queries using this reservation might use more slots during
            runtime if ignore_idle_slots is set to false.

            If the new reservation's slot capacity exceeds the project's
            slot capacity or if total slot capacity of the new
            reservation and its siblings exceeds the project's slot
            capacity, the request will fail with
            ``google.rpc.Code.RESOURCE_EXHAUSTED``.

            NOTE: for reservations in US or EU multi-regions, slot
            capacity constraints are checked separately for default and
            auxiliary regions. See multi_region_auxiliary flag for more
            details.
        ignore_idle_slots (bool):
            If false, any query or pipeline job using this reservation
            will use idle slots from other reservations within the same
            admin project. If true, a query or pipeline job using this
            reservation will execute with the slot capacity specified in
            the slot_capacity field at most.
        concurrency (int):
            Maximum number of queries that are allowed to
            run concurrently in this reservation. This is a
            soft limit due to asynchronous nature of the
            system and various optimizations for small
            queries.
            Default value is 0 which means that concurrency
            will be automatically set based on the
            reservation size.
        creation_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Creation time of the
            reservation.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Last update time of the
            reservation.
        multi_region_auxiliary (bool):
            Applicable only for reservations located
            within one of the BigQuery multi-regions (US or
            EU).
            If set to true, this reservation is placed in
            the organization's secondary region which is
            designated for disaster recovery purposes. If
            false, this reservation is placed in the
            organization's default region.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    slot_capacity: int = proto.Field(
        proto.INT64,
        number=2,
    )
    ignore_idle_slots: bool = proto.Field(
        proto.BOOL,
        number=4,
    )
    concurrency: int = proto.Field(
        proto.INT64,
        number=16,
    )
    creation_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=8,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=9,
        message=timestamp_pb2.Timestamp,
    )
    multi_region_auxiliary: bool = proto.Field(
        proto.BOOL,
        number=14,
    )


class CapacityCommitment(proto.Message):
    r"""Capacity commitment is a way to purchase compute capacity for
    BigQuery jobs (in the form of slots) with some committed period
    of usage. Annual commitments renew by default. Commitments can
    be removed after their commitment end time passes.

    In order to remove annual commitment, its plan needs to be
    changed to monthly or flex first.

    A capacity commitment resource exists as a child resource of the
    admin project.

    Attributes:
        name (str):
            Output only. The resource name of the capacity commitment,
            e.g.,
            ``projects/myproject/locations/US/capacityCommitments/123``
            The commitment_id must only contain lower case alphanumeric
            characters or dashes. It must start with a letter and must
            not end with a dash. Its maximum length is 64 characters.
        slot_count (int):
            Number of slots in this commitment.
        plan (google.cloud.bigquery_reservation_v1.types.CapacityCommitment.CommitmentPlan):
            Capacity commitment commitment plan.
        state (google.cloud.bigquery_reservation_v1.types.CapacityCommitment.State):
            Output only. State of the commitment.
        commitment_start_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The start of the current
            commitment period. It is applicable only for
            ACTIVE capacity commitments.
        commitment_end_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The end of the current
            commitment period. It is applicable only for
            ACTIVE capacity commitments.
        failure_status (google.rpc.status_pb2.Status):
            Output only. For FAILED commitment plan,
            provides the reason of failure.
        renewal_plan (google.cloud.bigquery_reservation_v1.types.CapacityCommitment.CommitmentPlan):
            The plan this capacity commitment is converted to after
            commitment_end_time passes. Once the plan is changed,
            committed period is extended according to commitment plan.
            Only applicable for ANNUAL and TRIAL commitments.
        multi_region_auxiliary (bool):
            Applicable only for commitments located
            within one of the BigQuery multi-regions (US or
            EU).
            If set to true, this commitment is placed in the
            organization's secondary region which is
            designated for disaster recovery purposes. If
            false, this commitment is placed in the
            organization's default region.
    """
    class CommitmentPlan(proto.Enum):
        r"""Commitment plan defines the current committed period.
        Capacity commitment cannot be deleted during it's committed
        period.
        """
        COMMITMENT_PLAN_UNSPECIFIED = 0
        FLEX = 3
        TRIAL = 5
        MONTHLY = 2
        ANNUAL = 4

    class State(proto.Enum):
        r"""Capacity commitment can either become ACTIVE right away or
        transition from PENDING to ACTIVE or FAILED.
        """
        STATE_UNSPECIFIED = 0
        PENDING = 1
        ACTIVE = 2
        FAILED = 3

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    slot_count: int = proto.Field(
        proto.INT64,
        number=2,
    )
    plan: CommitmentPlan = proto.Field(
        proto.ENUM,
        number=3,
        enum=CommitmentPlan,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=4,
        enum=State,
    )
    commitment_start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=9,
        message=timestamp_pb2.Timestamp,
    )
    commitment_end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    failure_status: status_pb2.Status = proto.Field(
        proto.MESSAGE,
        number=7,
        message=status_pb2.Status,
    )
    renewal_plan: CommitmentPlan = proto.Field(
        proto.ENUM,
        number=8,
        enum=CommitmentPlan,
    )
    multi_region_auxiliary: bool = proto.Field(
        proto.BOOL,
        number=10,
    )


class CreateReservationRequest(proto.Message):
    r"""The request for
    [ReservationService.CreateReservation][google.cloud.bigquery.reservation.v1.ReservationService.CreateReservation].

    Attributes:
        parent (str):
            Required. Project, location. E.g.,
            ``projects/myproject/locations/US``
        reservation_id (str):
            The reservation ID. It must only contain
            lower case alphanumeric characters or dashes. It
            must start with a letter and must not end with a
            dash. Its maximum length is 64 characters.
        reservation (google.cloud.bigquery_reservation_v1.types.Reservation):
            Definition of the new reservation to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    reservation_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    reservation: 'Reservation' = proto.Field(
        proto.MESSAGE,
        number=3,
        message='Reservation',
    )


class ListReservationsRequest(proto.Message):
    r"""The request for
    [ReservationService.ListReservations][google.cloud.bigquery.reservation.v1.ReservationService.ListReservations].

    Attributes:
        parent (str):
            Required. The parent resource name containing project and
            location, e.g.: ``projects/myproject/locations/US``
        page_size (int):
            The maximum number of items to return per
            page.
        page_token (str):
            The next_page_token value returned from a previous List
            request, if any.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=2,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ListReservationsResponse(proto.Message):
    r"""The response for
    [ReservationService.ListReservations][google.cloud.bigquery.reservation.v1.ReservationService.ListReservations].

    Attributes:
        reservations (MutableSequence[google.cloud.bigquery_reservation_v1.types.Reservation]):
            List of reservations visible to the user.
        next_page_token (str):
            Token to retrieve the next page of results,
            or empty if there are no more results in the
            list.
    """

    @property
    def raw_page(self):
        return self

    reservations: MutableSequence['Reservation'] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message='Reservation',
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetReservationRequest(proto.Message):
    r"""The request for
    [ReservationService.GetReservation][google.cloud.bigquery.reservation.v1.ReservationService.GetReservation].

    Attributes:
        name (str):
            Required. Resource name of the reservation to retrieve.
            E.g.,
            ``projects/myproject/locations/US/reservations/team1-prod``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class DeleteReservationRequest(proto.Message):
    r"""The request for
    [ReservationService.DeleteReservation][google.cloud.bigquery.reservation.v1.ReservationService.DeleteReservation].

    Attributes:
        name (str):
            Required. Resource name of the reservation to retrieve.
            E.g.,
            ``projects/myproject/locations/US/reservations/team1-prod``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateReservationRequest(proto.Message):
    r"""The request for
    [ReservationService.UpdateReservation][google.cloud.bigquery.reservation.v1.ReservationService.UpdateReservation].

    Attributes:
        reservation (google.cloud.bigquery_reservation_v1.types.Reservation):
            Content of the reservation to update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Standard field mask for the set of fields to
            be updated.
    """

    reservation: 'Reservation' = proto.Field(
        proto.MESSAGE,
        number=1,
        message='Reservation',
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class CreateCapacityCommitmentRequest(proto.Message):
    r"""The request for
    [ReservationService.CreateCapacityCommitment][google.cloud.bigquery.reservation.v1.ReservationService.CreateCapacityCommitment].

    Attributes:
        parent (str):
            Required. Resource name of the parent reservation. E.g.,
            ``projects/myproject/locations/US``
        capacity_commitment (google.cloud.bigquery_reservation_v1.types.CapacityCommitment):
            Content of the capacity commitment to create.
        enforce_single_admin_project_per_org (bool):
            If true, fail the request if another project
            in the organization has a capacity commitment.
        capacity_commitment_id (str):
            The optional capacity commitment ID. Capacity
            commitment name will be generated automatically
            if this field is empty. This field must only
            contain lower case alphanumeric characters or
            dashes. The first and last character cannot be a
            dash. Max length is 64 characters. NOTE: this ID
            won't be kept if the capacity commitment is
            split or merged.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    capacity_commitment: 'CapacityCommitment' = proto.Field(
        proto.MESSAGE,
        number=2,
        message='CapacityCommitment',
    )
    enforce_single_admin_project_per_org: bool = proto.Field(
        proto.BOOL,
        number=4,
    )
    capacity_commitment_id: str = proto.Field(
        proto.STRING,
        number=5,
    )


class ListCapacityCommitmentsRequest(proto.Message):
    r"""The request for
    [ReservationService.ListCapacityCommitments][google.cloud.bigquery.reservation.v1.ReservationService.ListCapacityCommitments].

    Attributes:
        parent (str):
            Required. Resource name of the parent reservation. E.g.,
            ``projects/myproject/locations/US``
        page_size (int):
            The maximum number of items to return.
        page_token (str):
            The next_page_token value returned from a previous List
            request, if any.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=2,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ListCapacityCommitmentsResponse(proto.Message):
    r"""The response for
    [ReservationService.ListCapacityCommitments][google.cloud.bigquery.reservation.v1.ReservationService.ListCapacityCommitments].

    Attributes:
        capacity_commitments (MutableSequence[google.cloud.bigquery_reservation_v1.types.CapacityCommitment]):
            List of capacity commitments visible to the
            user.
        next_page_token (str):
            Token to retrieve the next page of results,
            or empty if there are no more results in the
            list.
    """

    @property
    def raw_page(self):
        return self

    capacity_commitments: MutableSequence['CapacityCommitment'] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message='CapacityCommitment',
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetCapacityCommitmentRequest(proto.Message):
    r"""The request for
    [ReservationService.GetCapacityCommitment][google.cloud.bigquery.reservation.v1.ReservationService.GetCapacityCommitment].

    Attributes:
        name (str):
            Required. Resource name of the capacity commitment to
            retrieve. E.g.,
            ``projects/myproject/locations/US/capacityCommitments/123``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class DeleteCapacityCommitmentRequest(proto.Message):
    r"""The request for
    [ReservationService.DeleteCapacityCommitment][google.cloud.bigquery.reservation.v1.ReservationService.DeleteCapacityCommitment].

    Attributes:
        name (str):
            Required. Resource name of the capacity commitment to
            delete. E.g.,
            ``projects/myproject/locations/US/capacityCommitments/123``
        force (bool):
            Can be used to force delete commitments even
            if assignments exist. Deleting commitments with
            assignments may cause queries to fail if they no
            longer have access to slots.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    force: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


class UpdateCapacityCommitmentRequest(proto.Message):
    r"""The request for
    [ReservationService.UpdateCapacityCommitment][google.cloud.bigquery.reservation.v1.ReservationService.UpdateCapacityCommitment].

    Attributes:
        capacity_commitment (google.cloud.bigquery_reservation_v1.types.CapacityCommitment):
            Content of the capacity commitment to update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Standard field mask for the set of fields to
            be updated.
    """

    capacity_commitment: 'CapacityCommitment' = proto.Field(
        proto.MESSAGE,
        number=1,
        message='CapacityCommitment',
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class SplitCapacityCommitmentRequest(proto.Message):
    r"""The request for
    [ReservationService.SplitCapacityCommitment][google.cloud.bigquery.reservation.v1.ReservationService.SplitCapacityCommitment].

    Attributes:
        name (str):
            Required. The resource name e.g.,:
            ``projects/myproject/locations/US/capacityCommitments/123``
        slot_count (int):
            Number of slots in the capacity commitment
            after the split.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    slot_count: int = proto.Field(
        proto.INT64,
        number=2,
    )


class SplitCapacityCommitmentResponse(proto.Message):
    r"""The response for
    [ReservationService.SplitCapacityCommitment][google.cloud.bigquery.reservation.v1.ReservationService.SplitCapacityCommitment].

    Attributes:
        first (google.cloud.bigquery_reservation_v1.types.CapacityCommitment):
            First capacity commitment, result of a split.
        second (google.cloud.bigquery_reservation_v1.types.CapacityCommitment):
            Second capacity commitment, result of a
            split.
    """

    first: 'CapacityCommitment' = proto.Field(
        proto.MESSAGE,
        number=1,
        message='CapacityCommitment',
    )
    second: 'CapacityCommitment' = proto.Field(
        proto.MESSAGE,
        number=2,
        message='CapacityCommitment',
    )


class MergeCapacityCommitmentsRequest(proto.Message):
    r"""The request for
    [ReservationService.MergeCapacityCommitments][google.cloud.bigquery.reservation.v1.ReservationService.MergeCapacityCommitments].

    Attributes:
        parent (str):
            Parent resource that identifies admin project and location
            e.g., ``projects/myproject/locations/us``
        capacity_commitment_ids (MutableSequence[str]):
            Ids of capacity commitments to merge.
            These capacity commitments must exist under
            admin project and location specified in the
            parent.
            ID is the last portion of capacity commitment
            name e.g., 'abc' for
            projects/myproject/locations/US/capacityCommitments/abc
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    capacity_commitment_ids: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class Assignment(proto.Message):
    r"""An assignment allows a project to submit jobs
    of a certain type using slots from the specified reservation.

    Attributes:
        name (str):
            Output only. Name of the resource. E.g.:
            ``projects/myproject/locations/US/reservations/team1-prod/assignments/123``.
            The assignment_id must only contain lower case alphanumeric
            characters or dashes and the max length is 64 characters.
        assignee (str):
            The resource which will use the reservation. E.g.
            ``projects/myproject``, ``folders/123``, or
            ``organizations/456``.
        job_type (google.cloud.bigquery_reservation_v1.types.Assignment.JobType):
            Which type of jobs will use the reservation.
        state (google.cloud.bigquery_reservation_v1.types.Assignment.State):
            Output only. State of the assignment.
    """
    class JobType(proto.Enum):
        r"""Types of job, which could be specified when using the
        reservation.
        """
        JOB_TYPE_UNSPECIFIED = 0
        PIPELINE = 1
        QUERY = 2
        ML_EXTERNAL = 3

    class State(proto.Enum):
        r"""Assignment will remain in PENDING state if no active capacity
        commitment is present. It will become ACTIVE when some capacity
        commitment becomes active.
        """
        STATE_UNSPECIFIED = 0
        PENDING = 1
        ACTIVE = 2

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    assignee: str = proto.Field(
        proto.STRING,
        number=4,
    )
    job_type: JobType = proto.Field(
        proto.ENUM,
        number=3,
        enum=JobType,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=6,
        enum=State,
    )


class CreateAssignmentRequest(proto.Message):
    r"""The request for
    [ReservationService.CreateAssignment][google.cloud.bigquery.reservation.v1.ReservationService.CreateAssignment].
    Note: "bigquery.reservationAssignments.create" permission is
    required on the related assignee.

    Attributes:
        parent (str):
            Required. The parent resource name of the assignment E.g.
            ``projects/myproject/locations/US/reservations/team1-prod``
        assignment (google.cloud.bigquery_reservation_v1.types.Assignment):
            Assignment resource to create.
        assignment_id (str):
            The optional assignment ID. Assignment name
            will be generated automatically if this field is
            empty. This field must only contain lower case
            alphanumeric characters or dashes. Max length is
            64 characters.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    assignment: 'Assignment' = proto.Field(
        proto.MESSAGE,
        number=2,
        message='Assignment',
    )
    assignment_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class ListAssignmentsRequest(proto.Message):
    r"""The request for
    [ReservationService.ListAssignments][google.cloud.bigquery.reservation.v1.ReservationService.ListAssignments].

    Attributes:
        parent (str):
            Required. The parent resource name e.g.:

            ``projects/myproject/locations/US/reservations/team1-prod``

            Or:

            ``projects/myproject/locations/US/reservations/-``
        page_size (int):
            The maximum number of items to return per
            page.
        page_token (str):
            The next_page_token value returned from a previous List
            request, if any.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=2,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ListAssignmentsResponse(proto.Message):
    r"""The response for
    [ReservationService.ListAssignments][google.cloud.bigquery.reservation.v1.ReservationService.ListAssignments].

    Attributes:
        assignments (MutableSequence[google.cloud.bigquery_reservation_v1.types.Assignment]):
            List of assignments visible to the user.
        next_page_token (str):
            Token to retrieve the next page of results,
            or empty if there are no more results in the
            list.
    """

    @property
    def raw_page(self):
        return self

    assignments: MutableSequence['Assignment'] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message='Assignment',
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class DeleteAssignmentRequest(proto.Message):
    r"""The request for
    [ReservationService.DeleteAssignment][google.cloud.bigquery.reservation.v1.ReservationService.DeleteAssignment].
    Note: "bigquery.reservationAssignments.delete" permission is
    required on the related assignee.

    Attributes:
        name (str):
            Required. Name of the resource, e.g.
            ``projects/myproject/locations/US/reservations/team1-prod/assignments/123``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class SearchAssignmentsRequest(proto.Message):
    r"""The request for
    [ReservationService.SearchAssignments][google.cloud.bigquery.reservation.v1.ReservationService.SearchAssignments].
    Note: "bigquery.reservationAssignments.search" permission is
    required on the related assignee.

    Attributes:
        parent (str):
            Required. The resource name of the admin project(containing
            project and location), e.g.:
            ``projects/myproject/locations/US``.
        query (str):
            Please specify resource name as assignee in the query.

            Examples:

            -  ``assignee=projects/myproject``
            -  ``assignee=folders/123``
            -  ``assignee=organizations/456``
        page_size (int):
            The maximum number of items to return per
            page.
        page_token (str):
            The next_page_token value returned from a previous List
            request, if any.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    query: str = proto.Field(
        proto.STRING,
        number=2,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=3,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=4,
    )


class SearchAllAssignmentsRequest(proto.Message):
    r"""The request for
    [ReservationService.SearchAllAssignments][google.cloud.bigquery.reservation.v1.ReservationService.SearchAllAssignments].
    Note: "bigquery.reservationAssignments.search" permission is
    required on the related assignee.

    Attributes:
        parent (str):
            Required. The resource name with location (project name
            could be the wildcard '-'), e.g.:
            ``projects/-/locations/US``.
        query (str):
            Please specify resource name as assignee in the query.

            Examples:

            -  ``assignee=projects/myproject``
            -  ``assignee=folders/123``
            -  ``assignee=organizations/456``
        page_size (int):
            The maximum number of items to return per
            page.
        page_token (str):
            The next_page_token value returned from a previous List
            request, if any.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    query: str = proto.Field(
        proto.STRING,
        number=2,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=3,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=4,
    )


class SearchAssignmentsResponse(proto.Message):
    r"""The response for
    [ReservationService.SearchAssignments][google.cloud.bigquery.reservation.v1.ReservationService.SearchAssignments].

    Attributes:
        assignments (MutableSequence[google.cloud.bigquery_reservation_v1.types.Assignment]):
            List of assignments visible to the user.
        next_page_token (str):
            Token to retrieve the next page of results,
            or empty if there are no more results in the
            list.
    """

    @property
    def raw_page(self):
        return self

    assignments: MutableSequence['Assignment'] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message='Assignment',
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class SearchAllAssignmentsResponse(proto.Message):
    r"""The response for
    [ReservationService.SearchAllAssignments][google.cloud.bigquery.reservation.v1.ReservationService.SearchAllAssignments].

    Attributes:
        assignments (MutableSequence[google.cloud.bigquery_reservation_v1.types.Assignment]):
            List of assignments visible to the user.
        next_page_token (str):
            Token to retrieve the next page of results,
            or empty if there are no more results in the
            list.
    """

    @property
    def raw_page(self):
        return self

    assignments: MutableSequence['Assignment'] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message='Assignment',
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class MoveAssignmentRequest(proto.Message):
    r"""The request for
    [ReservationService.MoveAssignment][google.cloud.bigquery.reservation.v1.ReservationService.MoveAssignment].

    **Note**: "bigquery.reservationAssignments.create" permission is
    required on the destination_id.

    **Note**: "bigquery.reservationAssignments.create" and
    "bigquery.reservationAssignments.delete" permission are required on
    the related assignee.

    Attributes:
        name (str):
            Required. The resource name of the assignment, e.g.
            ``projects/myproject/locations/US/reservations/team1-prod/assignments/123``
        destination_id (str):
            The new reservation ID, e.g.:
            ``projects/myotherproject/locations/US/reservations/team2-prod``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    destination_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class UpdateAssignmentRequest(proto.Message):
    r"""The request for
    [ReservationService.UpdateAssignment][google.cloud.bigquery.reservation.v1.ReservationService.UpdateAssignment].

    Attributes:
        assignment (google.cloud.bigquery_reservation_v1.types.Assignment):
            Content of the assignment to update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Standard field mask for the set of fields to
            be updated.
    """

    assignment: 'Assignment' = proto.Field(
        proto.MESSAGE,
        number=1,
        message='Assignment',
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class TableReference(proto.Message):
    r"""Fully qualified reference to BigQuery table.
    Internally stored as google.cloud.bi.v1.BqTableReference.

    Attributes:
        project_id (str):
            The assigned project ID of the project.
        dataset_id (str):
            The ID of the dataset in the above project.
        table_id (str):
            The ID of the table in the above dataset.
    """

    project_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    dataset_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    table_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class BiReservation(proto.Message):
    r"""Represents a BI Reservation.

    Attributes:
        name (str):
            The resource name of the singleton BI reservation.
            Reservation names have the form
            ``projects/{project_id}/locations/{location_id}/biReservation``.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The last update timestamp of a
            reservation.
        size (int):
            Size of a reservation, in bytes.
        preferred_tables (MutableSequence[google.cloud.bigquery_reservation_v1.types.TableReference]):
            Preferred tables to use BI capacity for.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    size: int = proto.Field(
        proto.INT64,
        number=4,
    )
    preferred_tables: MutableSequence['TableReference'] = proto.RepeatedField(
        proto.MESSAGE,
        number=5,
        message='TableReference',
    )


class GetBiReservationRequest(proto.Message):
    r"""A request to get a singleton BI reservation.

    Attributes:
        name (str):
            Required. Name of the requested reservation, for example:
            ``projects/{project_id}/locations/{location_id}/biReservation``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateBiReservationRequest(proto.Message):
    r"""A request to update a BI reservation.

    Attributes:
        bi_reservation (google.cloud.bigquery_reservation_v1.types.BiReservation):
            A reservation to update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            A list of fields to be updated in this
            request.
    """

    bi_reservation: 'BiReservation' = proto.Field(
        proto.MESSAGE,
        number=1,
        message='BiReservation',
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
