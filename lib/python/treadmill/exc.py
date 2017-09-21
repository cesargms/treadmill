"""Treadmill exceptions and utility functions."""

from __future__ import absolute_import

import logging

_LOGGER = logging.getLogger(__name__)


class TreadmillError(Exception):
    """Base class for all Treadmill errors"""

    def __str__(self):
        return self.message


class InvalidInputError(TreadmillError):
    """Non-fatal error, indicating incorrect input."""

    def __init__(self, source, msg):
        self.source = source
        self.message = msg
        super(InvalidInputError, self).__init__()


class ContainerSetupError(TreadmillError):
    """Fatal error, indicating problem setting up container environment."""

    def __init__(self, msg, reason=None):
        self.message = msg
        if reason is None:
            self.reason = 'unknown'
        else:
            self.reason = reason
        super(ContainerSetupError, self).__init__()


class NodeSetupError(TreadmillError):
    """Fatal error, indicating problem initializing the node environment"""
    pass


class FileNotFoundError(TreadmillError):
    """Thrown if the file cannot be found on the host."""
    pass


class NotFoundError(TreadmillError):
    """Thrown in REST API when a resource is not found"""
    pass


class FoundError(TreadmillError):
    """Thrown in REST API when a resource is found"""
    pass
