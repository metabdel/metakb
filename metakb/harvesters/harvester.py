"""Base module for all harvesters."""
from abc import ABC, abstractmethod


class Harvester(ABC):
    """Abstract base class for all harvester classes."""

    @abstractmethod
    def harvest_iter(self):
        """Collect all associations from the resource and yield as dict."""
