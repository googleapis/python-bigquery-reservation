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

"""Wrappers for protocol buffer enum types."""

import enum


class Assignment(object):
    class JobType(enum.IntEnum):
        """
        Types of job, which could be specified when using the reservation.

        Attributes:
          JOB_TYPE_UNSPECIFIED (int): Invalid type. Requests with this value will be rejected with error
          code ``google.rpc.Code.INVALID_ARGUMENT``.
          PIPELINE (int): Pipeline (load/export) jobs from the project will use the reservation.
          QUERY (int): Query jobs from the project will use the reservation.
        """

        JOB_TYPE_UNSPECIFIED = 0
        PIPELINE = 1
        QUERY = 2

    class State(enum.IntEnum):
        """
        Assignment will remain in PENDING state if no active capacity commitment is
        present. It will become ACTIVE when some capacity commitment becomes
        active.

        Attributes:
          STATE_UNSPECIFIED (int): Invalid state value.
          PENDING (int): Queries from assignee will be executed as on-demand, if related
          assignment is pending.
          ACTIVE (int): Assignment is ready.
        """

        STATE_UNSPECIFIED = 0
        PENDING = 1
        ACTIVE = 2


class CapacityCommitment(object):
    class CommitmentPlan(enum.IntEnum):
        """
        Commitment plan defines the current committed period. Capacity commitment
        cannot be deleted during it's committed period.

        Attributes:
          COMMITMENT_PLAN_UNSPECIFIED (int): Invalid plan value. Requests with this value will be rejected with
          error code ``google.rpc.Code.INVALID_ARGUMENT``.
          FLEX (int): Flex commitments have committed period of 1 minute after becoming ACTIVE.
          After that, they are not in a committed period anymore and can be removed
          any time.
          TRIAL (int): Trial commitments have a committed period of 182 days after becoming
          ACTIVE. After that, they are converted to a new commitment based on the
          ``renewal_plan``. Default ``renewal_plan`` for Trial commitment is Flex
          so that it can be deleted right after committed period ends.
          MONTHLY (int): Monthly commitments have a committed period of 30 days after becoming
          ACTIVE. After that, they are not in a committed period anymore and can be
          removed any time.
          ANNUAL (int): Annual commitments have a committed period of 365 days after
          becoming ACTIVE. After that they are converted to a new commitment based
          on the renewal_plan.
        """

        COMMITMENT_PLAN_UNSPECIFIED = 0
        FLEX = 3
        TRIAL = 5
        MONTHLY = 2
        ANNUAL = 4

    class State(enum.IntEnum):
        """
        Capacity commitment can either become ACTIVE right away or transition
        from PENDING to ACTIVE or FAILED.

        Attributes:
          STATE_UNSPECIFIED (int): Invalid state value.
          PENDING (int): Capacity commitment is pending provisioning. Pending capacity
          commitment does not contribute to the parent's slot_capacity.
          ACTIVE (int): Once slots are provisioned, capacity commitment becomes active.
          slot_count is added to the parent's slot_capacity.
          FAILED (int): Capacity commitment is failed to be activated by the backend.
        """

        STATE_UNSPECIFIED = 0
        PENDING = 1
        ACTIVE = 2
        FAILED = 3
