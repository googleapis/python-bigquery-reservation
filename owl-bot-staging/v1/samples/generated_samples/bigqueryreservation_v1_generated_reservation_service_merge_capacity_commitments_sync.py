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
# Generated code. DO NOT EDIT!
#
# Snippet for MergeCapacityCommitments
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-bigquery-reservation


# [START bigqueryreservation_v1_generated_ReservationService_MergeCapacityCommitments_sync]
from google.cloud import bigquery_reservation_v1


def sample_merge_capacity_commitments():
    # Create a client
    client = bigquery_reservation_v1.ReservationServiceClient()

    # Initialize request argument(s)
    request = bigquery_reservation_v1.MergeCapacityCommitmentsRequest(
    )

    # Make the request
    response = client.merge_capacity_commitments(request=request)

    # Handle the response
    print(response)

# [END bigqueryreservation_v1_generated_ReservationService_MergeCapacityCommitments_sync]
