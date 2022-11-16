from abc import ABC, abstractmethod

class vCommand(ABC):

    @abstractmethod
    def execute(self) -> None:
        """execute method"""

    @abstractmethod
    def undo(self) -> None:
        """undo method"""

    @abstractmethod
    def redo(self) -> None:
        """redo method"""   

        