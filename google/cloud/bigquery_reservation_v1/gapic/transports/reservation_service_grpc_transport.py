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


import google.api_core.grpc_helpers

from google.cloud.bigquery_reservation_v1.proto import reservation_pb2_grpc


class ReservationServiceGrpcTransport(object):
    """gRPC transport class providing stubs for
    google.cloud.bigquery.reservation.v1 ReservationService API.

    The transport provides access to the raw gRPC stubs,
    which can be used to take advantage of advanced
    features of gRPC.
    """

    # The scopes needed to make gRPC calls to all of the methods defined
    # in this service.
    _OAUTH_SCOPES = (
        "https://www.googleapis.com/auth/bigquery",
        "https://www.googleapis.com/auth/cloud-platform",
    )

    def __init__(
        self,
        channel=None,
        credentials=None,
        address="bigqueryreservation.googleapis.com:443",
    ):
        """Instantiate the transport class.

        Args:
            channel (grpc.Channel): A ``Channel`` instance through
                which to make calls. This argument is mutually exclusive
                with ``credentials``; providing both will raise an exception.
            credentials (google.auth.credentials.Credentials): The
                authorization credentials to attach to requests. These
                credentials identify this application to the service. If none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            address (str): The address where the service is hosted.
        """
        # If both `channel` and `credentials` are specified, raise an
        # exception (channels come with credentials baked in already).
        if channel is not None and credentials is not None:
            raise ValueError(
                "The `channel` and `credentials` arguments are mutually " "exclusive.",
            )

        # Create the channel.
        if channel is None:
            channel = self.create_channel(
                address=address,
                credentials=credentials,
                options={
                    "grpc.max_send_message_length": -1,
                    "grpc.max_receive_message_length": -1,
                }.items(),
            )

        self._channel = channel

        # gRPC uses objects called "stubs" that are bound to the
        # channel and provide a basic method for each RPC.
        self._stubs = {
            "reservation_service_stub": reservation_pb2_grpc.ReservationServiceStub(
                channel
            ),
        }

    @classmethod
    def create_channel(
        cls,
        address="bigqueryreservation.googleapis.com:443",
        credentials=None,
        **kwargs
    ):
        """Create and return a gRPC channel object.

        Args:
            address (str): The host for the channel to use.
            credentials (~.Credentials): The
                authorization credentials to attach to requests. These
                credentials identify this application to the service. If
                none are specified, the client will attempt to ascertain
                the credentials from the environment.
            kwargs (dict): Keyword arguments, which are passed to the
                channel creation.

        Returns:
            grpc.Channel: A gRPC channel object.
        """
        return google.api_core.grpc_helpers.create_channel(
            address, credentials=credentials, scopes=cls._OAUTH_SCOPES, **kwargs
        )

    @property
    def channel(self):
        """The gRPC channel used by the transport.

        Returns:
            grpc.Channel: A gRPC channel object.
        """
        return self._channel

    @property
    def create_reservation(self):
        """Return the gRPC stub for :meth:`ReservationServiceClient.create_reservation`.

        Creates a new reservation resource.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["reservation_service_stub"].CreateReservation

    @property
    def list_reservations(self):
        """Return the gRPC stub for :meth:`ReservationServiceClient.list_reservations`.

        Lists all the reservations for the project in the specified location.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["reservation_service_stub"].ListReservations

    @property
    def get_reservation(self):
        """Return the gRPC stub for :meth:`ReservationServiceClient.get_reservation`.

        Returns information about the reservation.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["reservation_service_stub"].GetReservation

    @property
    def delete_reservation(self):
        """Return the gRPC stub for :meth:`ReservationServiceClient.delete_reservation`.

        Deletes a reservation. Returns
        ``google.rpc.Code.FAILED_PRECONDITION`` when reservation has
        assignments.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["reservation_service_stub"].DeleteReservation

    @property
    def update_reservation(self):
        """Return the gRPC stub for :meth:`ReservationServiceClient.update_reservation`.

        Updates an existing reservation resource.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["reservation_service_stub"].UpdateReservation

    @property
    def create_capacity_commitment(self):
        """Return the gRPC stub for :meth:`ReservationServiceClient.create_capacity_commitment`.

        Creates a new capacity commitment resource.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["reservation_service_stub"].CreateCapacityCommitment

    @property
    def list_capacity_commitments(self):
        """Return the gRPC stub for :meth:`ReservationServiceClient.list_capacity_commitments`.

        Lists all the capacity commitments for the admin project.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["reservation_service_stub"].ListCapacityCommitments

    @property
    def get_capacity_commitment(self):
        """Return the gRPC stub for :meth:`ReservationServiceClient.get_capacity_commitment`.

        Returns information about the capacity commitment.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["reservation_service_stub"].GetCapacityCommitment

    @property
    def delete_capacity_commitment(self):
        """Return the gRPC stub for :meth:`ReservationServiceClient.delete_capacity_commitment`.

        Deletes a capacity commitment. Attempting to delete capacity
        commitment before its commitment_end_time will fail with the error code
        ``google.rpc.Code.FAILED_PRECONDITION``.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["reservation_service_stub"].DeleteCapacityCommitment

    @property
    def update_capacity_commitment(self):
        """Return the gRPC stub for :meth:`ReservationServiceClient.update_capacity_commitment`.

        Updates an existing capacity commitment.

        Only ``plan`` and ``renewal_plan`` fields can be updated.

        Plan can only be changed to a plan of a longer commitment period.
        Attempting to change to a plan with shorter commitment period will fail
        with the error code ``google.rpc.Code.FAILED_PRECONDITION``.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["reservation_service_stub"].UpdateCapacityCommitment

    @property
    def split_capacity_commitment(self):
        """Return the gRPC stub for :meth:`ReservationServiceClient.split_capacity_commitment`.

        Splits capacity commitment to two commitments of the same plan and
        ``commitment_end_time``.

        A common use case is to enable downgrading commitments.

        For example, in order to downgrade from 10000 slots to 8000, you might
        split a 10000 capacity commitment into commitments of 2000 and 8000.
        Then, you would change the plan of the first one to ``FLEX`` and then
        delete it.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["reservation_service_stub"].SplitCapacityCommitment

    @property
    def merge_capacity_commitments(self):
        """Return the gRPC stub for :meth:`ReservationServiceClient.merge_capacity_commitments`.

        Merges capacity commitments of the same plan into a single
        commitment.

        The resulting capacity commitment has the greater commitment_end_time
        out of the to-be-merged capacity commitments.

        Attempting to merge capacity commitments of different plan will fail
        with the error code ``google.rpc.Code.FAILED_PRECONDITION``.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["reservation_service_stub"].MergeCapacityCommitments

    @property
    def create_assignment(self):
        """Return the gRPC stub for :meth:`ReservationServiceClient.create_assignment`.

        Creates an assignment object which allows the given project to
        submit jobs of a certain type using slots from the specified
        reservation.

        Currently a resource (project, folder, organization) can only have one
        assignment per each (job_type, location) combination, and that
        reservation will be used for all jobs of the matching type.

        Different assignments can be created on different levels of the
        projects, folders or organization hierarchy. During query execution, the
        assignment is looked up at the project, folder and organization levels
        in that order. The first assignment found is applied to the query.

        When creating assignments, it does not matter if other assignments exist
        at higher levels.

        Example:

        -  The organization ``organizationA`` contains two projects,
           ``project1`` and ``project2``.
        -  Assignments for all three entities (``organizationA``, ``project1``,
           and ``project2``) could all be created and mapped to the same or
           different reservations.

        Returns ``google.rpc.Code.PERMISSION_DENIED`` if user does not have
        'bigquery.admin' permissions on the project using the reservation and
        the project that owns this reservation.

        Returns ``google.rpc.Code.INVALID_ARGUMENT`` when location of the
        assignment does not match location of the reservation.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["reservation_service_stub"].CreateAssignment

    @property
    def list_assignments(self):
        """Return the gRPC stub for :meth:`ReservationServiceClient.list_assignments`.

        Lists assignments.

        Only explicitly created assignments will be returned.

        Example:

        -  Organization ``organizationA`` contains two projects, ``project1``
           and ``project2``.
        -  Reservation ``res1`` exists and was created previously.
        -  CreateAssignment was used previously to define the following
           associations between entities and reservations:
           ``<organizationA, res1>`` and ``<project1, res1>``

        In this example, ListAssignments will just return the above two
        assignments for reservation ``res1``, and no expansion/merge will
        happen.

        The wildcard "-" can be used for reservations in the request. In that
        case all assignments belongs to the specified project and location will
        be listed.

        **Note** "-" cannot be used for projects nor locations.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["reservation_service_stub"].ListAssignments

    @property
    def delete_assignment(self):
        """Return the gRPC stub for :meth:`ReservationServiceClient.delete_assignment`.

        Deletes a assignment. No expansion will happen.

        Example:

        -  Organization ``organizationA`` contains two projects, ``project1``
           and ``project2``.
        -  Reservation ``res1`` exists and was created previously.
        -  CreateAssignment was used previously to define the following
           associations between entities and reservations:
           ``<organizationA, res1>`` and ``<project1, res1>``

        In this example, deletion of the ``<organizationA, res1>`` assignment
        won't affect the other assignment ``<project1, res1>``. After said
        deletion, queries from ``project1`` will still use ``res1`` while
        queries from ``project2`` will switch to use on-demand mode.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["reservation_service_stub"].DeleteAssignment

    @property
    def search_assignments(self):
        """Return the gRPC stub for :meth:`ReservationServiceClient.search_assignments`.

        Looks up assignments for a specified resource for a particular
        region. If the request is about a project:

        1. Assignments created on the project will be returned if they exist.
        2. Otherwise assignments created on the closest ancestor will be
           returned.
        3. Assignments for different JobTypes will all be returned.

        The same logic applies if the request is about a folder.

        If the request is about an organization, then assignments created on the
        organization will be returned (organization doesn't have ancestors).

        Comparing to ListAssignments, there are some behavior differences:

        1. permission on the assignee will be verified in this API.
        2. Hierarchy lookup (project->folder->organization) happens in this API.
        3. Parent here is ``projects/*/locations/*``, instead of
           ``projects/*/locations/*reservations/*``.

        **Note** "-" cannot be used for projects nor locations.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["reservation_service_stub"].SearchAssignments

    @property
    def move_assignment(self):
        """Return the gRPC stub for :meth:`ReservationServiceClient.move_assignment`.

        Moves an assignment under a new reservation.

        This differs from removing an existing assignment and recreating a new one
        by providing a transactional change that ensures an assignee always has an
        associated reservation.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["reservation_service_stub"].MoveAssignment

    @property
    def get_bi_reservation(self):
        """Return the gRPC stub for :meth:`ReservationServiceClient.get_bi_reservation`.

        Retrieves a BI reservation.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["reservation_service_stub"].GetBiReservation

    @property
    def update_bi_reservation(self):
        """Return the gRPC stub for :meth:`ReservationServiceClient.update_bi_reservation`.

        Updates a BI reservation.

        Only fields specified in the ``field_mask`` are updated.

        A singleton BI reservation always exists with default size 0. In order
        to reserve BI capacity it needs to be updated to an amount greater than
        0. In order to release BI capacity reservation size must be set to 0.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["reservation_service_stub"].UpdateBiReservation
