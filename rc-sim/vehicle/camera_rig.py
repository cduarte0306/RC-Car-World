"""Camera rig skeleton for rc-sim."""


class CameraRig:
    """Represent the camera capture interface attached to a vehicle."""

    def grab_frame(self):
        """Capture and return the latest frame from the camera rig."""
        raise NotImplementedError("TODO")
