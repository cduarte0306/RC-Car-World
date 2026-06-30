"""RC car interface skeleton for rc-sim."""


class RCCar:
    """Represent the interface of a simulated RC car."""

    def step(self, dt: float) -> None:
        """Advance the car state by one simulation time step.

        Args:
            dt: Duration of the simulation step in seconds.
        """
        raise NotImplementedError("TODO")

    @property
    def pose(self):
        """Return the current pose of the simulated car."""
        raise NotImplementedError("TODO")

    def reset(self) -> None:
        """Reset the car state to its initial simulation conditions."""
        raise NotImplementedError("TODO")
