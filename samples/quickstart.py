# Copyright 2020 Google LLC
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

import argparse
from google.cloud.bigquery import reservation_v1

# [START bigqueryreservation_quickstart]


def main(project_id="your-project-id", location="US"):
    # Constructs the client for interacting with the service.
    client = reservation_v1.ReservationServiceClient()

    report_capacity_commitments(client, project_id, location)
    report_reservations(client, project_id, location)


def report_capacity_commitments(client, project_id, location):
    """ Prints details and summary information about capacity commitments for
        a given admin project and location.
    """
    print(
        "Capacity commitments in project {} in location {}".format(project_id, location)
    )
    req = reservation_v1.types.ListCapacityCommitmentsRequest()
    req.parent = "projects/{}/locations/{}".format(project_id, location)
    total_commitments = 0
    for commitment in client.list_capacity_commitments(request=req):
        print("\tCommitment {} in state {}".format(commitment.name, commitment.state))
        total_commitments = total_commitments + 1
    print("\n{} commitments processed.".format(total_commitments))


def report_reservations(client, project_id, location):
    """ Prints details and summary information about reservations defined within
        a given admin project and location.
    """
    print("Reservations in project {} in location {}".format(project_id, location))
    req = reservation_v1.types.ListReservationsRequest()
    req.parent = "projects/{}/locations/{}".format(project_id, location)
    total_reservations = 0
    for reservation in client.list_reservations(request=req):
        print(
            "\tReservation {} has {} slot capacity.".format(
                reservation.name, reservation.slot_capacity
            )
        )
        total_reservations = total_reservations + 1
    print("\n{} reservations processed.".format(total_reservations))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--project_id", type=str)
    parser.add_argument("--location", default="US", type=str)
    args = parser.parse_args()
    main(project_id=args.project_id, location=args.location)

# [END bigqueryreservation_quickstart]
