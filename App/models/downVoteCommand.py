from App.models.review import Review
from dataclasses import dataclass, field

@dataclass

class downVote:
    review: Review
    vote: str

    def execute(self) -> str:
        return f"${self.vote} to review {self.review.vote}"
    
    def undo(self) -> None:
        return f"${self.review.vote} to review {self.review.vote}"

    def redo(self) -> None:
        return f"${self.vote} to review {self.review.vote}"