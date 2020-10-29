# -*- coding: utf-8 -*-
#
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

"""Unit tests."""

import mock
import pytest

from google.cloud import bigquery_reservation_v1
from google.cloud.bigquery_reservation_v1.proto import reservation_pb2
from google.protobuf import empty_pb2


class MultiCallableStub(object):
    """Stub for the grpc.UnaryUnaryMultiCallable interface."""

    def __init__(self, method, channel_stub):
        self.method = method
        self.channel_stub = channel_stub

    def __call__(self, request, timeout=None, metadata=None, credentials=None):
        self.channel_stub.requests.append((self.method, request))

        response = None
        if self.channel_stub.responses:
            response = self.channel_stub.responses.pop()

        if isinstance(response, Exception):
            raise response

        if response:
            return response


class ChannelStub(object):
    """Stub for the grpc.Channel interface."""

    def __init__(self, responses=[]):
        self.responses = responses
        self.requests = []

    def unary_unary(self, method, request_serializer=None, response_deserializer=None):
        return MultiCallableStub(method, self)


class CustomException(Exception):
    pass


class TestReservationServiceClient(object):
    def test_create_reservation(self):
        # Setup Expected Response
        name = "name3373707"
        slot_capacity = 1516717605
        ignore_idle_slots = False
        expected_response = {
            "name": name,
            "slot_capacity": slot_capacity,
            "ignore_idle_slots": ignore_idle_slots,
        }
        expected_response = reservation_pb2.Reservation(**expected_response)

        # Mock the API response
        channel = ChannelStub(responses=[expected_response])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = bigquery_reservation_v1.ReservationServiceClient()

        # Setup Request
        parent = client.location_path("[PROJECT]", "[LOCATION]")

        response = client.create_reservation(parent)
        assert expected_response == response

        assert len(channel.requests) == 1
        expected_request = reservation_pb2.CreateReservationRequest(parent=parent)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_create_reservation_exception(self):
        # Mock the API response
        channel = ChannelStub(responses=[CustomException()])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = bigquery_reservation_v1.ReservationServiceClient()

        # Setup request
        parent = client.location_path("[PROJECT]", "[LOCATION]")

        with pytest.raises(CustomException):
            client.create_reservation(parent)

    def test_list_reservations(self):
        # Setup Expected Response
        next_page_token = ""
        reservations_element = {}
        reservations = [reservations_element]
        expected_response = {
            "next_page_token": next_page_token,
            "reservations": reservations,
        }
        expected_response = reservation_pb2.ListReservationsResponse(
            **expected_response
        )

        # Mock the API response
        channel = ChannelStub(responses=[expected_response])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = bigquery_reservation_v1.ReservationServiceClient()

        # Setup Request
        parent = client.location_path("[PROJECT]", "[LOCATION]")

        paged_list_response = client.list_reservations(parent)
        resources = list(paged_list_response)
        assert len(resources) == 1

        assert expected_response.reservations[0] == resources[0]

        assert len(channel.requests) == 1
        expected_request = reservation_pb2.ListReservationsRequest(parent=parent)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_list_reservations_exception(self):
        channel = ChannelStub(responses=[CustomException()])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = bigquery_reservation_v1.ReservationServiceClient()

        # Setup request
        parent = client.location_path("[PROJECT]", "[LOCATION]")

        paged_list_response = client.list_reservations(parent)
        with pytest.raises(CustomException):
            list(paged_list_response)

    def test_get_reservation(self):
        # Setup Expected Response
        name_2 = "name2-1052831874"
        slot_capacity = 1516717605
        ignore_idle_slots = False
        expected_response = {
            "name": name_2,
            "slot_capacity": slot_capacity,
            "ignore_idle_slots": ignore_idle_slots,
        }
        expected_response = reservation_pb2.Reservation(**expected_response)

        # Mock the API response
        channel = ChannelStub(responses=[expected_response])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = bigquery_reservation_v1.ReservationServiceClient()

        # Setup Request
        name = client.reservation_path("[PROJECT]", "[LOCATION]", "[RESERVATION]")

        response = client.get_reservation(name)
        assert expected_response == response

        assert len(channel.requests) == 1
        expected_request = reservation_pb2.GetReservationRequest(name=name)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_get_reservation_exception(self):
        # Mock the API response
        channel = ChannelStub(responses=[CustomException()])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = bigquery_reservation_v1.ReservationServiceClient()

        # Setup request
        name = client.reservation_path("[PROJECT]", "[LOCATION]", "[RESERVATION]")

        with pytest.raises(CustomException):
            client.get_reservation(name)

    def test_delete_reservation(self):
        channel = ChannelStub()
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = bigquery_reservation_v1.ReservationServiceClient()

        # Setup Request
        name = client.reservation_path("[PROJECT]", "[LOCATION]", "[RESERVATION]")

        client.delete_reservation(name)

        assert len(channel.requests) == 1
        expected_request = reservation_pb2.DeleteReservationRequest(name=name)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_delete_reservation_exception(self):
        # Mock the API response
        channel = ChannelStub(responses=[CustomException()])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = bigquery_reservation_v1.ReservationServiceClient()

        # Setup request
        name = client.reservation_path("[PROJECT]", "[LOCATION]", "[RESERVATION]")

        with pytest.raises(CustomException):
            client.delete_reservation(name)

    def test_update_reservation(self):
        # Setup Expected Response
        name = "name3373707"
        slot_capacity = 1516717605
        ignore_idle_slots = False
        expected_response = {
            "name": name,
            "slot_capacity": slot_capacity,
            "ignore_idle_slots": ignore_idle_slots,
        }
        expected_response = reservation_pb2.Reservation(**expected_response)

        # Mock the API response
        channel = ChannelStub(responses=[expected_response])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = bigquery_reservation_v1.ReservationServiceClient()

        response = client.update_reservation()
        assert expected_response == response

        assert len(channel.requests) == 1
        expected_request = reservation_pb2.UpdateReservationRequest()
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_update_reservation_exception(self):
        # Mock the API response
        channel = ChannelStub(responses=[CustomException()])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = bigquery_reservation_v1.ReservationServiceClient()

        with pytest.raises(CustomException):
            client.update_reservation()

    def test_create_capacity_commitment(self):
        # Setup Expected Response
        name = "name3373707"
        slot_count = 191518834
        expected_response = {"name": name, "slot_count": slot_count}
        expected_response = reservation_pb2.CapacityCommitment(**expected_response)

        # Mock the API response
        channel = ChannelStub(responses=[expected_response])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = bigquery_reservation_v1.ReservationServiceClient()

        # Setup Request
        parent = client.location_path("[PROJECT]", "[LOCATION]")

        response = client.create_capacity_commitment(parent)
        assert expected_response == response

        assert len(channel.requests) == 1
        expected_request = reservation_pb2.CreateCapacityCommitmentRequest(
            parent=parent
        )
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_create_capacity_commitment_exception(self):
        # Mock the API response
        channel = ChannelStub(responses=[CustomException()])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = bigquery_reservation_v1.ReservationServiceClient()

        # Setup request
        parent = client.location_path("[PROJECT]", "[LOCATION]")

        with pytest.raises(CustomException):
            client.create_capacity_commitment(parent)

    def test_list_capacity_commitments(self):
        # Setup Expected Response
        next_page_token = ""
        capacity_commitments_element = {}
        capacity_commitments = [capacity_commitments_element]
        expected_response = {
            "next_page_token": next_page_token,
            "capacity_commitments": capacity_commitments,
        }
        expected_response = reservation_pb2.ListCapacityCommitmentsResponse(
            **expected_response
        )

        # Mock the API response
        channel = ChannelStub(responses=[expected_response])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = bigquery_reservation_v1.ReservationServiceClient()

        # Setup Request
        parent = client.location_path("[PROJECT]", "[LOCATION]")

        paged_list_response = client.list_capacity_commitments(parent)
        resources = list(paged_list_response)
        assert len(resources) == 1

        assert expected_response.capacity_commitments[0] == resources[0]

        assert len(channel.requests) == 1
        expected_request = reservation_pb2.ListCapacityCommitmentsRequest(parent=parent)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_list_capacity_commitments_exception(self):
        channel = ChannelStub(responses=[CustomException()])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = bigquery_reservation_v1.ReservationServiceClient()

        # Setup request
        parent = client.location_path("[PROJECT]", "[LOCATION]")

        paged_list_response = client.list_capacity_commitments(parent)
        with pytest.raises(CustomException):
            list(paged_list_response)

    def test_get_capacity_commitment(self):
        # Setup Expected Response
        name_2 = "name2-1052831874"
        slot_count = 191518834
        expected_response = {"name": name_2, "slot_count": slot_count}
        expected_response = reservation_pb2.CapacityCommitment(**expected_response)

        # Mock the API response
        channel = ChannelStub(responses=[expected_response])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = bigquery_reservation_v1.ReservationServiceClient()

        # Setup Request
        name = client.capacity_commitment_path(
            "[PROJECT]", "[LOCATION]", "[CAPACITY_COMMITMENT]"
        )

        response = client.get_capacity_commitment(name)
        assert expected_response == response

        assert len(channel.requests) == 1
        expected_request = reservation_pb2.GetCapacityCommitmentRequest(name=name)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_get_capacity_commitment_exception(self):
        # Mock the API response
        channel = ChannelStub(responses=[CustomException()])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = bigquery_reservation_v1.ReservationServiceClient()

        # Setup request
        name = client.capacity_commitment_path(
            "[PROJECT]", "[LOCATION]", "[CAPACITY_COMMITMENT]"
        )

        with pytest.raises(CustomException):
            client.get_capacity_commitment(name)

    def test_delete_capacity_commitment(self):
        channel = ChannelStub()
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = bigquery_reservation_v1.ReservationServiceClient()

        # Setup Request
        name = client.capacity_commitment_path(
            "[PROJECT]", "[LOCATION]", "[CAPACITY_COMMITMENT]"
        )

        client.delete_capacity_commitment(name)

        assert len(channel.requests) == 1
        expected_request = reservation_pb2.DeleteCapacityCommitmentRequest(name=name)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_delete_capacity_commitment_exception(self):
        # Mock the API response
        channel = ChannelStub(responses=[CustomException()])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = bigquery_reservation_v1.ReservationServiceClient()

        # Setup request
        name = client.capacity_commitment_path(
            "[PROJECT]", "[LOCATION]", "[CAPACITY_COMMITMENT]"
        )

        with pytest.raises(CustomException):
            client.delete_capacity_commitment(name)

    def test_update_capacity_commitment(self):
        # Setup Expected Response
        name = "name3373707"
        slot_count = 191518834
        expected_response = {"name": name, "slot_count": slot_count}
        expected_response = reservation_pb2.CapacityCommitment(**expected_response)

        # Mock the API response
        channel = ChannelStub(responses=[expected_response])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = bigquery_reservation_v1.ReservationServiceClient()

        response = client.update_capacity_commitment()
        assert expected_response == response

        assert len(channel.requests) == 1
        expected_request = reservation_pb2.UpdateCapacityCommitmentRequest()
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_update_capacity_commitment_exception(self):
        # Mock the API response
        channel = ChannelStub(responses=[CustomException()])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = bigquery_reservation_v1.ReservationServiceClient()

        with pytest.raises(CustomException):
            client.update_capacity_commitment()

    def test_split_capacity_commitment(self):
        # Setup Expected Response
        expected_response = {}
        expected_response = reservation_pb2.SplitCapacityCommitmentResponse(
            **expected_response
        )

        # Mock the API response
        channel = ChannelStub(responses=[expected_response])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = bigquery_reservation_v1.ReservationServiceClient()

        # Setup Request
        name = client.capacity_commitment_path(
            "[PROJECT]", "[LOCATION]", "[CAPACITY_COMMITMENT]"
        )

        response = client.split_capacity_commitment(name)
        assert expected_response == response

        assert len(channel.requests) == 1
        expected_request = reservation_pb2.SplitCapacityCommitmentRequest(name=name)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_split_capacity_commitment_exception(self):
        # Mock the API response
        channel = ChannelStub(responses=[CustomException()])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = bigquery_reservation_v1.ReservationServiceClient()

        # Setup request
        name = client.capacity_commitment_path(
            "[PROJECT]", "[LOCATION]", "[CAPACITY_COMMITMENT]"
        )

        with pytest.raises(CustomException):
            client.split_capacity_commitment(name)

    def test_merge_capacity_commitments(self):
        # Setup Expected Response
        name = "name3373707"
        slot_count = 191518834
        expected_response = {"name": name, "slot_count": slot_count}
        expected_response = reservation_pb2.CapacityCommitment(**expected_response)

        # Mock the API response
        channel = ChannelStub(responses=[expected_response])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = bigquery_reservation_v1.ReservationServiceClient()

        response = client.merge_capacity_commitments()
        assert expected_response == response

        assert len(channel.requests) == 1
        expected_request = reservation_pb2.MergeCapacityCommitmentsRequest()
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_merge_capacity_commitments_exception(self):
        # Mock the API response
        channel = ChannelStub(responses=[CustomException()])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = bigquery_reservation_v1.ReservationServiceClient()

        with pytest.raises(CustomException):
            client.merge_capacity_commitments()

    def test_create_assignment(self):
        # Setup Expected Response
        name = "name3373707"
        assignee = "assignee-369881649"
        expected_response = {"name": name, "assignee": assignee}
        expected_response = reservation_pb2.Assignment(**expected_response)

        # Mock the API response
        channel = ChannelStub(responses=[expected_response])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = bigquery_reservation_v1.ReservationServiceClient()

        # Setup Request
        parent = client.reservation_path("[PROJECT]", "[LOCATION]", "[RESERVATION]")

        response = client.create_assignment(parent)
        assert expected_response == response

        assert len(channel.requests) == 1
        expected_request = reservation_pb2.CreateAssignmentRequest(parent=parent)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_create_assignment_exception(self):
        # Mock the API response
        channel = ChannelStub(responses=[CustomException()])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = bigquery_reservation_v1.ReservationServiceClient()

        # Setup request
        parent = client.reservation_path("[PROJECT]", "[LOCATION]", "[RESERVATION]")

        with pytest.raises(CustomException):
            client.create_assignment(parent)

    def test_list_assignments(self):
        # Setup Expected Response
        next_page_token = ""
        assignments_element = {}
        assignments = [assignments_element]
        expected_response = {
            "next_page_token": next_page_token,
            "assignments": assignments,
        }
        expected_response = reservation_pb2.ListAssignmentsResponse(**expected_response)

        # Mock the API response
        channel = ChannelStub(responses=[expected_response])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = bigquery_reservation_v1.ReservationServiceClient()

        # Setup Request
        parent = client.reservation_path("[PROJECT]", "[LOCATION]", "[RESERVATION]")

        paged_list_response = client.list_assignments(parent)
        resources = list(paged_list_response)
        assert len(resources) == 1

        assert expected_response.assignments[0] == resources[0]

        assert len(channel.requests) == 1
        expected_request = reservation_pb2.ListAssignmentsRequest(parent=parent)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_list_assignments_exception(self):
        channel = ChannelStub(responses=[CustomException()])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = bigquery_reservation_v1.ReservationServiceClient()

        # Setup request
        parent = client.reservation_path("[PROJECT]", "[LOCATION]", "[RESERVATION]")

        paged_list_response = client.list_assignments(parent)
        with pytest.raises(CustomException):
            list(paged_list_response)

    def test_delete_assignment(self):
        channel = ChannelStub()
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = bigquery_reservation_v1.ReservationServiceClient()

        # Setup Request
        name = client.assignment_path(
            "[PROJECT]", "[LOCATION]", "[RESERVATION]", "[ASSIGNMENT]"
        )

        client.delete_assignment(name)

        assert len(channel.requests) == 1
        expected_request = reservation_pb2.DeleteAssignmentRequest(name=name)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_delete_assignment_exception(self):
        # Mock the API response
        channel = ChannelStub(responses=[CustomException()])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = bigquery_reservation_v1.ReservationServiceClient()

        # Setup request
        name = client.assignment_path(
            "[PROJECT]", "[LOCATION]", "[RESERVATION]", "[ASSIGNMENT]"
        )

        with pytest.raises(CustomException):
            client.delete_assignment(name)

    def test_search_assignments(self):
        # Setup Expected Response
        next_page_token = ""
        assignments_element = {}
        assignments = [assignments_element]
        expected_response = {
            "next_page_token": next_page_token,
            "assignments": assignments,
        }
        expected_response = reservation_pb2.SearchAssignmentsResponse(
            **expected_response
        )

        # Mock the API response
        channel = ChannelStub(responses=[expected_response])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = bigquery_reservation_v1.ReservationServiceClient()

        # Setup Request
        parent = client.location_path("[PROJECT]", "[LOCATION]")

        paged_list_response = client.search_assignments(parent)
        resources = list(paged_list_response)
        assert len(resources) == 1

        assert expected_response.assignments[0] == resources[0]

        assert len(channel.requests) == 1
        expected_request = reservation_pb2.SearchAssignmentsRequest(parent=parent)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_search_assignments_exception(self):
        channel = ChannelStub(responses=[CustomException()])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = bigquery_reservation_v1.ReservationServiceClient()

        # Setup request
        parent = client.location_path("[PROJECT]", "[LOCATION]")

        paged_list_response = client.search_assignments(parent)
        with pytest.raises(CustomException):
            list(paged_list_response)

    def test_move_assignment(self):
        # Setup Expected Response
        name_2 = "name2-1052831874"
        assignee = "assignee-369881649"
        expected_response = {"name": name_2, "assignee": assignee}
        expected_response = reservation_pb2.Assignment(**expected_response)

        # Mock the API response
        channel = ChannelStub(responses=[expected_response])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = bigquery_reservation_v1.ReservationServiceClient()

        # Setup Request
        name = client.assignment_path(
            "[PROJECT]", "[LOCATION]", "[RESERVATION]", "[ASSIGNMENT]"
        )

        response = client.move_assignment(name)
        assert expected_response == response

        assert len(channel.requests) == 1
        expected_request = reservation_pb2.MoveAssignmentRequest(name=name)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_move_assignment_exception(self):
        # Mock the API response
        channel = ChannelStub(responses=[CustomException()])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = bigquery_reservation_v1.ReservationServiceClient()

        # Setup request
        name = client.assignment_path(
            "[PROJECT]", "[LOCATION]", "[RESERVATION]", "[ASSIGNMENT]"
        )

        with pytest.raises(CustomException):
            client.move_assignment(name)

    def test_get_bi_reservation(self):
        # Setup Expected Response
        name_2 = "name2-1052831874"
        size = 3530753
        expected_response = {"name": name_2, "size": size}
        expected_response = reservation_pb2.BiReservation(**expected_response)

        # Mock the API response
        channel = ChannelStub(responses=[expected_response])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = bigquery_reservation_v1.ReservationServiceClient()

        # Setup Request
        name = client.bi_reservation_path("[PROJECT]", "[LOCATION]")

        response = client.get_bi_reservation(name)
        assert expected_response == response

        assert len(channel.requests) == 1
        expected_request = reservation_pb2.GetBiReservationRequest(name=name)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_get_bi_reservation_exception(self):
        # Mock the API response
        channel = ChannelStub(responses=[CustomException()])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = bigquery_reservation_v1.ReservationServiceClient()

        # Setup request
        name = client.bi_reservation_path("[PROJECT]", "[LOCATION]")

        with pytest.raises(CustomException):
            client.get_bi_reservation(name)

    def test_update_bi_reservation(self):
        # Setup Expected Response
        name = "name3373707"
        size = 3530753
        expected_response = {"name": name, "size": size}
        expected_response = reservation_pb2.BiReservation(**expected_response)

        # Mock the API response
        channel = ChannelStub(responses=[expected_response])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = bigquery_reservation_v1.ReservationServiceClient()

        response = client.update_bi_reservation()
        assert expected_response == response

        assert len(channel.requests) == 1
        expected_request = reservation_pb2.UpdateBiReservationRequest()
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_update_bi_reservation_exception(self):
        # Mock the API response
        channel = ChannelStub(responses=[CustomException()])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = bigquery_reservation_v1.ReservationServiceClient()

        with pytest.raises(CustomException):
            client.update_bi_reservation()
