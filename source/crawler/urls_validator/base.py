from dataclasses import dataclass
from typing import List, Union, Dict

from requests import get
from bs4 import BeautifulSoup
from urllib.parse import urlparse

from source.crawler.urls_validator.models.page_metadata import PageMetadata


@dataclass
class UrlsValidator:
    """ 
    Interface, which stands for validating, whether a particular url(s)
    represents valid URL, which holds HTML content.

    Notes:
        Valid URL meets next requirements:
            - http/https protocol is presented
            - URL points to an HTML document (AKA web page)

    Returns: 
        PageMetadata
    
    Usage:
        url = 'someUrl'

        validator = UrlsValidator()
        validated_object = validator.validate(url=url)  # type(validated_object) --> PageMetadata
    """

    @staticmethod
    def url_protocol(url: str) -> Union[str, bool]:
        """ Method, which retrieves protocol (schema) from a URL. """

        _protocol = urlparse(url).scheme
        return False if not _protocol else _protocol

    @staticmethod
    def url_domain(url: str) -> Union[str, bool]:
        """ Method, which retrieves domain from a URL. """

        _domain = urlparse(url).netloc
        return False if not _domain else _domain

    @staticmethod
    def url_path(url: str) -> Union[str, bool]:
        """ Method, which retrieves path from a URL. """

        _path = urlparse(url).path
        return False if not _path else _path

    @staticmethod
    def populate_url_protocol(url: str) -> str:
        """ Method, which populates protocol for a URL. """

        _protocol = 'http://'
        return _protocol + url

    @staticmethod
    def url_exists(url: str) ->  bool:
        """ Method, which makes a sanity check request whether url address is up and exists.  """
        
        _valid_status = 200

        try:
            response = get(url, timeout=1)
            response.raise_for_status()
            return True if response.status_code == _valid_status else False
        except:
            return False

    @staticmethod
    def url_holds_html_body(url: str) -> Union[BeautifulSoup, bool]:
        """ Method, which makes sanity check request whether web application content type holds HTML. """

        _valid_content_type = 'text/html'
        _parser = 'html.parser'

        try:
            response = get(url, timeout=1)
            
            html_object = BeautifulSoup(response.text, _parser)
            html_headers = response.headers["content-type"]

            return html_object if _valid_content_type in html_headers else False

        except:
            return False

    def _process_single_url(self, url: str) -> Dict:
        """ Method, which processes single URL. """
        protocol, domain, path = self.url_protocol(url=url), self.url_domain(url=url), self.url_path(url=url)
        if not protocol:
            url = self.populate_url_protocol(url=url)
        
        url_exists = self.url_exists(url=url)
        html_object = self.url_holds_html_body(url=url)
    
        if url_exists and html_object:
            
            buffer =  {
                "url": url, 
                "html": html_object,
                "path": path,
                "domain": domain,
                "protocol": protocol
                }

            return PageMetadata(**buffer)
        
        return False
    
    def validate(self, urls: Union[str, List[str]]) -> Union[List[Dict], Dict, bool]:
        """ Main entrypoint to UrlsValdiator, which validates single or list of URLs. """

        if isinstance(urls, list):
            _result = []
            
            for url in urls:
                result = self._process_single_url(url=url)

                if result:
                    _result.append(result)

            return _result

        return self._process_single_url(url=urls)