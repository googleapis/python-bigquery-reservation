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

"""Accesses the google.cloud.bigquery.reservation.v1 ReservationService API."""

import functools
import pkg_resources
import warnings

from google.oauth2 import service_account
import google.api_core.client_options
import google.api_core.gapic_v1.client_info
import google.api_core.gapic_v1.config
import google.api_core.gapic_v1.method
import google.api_core.gapic_v1.routing_header
import google.api_core.grpc_helpers
import google.api_core.page_iterator
import google.api_core.path_template
import grpc

from google.cloud.bigquery_reservation_v1.gapic import enums
from google.cloud.bigquery_reservation_v1.gapic import reservation_service_client_config
from google.cloud.bigquery_reservation_v1.gapic.transports import (
    reservation_service_grpc_transport,
)
from google.cloud.bigquery_reservation_v1.proto import reservation_pb2
from google.cloud.bigquery_reservation_v1.proto import reservation_pb2_grpc
from google.protobuf import empty_pb2
from google.protobuf import field_mask_pb2


_GAPIC_LIBRARY_VERSION = pkg_resources.get_distribution(
    "google-cloud-bigquery-reservation",
).version


class ReservationServiceClient(object):
    """
    This API allows users to manage their flat-rate BigQuery
    reservations.

    A reservation provides computational resource guarantees, in the form of
    `slots <https://cloud.google.com/bigquery/docs/slots>`__, to users. A
    slot is a unit of computational power in BigQuery, and serves as the
    basic unit of parallelism. In a scan of a multi-partitioned table, a
    single slot operates on a single partition of the table. A reservation
    resource exists as a child resource of the admin project and location,
    e.g.: ``projects/myproject/locations/US/reservations/reservationName``.

    A capacity commitment is a way to purchase compute capacity for BigQuery
    jobs (in the form of slots) with some committed period of usage. A
    capacity commitment resource exists as a child resource of the admin
    project and location, e.g.:
    ``projects/myproject/locations/US/capacityCommitments/id``.
    """

    SERVICE_ADDRESS = "bigqueryreservation.googleapis.com:443"
    """The default address of the service."""

    # The name of the interface for this client. This is the key used to
    # find the method configuration in the client_config dictionary.
    _INTERFACE_NAME = "google.cloud.bigquery.reservation.v1.ReservationService"

    @classmethod
    def from_service_account_file(cls, filename, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
        file.

        Args:
            filename (str): The path to the service account private key json
                file.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            ReservationServiceClient: The constructed client.
        """
        credentials = service_account.Credentials.from_service_account_file(filename)
        kwargs["credentials"] = credentials
        return cls(*args, **kwargs)

    from_service_account_json = from_service_account_file

    @classmethod
    def assignment_path(cls, project, location, reservation, assignment):
        """Return a fully-qualified assignment string."""
        return google.api_core.path_template.expand(
            "projects/{project}/locations/{location}/reservations/{reservation}/assignments/{assignment}",
            project=project,
            location=location,
            reservation=reservation,
            assignment=assignment,
        )

    @classmethod
    def bi_reservation_path(cls, project, location):
        """Return a fully-qualified bi_reservation string."""
        return google.api_core.path_template.expand(
            "projects/{project}/locations/{location}/bireservation",
            project=project,
            location=location,
        )

    @classmethod
    def capacity_commitment_path(cls, project, location, capacity_commitment):
        """Return a fully-qualified capacity_commitment string."""
        return google.api_core.path_template.expand(
            "projects/{project}/locations/{location}/capacityCommitments/{capacity_commitment}",
            project=project,
            location=location,
            capacity_commitment=capacity_commitment,
        )

    @classmethod
    def location_path(cls, project, location):
        """Return a fully-qualified location string."""
        return google.api_core.path_template.expand(
            "projects/{project}/locations/{location}",
            project=project,
            location=location,
        )

    @classmethod
    def reservation_path(cls, project, location, reservation):
        """Return a fully-qualified reservation string."""
        return google.api_core.path_template.expand(
            "projects/{project}/locations/{location}/reservations/{reservation}",
            project=project,
            location=location,
            reservation=reservation,
        )

    def __init__(
        self,
        transport=None,
        channel=None,
        credentials=None,
        client_config=None,
        client_info=None,
        client_options=None,
    ):
        """Constructor.

        Args:
            transport (Union[~.ReservationServiceGrpcTransport,
                    Callable[[~.Credentials, type], ~.ReservationServiceGrpcTransport]): A transport
                instance, responsible for actually making the API calls.
                The default transport uses the gRPC protocol.
                This argument may also be a callable which returns a
                transport instance. Callables will be sent the credentials
                as the first argument and the default transport class as
                the second argument.
            channel (grpc.Channel): DEPRECATED. A ``Channel`` instance
                through which to make calls. This argument is mutually exclusive
                with ``credentials``; providing both will raise an exception.
            credentials (google.auth.credentials.Credentials): The
                authorization credentials to attach to requests. These
                credentials identify this application to the service. If none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
                This argument is mutually exclusive with providing a
                transport instance to ``transport``; doing so will raise
                an exception.
            client_config (dict): DEPRECATED. A dictionary of call options for
                each method. If not specified, the default configuration is used.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.
            client_options (Union[dict, google.api_core.client_options.ClientOptions]):
                Client options used to set user options on the client. API Endpoint
                should be set through client_options.
        """
        # Raise deprecation warnings for things we want to go away.
        if client_config is not None:
            warnings.warn(
                "The `client_config` argument is deprecated.",
                PendingDeprecationWarning,
                stacklevel=2,
            )
        else:
            client_config = reservation_service_client_config.config

        if channel:
            warnings.warn(
                "The `channel` argument is deprecated; use " "`transport` instead.",
                PendingDeprecationWarning,
                stacklevel=2,
            )

        api_endpoint = self.SERVICE_ADDRESS
        if client_options:
            if type(client_options) == dict:
                client_options = google.api_core.client_options.from_dict(
                    client_options
                )
            if client_options.api_endpoint:
                api_endpoint = client_options.api_endpoint

        # Instantiate the transport.
        # The transport is responsible for handling serialization and
        # deserialization and actually sending data to the service.
        if transport:
            if callable(transport):
                self.transport = transport(
                    credentials=credentials,
                    default_class=reservation_service_grpc_transport.ReservationServiceGrpcTransport,
                    address=api_endpoint,
                )
            else:
                if credentials:
                    raise ValueError(
                        "Received both a transport instance and "
                        "credentials; these are mutually exclusive."
                    )
                self.transport = transport
        else:
            self.transport = reservation_service_grpc_transport.ReservationServiceGrpcTransport(
                address=api_endpoint, channel=channel, credentials=credentials,
            )

        if client_info is None:
            client_info = google.api_core.gapic_v1.client_info.ClientInfo(
                gapic_version=_GAPIC_LIBRARY_VERSION,
            )
        else:
            client_info.gapic_version = _GAPIC_LIBRARY_VERSION
        self._client_info = client_info

        # Parse out the default settings for retry and timeout for each RPC
        # from the client configuration.
        # (Ordinarily, these are the defaults specified in the `*_config.py`
        # file next to this one.)
        self._method_configs = google.api_core.gapic_v1.config.parse_method_configs(
            client_config["interfaces"][self._INTERFACE_NAME],
        )

        # Save a dictionary of cached API call functions.
        # These are the actual callables which invoke the proper
        # transport methods, wrapped with `wrap_method` to add retry,
        # timeout, and the like.
        self._inner_api_calls = {}

    # Service calls
    def create_reservation(
        self,
        parent,
        reservation_id=None,
        reservation=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Creates a new reservation resource.

        Example:
            >>> from google.cloud import bigquery_reservation_v1
            >>>
            >>> client = bigquery_reservation_v1.ReservationServiceClient()
            >>>
            >>> parent = client.location_path('[PROJECT]', '[LOCATION]')
            >>>
            >>> response = client.create_reservation(parent)

        Args:
            parent (str): Required. Project, location. E.g.,
                ``projects/myproject/locations/US``
            reservation_id (str): The reservation ID. This field must only contain lower case alphanumeric
                characters or dash. Max length is 64 characters.
            reservation (Union[dict, ~google.cloud.bigquery_reservation_v1.types.Reservation]): Definition of the new reservation to create.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.bigquery_reservation_v1.types.Reservation`
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.bigquery_reservation_v1.types.Reservation` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "create_reservation" not in self._inner_api_calls:
            self._inner_api_calls[
                "create_reservation"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.create_reservation,
                default_retry=self._method_configs["CreateReservation"].retry,
                default_timeout=self._method_configs["CreateReservation"].timeout,
                client_info=self._client_info,
            )

        request = reservation_pb2.CreateReservationRequest(
            parent=parent, reservation_id=reservation_id, reservation=reservation,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("parent", parent)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["create_reservation"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def list_reservations(
        self,
        parent,
        page_size=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Lists all the reservations for the project in the specified location.

        Example:
            >>> from google.cloud import bigquery_reservation_v1
            >>>
            >>> client = bigquery_reservation_v1.ReservationServiceClient()
            >>>
            >>> parent = client.location_path('[PROJECT]', '[LOCATION]')
            >>>
            >>> # Iterate over all results
            >>> for element in client.list_reservations(parent):
            ...     # process element
            ...     pass
            >>>
            >>>
            >>> # Alternatively:
            >>>
            >>> # Iterate over results one page at a time
            >>> for page in client.list_reservations(parent).pages:
            ...     for element in page:
            ...         # process element
            ...         pass

        Args:
            parent (str): Required. The parent resource name containing project and location,
                e.g.: ``projects/myproject/locations/US``
            page_size (int): The maximum number of resources contained in the
                underlying API response. If page streaming is performed per-
                resource, this parameter does not affect the return value. If page
                streaming is performed per-page, this determines the maximum number
                of resources in a page.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.api_core.page_iterator.PageIterator` instance.
            An iterable of :class:`~google.cloud.bigquery_reservation_v1.types.Reservation` instances.
            You can also iterate over the pages of the response
            using its `pages` property.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "list_reservations" not in self._inner_api_calls:
            self._inner_api_calls[
                "list_reservations"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.list_reservations,
                default_retry=self._method_configs["ListReservations"].retry,
                default_timeout=self._method_configs["ListReservations"].timeout,
                client_info=self._client_info,
            )

        request = reservation_pb2.ListReservationsRequest(
            parent=parent, page_size=page_size,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("parent", parent)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        iterator = google.api_core.page_iterator.GRPCIterator(
            client=None,
            method=functools.partial(
                self._inner_api_calls["list_reservations"],
                retry=retry,
                timeout=timeout,
                metadata=metadata,
            ),
            request=request,
            items_field="reservations",
            request_token_field="page_token",
            response_token_field="next_page_token",
        )
        return iterator

    def get_reservation(
        self,
        name,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Returns information about the reservation.

        Example:
            >>> from google.cloud import bigquery_reservation_v1
            >>>
            >>> client = bigquery_reservation_v1.ReservationServiceClient()
            >>>
            >>> name = client.reservation_path('[PROJECT]', '[LOCATION]', '[RESERVATION]')
            >>>
            >>> response = client.get_reservation(name)

        Args:
            name (str): Required. Resource name of the reservation to retrieve. E.g.,
                ``projects/myproject/locations/US/reservations/team1-prod``
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.bigquery_reservation_v1.types.Reservation` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "get_reservation" not in self._inner_api_calls:
            self._inner_api_calls[
                "get_reservation"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.get_reservation,
                default_retry=self._method_configs["GetReservation"].retry,
                default_timeout=self._method_configs["GetReservation"].timeout,
                client_info=self._client_info,
            )

        request = reservation_pb2.GetReservationRequest(name=name,)
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("name", name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["get_reservation"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def delete_reservation(
        self,
        name,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Deletes a reservation. Returns
        ``google.rpc.Code.FAILED_PRECONDITION`` when reservation has
        assignments.

        Example:
            >>> from google.cloud import bigquery_reservation_v1
            >>>
            >>> client = bigquery_reservation_v1.ReservationServiceClient()
            >>>
            >>> name = client.reservation_path('[PROJECT]', '[LOCATION]', '[RESERVATION]')
            >>>
            >>> client.delete_reservation(name)

        Args:
            name (str): Required. Resource name of the reservation to retrieve. E.g.,
                ``projects/myproject/locations/US/reservations/team1-prod``
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "delete_reservation" not in self._inner_api_calls:
            self._inner_api_calls[
                "delete_reservation"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.delete_reservation,
                default_retry=self._method_configs["DeleteReservation"].retry,
                default_timeout=self._method_configs["DeleteReservation"].timeout,
                client_info=self._client_info,
            )

        request = reservation_pb2.DeleteReservationRequest(name=name,)
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("name", name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        self._inner_api_calls["delete_reservation"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def update_reservation(
        self,
        reservation=None,
        update_mask=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Updates an existing reservation resource.

        Example:
            >>> from google.cloud import bigquery_reservation_v1
            >>>
            >>> client = bigquery_reservation_v1.ReservationServiceClient()
            >>>
            >>> response = client.update_reservation()

        Args:
            reservation (Union[dict, ~google.cloud.bigquery_reservation_v1.types.Reservation]): Content of the reservation to update.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.bigquery_reservation_v1.types.Reservation`
            update_mask (Union[dict, ~google.cloud.bigquery_reservation_v1.types.FieldMask]): Standard field mask for the set of fields to be updated.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.bigquery_reservation_v1.types.FieldMask`
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.bigquery_reservation_v1.types.Reservation` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "update_reservation" not in self._inner_api_calls:
            self._inner_api_calls[
                "update_reservation"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.update_reservation,
                default_retry=self._method_configs["UpdateReservation"].retry,
                default_timeout=self._method_configs["UpdateReservation"].timeout,
                client_info=self._client_info,
            )

        request = reservation_pb2.UpdateReservationRequest(
            reservation=reservation, update_mask=update_mask,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("reservation.name", reservation.name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["update_reservation"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def create_capacity_commitment(
        self,
        parent,
        capacity_commitment=None,
        enforce_single_admin_project_per_org=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Creates a new capacity commitment resource.

        Example:
            >>> from google.cloud import bigquery_reservation_v1
            >>>
            >>> client = bigquery_reservation_v1.ReservationServiceClient()
            >>>
            >>> parent = client.location_path('[PROJECT]', '[LOCATION]')
            >>>
            >>> response = client.create_capacity_commitment(parent)

        Args:
            parent (str): Required. Resource name of the parent reservation. E.g.,
                ``projects/myproject/locations/US``
            capacity_commitment (Union[dict, ~google.cloud.bigquery_reservation_v1.types.CapacityCommitment]): Content of the capacity commitment to create.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.bigquery_reservation_v1.types.CapacityCommitment`
            enforce_single_admin_project_per_org (bool): If true, fail the request if another project in the organization has a
                capacity commitment.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.bigquery_reservation_v1.types.CapacityCommitment` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "create_capacity_commitment" not in self._inner_api_calls:
            self._inner_api_calls[
                "create_capacity_commitment"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.create_capacity_commitment,
                default_retry=self._method_configs["CreateCapacityCommitment"].retry,
                default_timeout=self._method_configs[
                    "CreateCapacityCommitment"
                ].timeout,
                client_info=self._client_info,
            )

        request = reservation_pb2.CreateCapacityCommitmentRequest(
            parent=parent,
            capacity_commitment=capacity_commitment,
            enforce_single_admin_project_per_org=enforce_single_admin_project_per_org,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("parent", parent)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["create_capacity_commitment"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def list_capacity_commitments(
        self,
        parent,
        page_size=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Lists all the capacity commitments for the admin project.

        Example:
            >>> from google.cloud import bigquery_reservation_v1
            >>>
            >>> client = bigquery_reservation_v1.ReservationServiceClient()
            >>>
            >>> parent = client.location_path('[PROJECT]', '[LOCATION]')
            >>>
            >>> # Iterate over all results
            >>> for element in client.list_capacity_commitments(parent):
            ...     # process element
            ...     pass
            >>>
            >>>
            >>> # Alternatively:
            >>>
            >>> # Iterate over results one page at a time
            >>> for page in client.list_capacity_commitments(parent).pages:
            ...     for element in page:
            ...         # process element
            ...         pass

        Args:
            parent (str): Required. Resource name of the parent reservation. E.g.,
                ``projects/myproject/locations/US``
            page_size (int): The maximum number of resources contained in the
                underlying API response. If page streaming is performed per-
                resource, this parameter does not affect the return value. If page
                streaming is performed per-page, this determines the maximum number
                of resources in a page.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.api_core.page_iterator.PageIterator` instance.
            An iterable of :class:`~google.cloud.bigquery_reservation_v1.types.CapacityCommitment` instances.
            You can also iterate over the pages of the response
            using its `pages` property.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "list_capacity_commitments" not in self._inner_api_calls:
            self._inner_api_calls[
                "list_capacity_commitments"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.list_capacity_commitments,
                default_retry=self._method_configs["ListCapacityCommitments"].retry,
                default_timeout=self._method_configs["ListCapacityCommitments"].timeout,
                client_info=self._client_info,
            )

        request = reservation_pb2.ListCapacityCommitmentsRequest(
            parent=parent, page_size=page_size,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("parent", parent)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        iterator = google.api_core.page_iterator.GRPCIterator(
            client=None,
            method=functools.partial(
                self._inner_api_calls["list_capacity_commitments"],
                retry=retry,
                timeout=timeout,
                metadata=metadata,
            ),
            request=request,
            items_field="capacity_commitments",
            request_token_field="page_token",
            response_token_field="next_page_token",
        )
        return iterator

    def get_capacity_commitment(
        self,
        name,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Returns information about the capacity commitment.

        Example:
            >>> from google.cloud import bigquery_reservation_v1
            >>>
            >>> client = bigquery_reservation_v1.ReservationServiceClient()
            >>>
            >>> name = client.capacity_commitment_path('[PROJECT]', '[LOCATION]', '[CAPACITY_COMMITMENT]')
            >>>
            >>> response = client.get_capacity_commitment(name)

        Args:
            name (str): Required. Resource name of the capacity commitment to retrieve.
                E.g., ``projects/myproject/locations/US/capacityCommitments/123``
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.bigquery_reservation_v1.types.CapacityCommitment` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "get_capacity_commitment" not in self._inner_api_calls:
            self._inner_api_calls[
                "get_capacity_commitment"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.get_capacity_commitment,
                default_retry=self._method_configs["GetCapacityCommitment"].retry,
                default_timeout=self._method_configs["GetCapacityCommitment"].timeout,
                client_info=self._client_info,
            )

        request = reservation_pb2.GetCapacityCommitmentRequest(name=name,)
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("name", name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["get_capacity_commitment"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def delete_capacity_commitment(
        self,
        name,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Deletes a capacity commitment. Attempting to delete capacity
        commitment before its commitment_end_time will fail with the error code
        ``google.rpc.Code.FAILED_PRECONDITION``.

        Example:
            >>> from google.cloud import bigquery_reservation_v1
            >>>
            >>> client = bigquery_reservation_v1.ReservationServiceClient()
            >>>
            >>> name = client.capacity_commitment_path('[PROJECT]', '[LOCATION]', '[CAPACITY_COMMITMENT]')
            >>>
            >>> client.delete_capacity_commitment(name)

        Args:
            name (str): Required. Resource name of the capacity commitment to delete. E.g.,
                ``projects/myproject/locations/US/capacityCommitments/123``
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "delete_capacity_commitment" not in self._inner_api_calls:
            self._inner_api_calls[
                "delete_capacity_commitment"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.delete_capacity_commitment,
                default_retry=self._method_configs["DeleteCapacityCommitment"].retry,
                default_timeout=self._method_configs[
                    "DeleteCapacityCommitment"
                ].timeout,
                client_info=self._client_info,
            )

        request = reservation_pb2.DeleteCapacityCommitmentRequest(name=name,)
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("name", name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        self._inner_api_calls["delete_capacity_commitment"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def update_capacity_commitment(
        self,
        capacity_commitment=None,
        update_mask=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Updates an existing capacity commitment.

        Only ``plan`` and ``renewal_plan`` fields can be updated.

        Plan can only be changed to a plan of a longer commitment period.
        Attempting to change to a plan with shorter commitment period will fail
        with the error code ``google.rpc.Code.FAILED_PRECONDITION``.

        Example:
            >>> from google.cloud import bigquery_reservation_v1
            >>>
            >>> client = bigquery_reservation_v1.ReservationServiceClient()
            >>>
            >>> response = client.update_capacity_commitment()

        Args:
            capacity_commitment (Union[dict, ~google.cloud.bigquery_reservation_v1.types.CapacityCommitment]): Content of the capacity commitment to update.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.bigquery_reservation_v1.types.CapacityCommitment`
            update_mask (Union[dict, ~google.cloud.bigquery_reservation_v1.types.FieldMask]): Standard field mask for the set of fields to be updated.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.bigquery_reservation_v1.types.FieldMask`
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.bigquery_reservation_v1.types.CapacityCommitment` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "update_capacity_commitment" not in self._inner_api_calls:
            self._inner_api_calls[
                "update_capacity_commitment"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.update_capacity_commitment,
                default_retry=self._method_configs["UpdateCapacityCommitment"].retry,
                default_timeout=self._method_configs[
                    "UpdateCapacityCommitment"
                ].timeout,
                client_info=self._client_info,
            )

        request = reservation_pb2.UpdateCapacityCommitmentRequest(
            capacity_commitment=capacity_commitment, update_mask=update_mask,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("capacity_commitment.name", capacity_commitment.name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["update_capacity_commitment"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def split_capacity_commitment(
        self,
        name,
        slot_count=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Splits capacity commitment to two commitments of the same plan and
        ``commitment_end_time``.

        A common use case is to enable downgrading commitments.

        For example, in order to downgrade from 10000 slots to 8000, you might
        split a 10000 capacity commitment into commitments of 2000 and 8000.
        Then, you would change the plan of the first one to ``FLEX`` and then
        delete it.

        Example:
            >>> from google.cloud import bigquery_reservation_v1
            >>>
            >>> client = bigquery_reservation_v1.ReservationServiceClient()
            >>>
            >>> name = client.capacity_commitment_path('[PROJECT]', '[LOCATION]', '[CAPACITY_COMMITMENT]')
            >>>
            >>> response = client.split_capacity_commitment(name)

        Args:
            name (str): Required. The resource name e.g.,:
                ``projects/myproject/locations/US/capacityCommitments/123``
            slot_count (long): Number of slots in the capacity commitment after the split.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.bigquery_reservation_v1.types.SplitCapacityCommitmentResponse` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "split_capacity_commitment" not in self._inner_api_calls:
            self._inner_api_calls[
                "split_capacity_commitment"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.split_capacity_commitment,
                default_retry=self._method_configs["SplitCapacityCommitment"].retry,
                default_timeout=self._method_configs["SplitCapacityCommitment"].timeout,
                client_info=self._client_info,
            )

        request = reservation_pb2.SplitCapacityCommitmentRequest(
            name=name, slot_count=slot_count,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("name", name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["split_capacity_commitment"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def merge_capacity_commitments(
        self,
        parent=None,
        capacity_commitment_ids=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Merges capacity commitments of the same plan into a single
        commitment.

        The resulting capacity commitment has the greater commitment_end_time
        out of the to-be-merged capacity commitments.

        Attempting to merge capacity commitments of different plan will fail
        with the error code ``google.rpc.Code.FAILED_PRECONDITION``.

        Example:
            >>> from google.cloud import bigquery_reservation_v1
            >>>
            >>> client = bigquery_reservation_v1.ReservationServiceClient()
            >>>
            >>> response = client.merge_capacity_commitments()

        Args:
            parent (str): Parent resource that identifies admin project and location e.g.,
                ``projects/myproject/locations/us``
            capacity_commitment_ids (list[str]): Ids of capacity commitments to merge.
                These capacity commitments must exist under admin project and location
                specified in the parent.
                ID is the last portion of capacity commitment name e.g., 'abc' for
                projects/myproject/locations/US/capacityCommitments/abc
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.bigquery_reservation_v1.types.CapacityCommitment` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "merge_capacity_commitments" not in self._inner_api_calls:
            self._inner_api_calls[
                "merge_capacity_commitments"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.merge_capacity_commitments,
                default_retry=self._method_configs["MergeCapacityCommitments"].retry,
                default_timeout=self._method_configs[
                    "MergeCapacityCommitments"
                ].timeout,
                client_info=self._client_info,
            )

        request = reservation_pb2.MergeCapacityCommitmentsRequest(
            parent=parent, capacity_commitment_ids=capacity_commitment_ids,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("parent", parent)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["merge_capacity_commitments"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def create_assignment(
        self,
        parent,
        assignment=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
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

        Example:
            >>> from google.cloud import bigquery_reservation_v1
            >>>
            >>> client = bigquery_reservation_v1.ReservationServiceClient()
            >>>
            >>> parent = client.reservation_path('[PROJECT]', '[LOCATION]', '[RESERVATION]')
            >>>
            >>> response = client.create_assignment(parent)

        Args:
            parent (str): Required. The parent resource name of the assignment E.g.
                ``projects/myproject/locations/US/reservations/team1-prod``
            assignment (Union[dict, ~google.cloud.bigquery_reservation_v1.types.Assignment]): Assignment resource to create.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.bigquery_reservation_v1.types.Assignment`
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.bigquery_reservation_v1.types.Assignment` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "create_assignment" not in self._inner_api_calls:
            self._inner_api_calls[
                "create_assignment"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.create_assignment,
                default_retry=self._method_configs["CreateAssignment"].retry,
                default_timeout=self._method_configs["CreateAssignment"].timeout,
                client_info=self._client_info,
            )

        request = reservation_pb2.CreateAssignmentRequest(
            parent=parent, assignment=assignment,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("parent", parent)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["create_assignment"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def list_assignments(
        self,
        parent,
        page_size=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
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

        Example:
            >>> from google.cloud import bigquery_reservation_v1
            >>>
            >>> client = bigquery_reservation_v1.ReservationServiceClient()
            >>>
            >>> parent = client.reservation_path('[PROJECT]', '[LOCATION]', '[RESERVATION]')
            >>>
            >>> # Iterate over all results
            >>> for element in client.list_assignments(parent):
            ...     # process element
            ...     pass
            >>>
            >>>
            >>> # Alternatively:
            >>>
            >>> # Iterate over results one page at a time
            >>> for page in client.list_assignments(parent).pages:
            ...     for element in page:
            ...         # process element
            ...         pass

        Args:
            parent (str): Required. The parent resource name e.g.:

                ``projects/myproject/locations/US/reservations/team1-prod``

                Or:

                ``projects/myproject/locations/US/reservations/-``
            page_size (int): The maximum number of resources contained in the
                underlying API response. If page streaming is performed per-
                resource, this parameter does not affect the return value. If page
                streaming is performed per-page, this determines the maximum number
                of resources in a page.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.api_core.page_iterator.PageIterator` instance.
            An iterable of :class:`~google.cloud.bigquery_reservation_v1.types.Assignment` instances.
            You can also iterate over the pages of the response
            using its `pages` property.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "list_assignments" not in self._inner_api_calls:
            self._inner_api_calls[
                "list_assignments"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.list_assignments,
                default_retry=self._method_configs["ListAssignments"].retry,
                default_timeout=self._method_configs["ListAssignments"].timeout,
                client_info=self._client_info,
            )

        request = reservation_pb2.ListAssignmentsRequest(
            parent=parent, page_size=page_size,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("parent", parent)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        iterator = google.api_core.page_iterator.GRPCIterator(
            client=None,
            method=functools.partial(
                self._inner_api_calls["list_assignments"],
                retry=retry,
                timeout=timeout,
                metadata=metadata,
            ),
            request=request,
            items_field="assignments",
            request_token_field="page_token",
            response_token_field="next_page_token",
        )
        return iterator

    def delete_assignment(
        self,
        name,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
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

        Example:
            >>> from google.cloud import bigquery_reservation_v1
            >>>
            >>> client = bigquery_reservation_v1.ReservationServiceClient()
            >>>
            >>> name = client.assignment_path('[PROJECT]', '[LOCATION]', '[RESERVATION]', '[ASSIGNMENT]')
            >>>
            >>> client.delete_assignment(name)

        Args:
            name (str): Required. Name of the resource, e.g.
                ``projects/myproject/locations/US/reservations/team1-prod/assignments/123``
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "delete_assignment" not in self._inner_api_calls:
            self._inner_api_calls[
                "delete_assignment"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.delete_assignment,
                default_retry=self._method_configs["DeleteAssignment"].retry,
                default_timeout=self._method_configs["DeleteAssignment"].timeout,
                client_info=self._client_info,
            )

        request = reservation_pb2.DeleteAssignmentRequest(name=name,)
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("name", name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        self._inner_api_calls["delete_assignment"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def search_assignments(
        self,
        parent,
        query=None,
        page_size=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
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

        Example:
            >>> from google.cloud import bigquery_reservation_v1
            >>>
            >>> client = bigquery_reservation_v1.ReservationServiceClient()
            >>>
            >>> parent = client.location_path('[PROJECT]', '[LOCATION]')
            >>>
            >>> # Iterate over all results
            >>> for element in client.search_assignments(parent):
            ...     # process element
            ...     pass
            >>>
            >>>
            >>> # Alternatively:
            >>>
            >>> # Iterate over results one page at a time
            >>> for page in client.search_assignments(parent).pages:
            ...     for element in page:
            ...         # process element
            ...         pass

        Args:
            parent (str): Required. The resource name of the admin project(containing project
                and location), e.g.: ``projects/myproject/locations/US``.
            query (str): Please specify resource name as assignee in the query.

                Examples:

                -  ``assignee=projects/myproject``
                -  ``assignee=folders/123``
                -  ``assignee=organizations/456``
            page_size (int): The maximum number of resources contained in the
                underlying API response. If page streaming is performed per-
                resource, this parameter does not affect the return value. If page
                streaming is performed per-page, this determines the maximum number
                of resources in a page.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.api_core.page_iterator.PageIterator` instance.
            An iterable of :class:`~google.cloud.bigquery_reservation_v1.types.Assignment` instances.
            You can also iterate over the pages of the response
            using its `pages` property.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "search_assignments" not in self._inner_api_calls:
            self._inner_api_calls[
                "search_assignments"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.search_assignments,
                default_retry=self._method_configs["SearchAssignments"].retry,
                default_timeout=self._method_configs["SearchAssignments"].timeout,
                client_info=self._client_info,
            )

        request = reservation_pb2.SearchAssignmentsRequest(
            parent=parent, query=query, page_size=page_size,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("parent", parent)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        iterator = google.api_core.page_iterator.GRPCIterator(
            client=None,
            method=functools.partial(
                self._inner_api_calls["search_assignments"],
                retry=retry,
                timeout=timeout,
                metadata=metadata,
            ),
            request=request,
            items_field="assignments",
            request_token_field="page_token",
            response_token_field="next_page_token",
        )
        return iterator

    def move_assignment(
        self,
        name,
        destination_id=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Moves an assignment under a new reservation.

        This differs from removing an existing assignment and recreating a new one
        by providing a transactional change that ensures an assignee always has an
        associated reservation.

        Example:
            >>> from google.cloud import bigquery_reservation_v1
            >>>
            >>> client = bigquery_reservation_v1.ReservationServiceClient()
            >>>
            >>> name = client.assignment_path('[PROJECT]', '[LOCATION]', '[RESERVATION]', '[ASSIGNMENT]')
            >>>
            >>> response = client.move_assignment(name)

        Args:
            name (str): Required. The resource name of the assignment, e.g.
                ``projects/myproject/locations/US/reservations/team1-prod/assignments/123``
            destination_id (str): The new reservation ID, e.g.:
                ``projects/myotherproject/locations/US/reservations/team2-prod``
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.bigquery_reservation_v1.types.Assignment` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "move_assignment" not in self._inner_api_calls:
            self._inner_api_calls[
                "move_assignment"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.move_assignment,
                default_retry=self._method_configs["MoveAssignment"].retry,
                default_timeout=self._method_configs["MoveAssignment"].timeout,
                client_info=self._client_info,
            )

        request = reservation_pb2.MoveAssignmentRequest(
            name=name, destination_id=destination_id,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("name", name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["move_assignment"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def get_bi_reservation(
        self,
        name,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Retrieves a BI reservation.

        Example:
            >>> from google.cloud import bigquery_reservation_v1
            >>>
            >>> client = bigquery_reservation_v1.ReservationServiceClient()
            >>>
            >>> name = client.bi_reservation_path('[PROJECT]', '[LOCATION]')
            >>>
            >>> response = client.get_bi_reservation(name)

        Args:
            name (str): Required. Name of the requested reservation, for example:
                ``projects/{project_id}/locations/{location_id}/bireservation``
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.bigquery_reservation_v1.types.BiReservation` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "get_bi_reservation" not in self._inner_api_calls:
            self._inner_api_calls[
                "get_bi_reservation"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.get_bi_reservation,
                default_retry=self._method_configs["GetBiReservation"].retry,
                default_timeout=self._method_configs["GetBiReservation"].timeout,
                client_info=self._client_info,
            )

        request = reservation_pb2.GetBiReservationRequest(name=name,)
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("name", name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["get_bi_reservation"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def update_bi_reservation(
        self,
        bi_reservation=None,
        update_mask=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Updates a BI reservation.

        Only fields specified in the ``field_mask`` are updated.

        A singleton BI reservation always exists with default size 0. In order
        to reserve BI capacity it needs to be updated to an amount greater than
        0. In order to release BI capacity reservation size must be set to 0.

        Example:
            >>> from google.cloud import bigquery_reservation_v1
            >>>
            >>> client = bigquery_reservation_v1.ReservationServiceClient()
            >>>
            >>> response = client.update_bi_reservation()

        Args:
            bi_reservation (Union[dict, ~google.cloud.bigquery_reservation_v1.types.BiReservation]): A reservation to update.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.bigquery_reservation_v1.types.BiReservation`
            update_mask (Union[dict, ~google.cloud.bigquery_reservation_v1.types.FieldMask]): A list of fields to be updated in this request.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.bigquery_reservation_v1.types.FieldMask`
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.bigquery_reservation_v1.types.BiReservation` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "update_bi_reservation" not in self._inner_api_calls:
            self._inner_api_calls[
                "update_bi_reservation"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.update_bi_reservation,
                default_retry=self._method_configs["UpdateBiReservation"].retry,
                default_timeout=self._method_configs["UpdateBiReservation"].timeout,
                client_info=self._client_info,
            )

        request = reservation_pb2.UpdateBiReservationRequest(
            bi_reservation=bi_reservation, update_mask=update_mask,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("bi_reservation.name", bi_reservation.name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["update_bi_reservation"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )
