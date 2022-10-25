from dataclasses import dataclass, field


from source.crawler.page_rank_counter.models.page_rank import PageRank
from source.crawler.urls_validator.models.page_metadata import PageMetadata
from source.crawler.linked_pages_crawler.models.page_linked_urls import PageLinkedUrls


@dataclass
class ProcessEntity:
    url: str = field(default_factory=lambda: None)
    depth: int = field(default_factory=lambda: None)
    page_rank: PageRank = field(init=False)
    metadata: PageMetadata = field(init=False)
    page_linked_urls: PageLinkedUrls = field(init=False)