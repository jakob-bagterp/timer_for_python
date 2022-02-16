from abc import ABC, abstractmethod
from .thread_item import ThreadItem
from .. import constants, helper
from ..model.thread_item import ThreadItem

class TimerObject(ABC):
    """Abstract base class of Timer object."""

    def __init__(self, decimals: int = constants.decimals.default()) -> None:    
        """Initiates basic properties of the Timer."""

        self.threads: list[ThreadItem] = []
        self.decimals: int = decimals if decimals == constants.decimals.default() else helper.decimals.validate_and_normalise(decimals)

    @abstractmethod
    def start(self, thread: str, decimals: int) -> None:
        """Starts the Timer."""

        raise NotImplementedError
    
    @abstractmethod
    def stop(self, thread: str) -> None:
        """Stops the Timer."""

        raise NotImplementedError
