from App.models.review import Review
from App.models import vCommand
from dataclasses import dataclass, field
from abc import ABC, abstractmethod

@dataclass

class voteController:

    undo_stack : list [vCommand] = field (default_factory = list)
    redo_stack : list [vCommand] = field (default_factory = list)


    def execute(self, vote: vCommand) -> None:
        vote.execute()

    def undo(self) -> None:
        if not self.undo_stack:
            return
        vote = self.undo_stack.pop()
        vote.undo()
        self.redo_stack.append(vote)

    def redo(self) -> None:
        if not self.redo_stack:
            return
        vote = self.redo_stack.pop()
        vote.execute()
        self.undo_stack.append(vote)
