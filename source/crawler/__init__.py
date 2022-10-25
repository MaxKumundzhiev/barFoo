from source.crawler.cache.base import Cache
from source.crawler.queue.base import Queue

from source.crawler.logger.base import InternalLogger

from source.crawler.driver.local.writer import Writer
from source.crawler.urls_validator.base import UrlsValidator
from source.crawler.page_rank_counter.base import PageRankCounter
from source.crawler.linked_pages_crawler.base import LinkedPagesCrawler

from source.crawler.models.entity import ProcessEntity

LOGGER = InternalLogger().writer

CACHE = Cache()
QUEUE = Queue()

VALIDATOR = UrlsValidator()
COUNTER = PageRankCounter()
CRAWLER = LinkedPagesCrawler()

WRITER = Writer()

event = ProcessEntity()