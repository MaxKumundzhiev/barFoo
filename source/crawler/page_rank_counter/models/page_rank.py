from dataclasses import dataclass


@dataclass
class PageRank:
    url: str
    value: float