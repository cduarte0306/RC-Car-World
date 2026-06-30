"""Configuration dataclass skeletons for rc-sim."""

from dataclasses import dataclass


@dataclass
class CameraConfig:
    """Describe camera-related configuration values for the simulator."""

    pass


@dataclass
class VehicleConfig:
    """Describe vehicle-specific configuration values for a simulated car."""

    pass


@dataclass
class BridgeConfig:
    """Describe bridge-related configuration values for external integrations."""

    pass


@dataclass
class CarConfig:
    """Describe the configuration for an individual car in the fleet."""

    pass


@dataclass
class FleetConfig:
    """Describe configuration values for coordinating a fleet of cars."""

    pass


@dataclass
class SimConfig:
    """Describe top-level configuration values for an rc-sim session."""

    pass
