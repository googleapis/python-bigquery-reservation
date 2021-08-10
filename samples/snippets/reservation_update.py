# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from google.cloud.bigquery_reservation_v1.types import reservation as reservation_types


def update_reservation(
    project_id: str, location: str, reservation_id: str, slot_capacity: str
) -> reservation_types.Reservation:
    original_project_id = project_id
    original_location = location
    original_reservation_id = reservation_id
    original_slot_capacity = slot_capacity

    # [START bigqueryreservation_reservation_update]
    # TODO(developer): Set project_id to the project ID containing the
    # reservation.
    project_id = "your-project-id"

    # TODO(developer): Set location to the location of the reservation.
    # See: https://cloud.google.com/bigquery/docs/locations for a list of
    # available locations.
    location = "US"

    # TODO(developer): Set reservation_id to a unique ID of the reservation.
    reservation_id = "sample-reservation"

    # TODO(developer): Set slot_capicity to the new number of slots in the
    # reservation.
    slot_capacity = 50

    # [START_EXCLUDE]
    project_id = original_project_id
    location = original_location
    reservation_id = original_reservation_id
    slot_capacity = original_slot_capacity
    # [END_EXCLUDE]

    from google.cloud.bigquery_reservation_v1.services import reservation_service
    from google.cloud.bigquery_reservation_v1.types import (
        reservation as reservation_types,
    )
    from google.protobuf import field_mask_pb2

    reservation_client = reservation_service.ReservationServiceClient()

    reservation_name = reservation_client.reservation_path(
        project_id, location, reservation_id
    )
    reservation = reservation_types.Reservation(
        name=reservation_name, slot_capacity=slot_capacity,
    )
    field_mask = field_mask_pb2.FieldMask(paths=["slot_capacity"])
    reservation = reservation_client.update_reservation(
        reservation=reservation, update_mask=field_mask
    )

    print(f"Updated reservation: {reservation.name}")
    print(f"\tslot_capacity: {reservation.slot_capacity}")
    # [END bigqueryreservation_reservation_update]
    return reservation
