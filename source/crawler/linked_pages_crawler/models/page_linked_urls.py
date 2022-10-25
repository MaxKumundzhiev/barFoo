from dataclasses import dataclass
from typing import List, Union


@dataclass
class PageLinkedUrls:
    url: str
    amount: int
    urls: Union[str, List[str]]