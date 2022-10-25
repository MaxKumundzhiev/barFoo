from typing import List, Union
from dataclasses import dataclass

from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin

from source.crawler.models.entity import ProcessEntity
from source.crawler.linked_pages_crawler.models.page_linked_urls import PageLinkedUrls


@dataclass
class LinkedPagesCrawler:
    """ 
    Interface, which is supossed to fetch statically linked pages
    and make certain adjustments if needed for a particular valid URL. 
    
    Note:
        Linked pages:
            All the links in the HTML document, i.e. HTML <a> elements with an href attribute.
            Excluding any <a> tags that may be dynamically added by scripts.
        
        Certain Adjustments:
            Link can appear in  Absolute | Relative Path | Anchor format.
            The interface will adjust all non `absolute` format to `absolute`.   
    """

    @staticmethod
    def find_urls(html: BeautifulSoup) -> Union[str, List[str]]:
        """ Method, which fetches all <a href=...> elements from html object. """

        _link_tag = 'a'
        _link_attribute = 'href'

        return [link.get(_link_attribute) for link in html.findAll(_link_tag)]

    @staticmethod
    def is_absolute(url: str) -> bool:
        """ Method, which checks whether URL is absolute. 
            
        Reference:
            https://www.w3schools.com/html/html_filepaths.asp
        """

        _is_absolute = bool(urlparse(url).netloc)
        return _is_absolute

    @staticmethod
    def cast_relative_to_absolute(relative: str, absolute: str) -> str:
        """ Method, which casts relative to absolute URL. """
        
        return urljoin(absolute, relative)

    def crawl(self, entity: ProcessEntity) -> Union[str, List[str]]:
        """ Main entrypoint to LinkedPagesCrawler, which crawls statically linked URLs. """

        _anchor_character = '#'
        _root_character = '/'
        _urls = self.find_urls(html=entity.metadata.html)

        for index, _url in enumerate(_urls):
            if _url is None:
                _urls.pop(index)

            if _url == _anchor_character or _url == _root_character:
                _urls.pop(index)

            if not self.is_absolute(url=_url):
                _urls[index] = self.cast_relative_to_absolute(relative=_url, absolute=entity.url)

        return PageLinkedUrls(url=entity.url, urls=_urls, amount=len(_urls))