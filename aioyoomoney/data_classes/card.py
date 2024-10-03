from dataclasses import dataclass


@dataclass
class Card:
    pan_fragment: str | None
    type: str | None

