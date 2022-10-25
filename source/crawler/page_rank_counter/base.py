from typing import List, Dict
from dataclasses import dataclass

from urllib.parse import urlparse

from source.crawler.models.entity import ProcessEntity
from source.crawler.page_rank_counter.models.page_rank import PageRank


@dataclass
class PageRankCounter:
    """
    Interface, which stands for counting page rank 
    for a particular url with html content-type.
    
    Note:
        * page rank is calculated as:
            numberOfRepetativeUrlsPresentedOnPage / numberOfAllUrlsPresentedOnPage
        
        * url is considered to be repetative (same) if just urls domains match:
            same     -- http://www.foo.com/a.html <--> http://www.foo.com/b/c.html (same domains: www.foo.com)
            not same -- http://baz.foo.com/a.html <--> http://www.foo.com/b/c.html (not same domains: baz.foo.com != www.foo.com)

            * domain difinition:
                http://{everythingBetweenProtocolAndEnclousingSlash}/a.html
    """

    @staticmethod
    def retrieve_domain(url: str) -> str:
        """ Method, which stands for retrieving domain from url. """

        return urlparse(url).netloc

    def count_matched_domains(self, domain: str, urls: List[str]) -> int:
        """ Method, which stands for counting matched substring (domain) in strings (urls). """
        _counter = 0
        
        for url in urls:
            if domain == self.retrieve_domain(url):
                _counter += 1
        
        return _counter

    def count(self, entity: ProcessEntity):
        """ Method, which stands for counting page rank. """

        all_urls_count = entity.page_linked_urls.amount
        matched_urls_domain_count = self.count_matched_domains(domain=entity.metadata.domain,
                                                               urls=entity.page_linked_urls.urls)
        ratio = matched_urls_domain_count / all_urls_count

        return PageRank(url=entity.url, value=ratio)
        
    

