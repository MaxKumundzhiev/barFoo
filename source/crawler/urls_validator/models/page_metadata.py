from dataclasses import dataclass
from bs4 import BeautifulSoup


@dataclass
class PageMetadata:
    url: str
    html: BeautifulSoup
    path: str
    domain: str
    protocol: str