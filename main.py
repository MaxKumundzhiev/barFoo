from pydantic_cli import run_and_exit

from source.crawler.users_input_handler.base import CommandLineInterface
from source.crawler import LOGGER, QUEUE, CACHE, VALIDATOR, CRAWLER, COUNTER, WRITER, event


def main(arguments: CommandLineInterface) -> int:
    """ Main entrypoint to launch the system. """
    
    # handle 1st url, when queue and cache are empty
    if not event.url:
        event.url, event.depth = arguments.url, arguments.depth

        validation_object = VALIDATOR.validate(urls=event.url)
        if validation_object:
            event.metadata = validation_object
            QUEUE.enqueue(event.url)
        else:
            raise SystemExit(f'Passed invalid url: {event.url}')

    # assume 1st url passed validation
    current_depth = 1
    while QUEUE.processed_urls_count != event.depth:
        
        event.url = QUEUE.dequeue()

        if not CACHE[event.url]:
            crawling_object = CRAWLER.crawl(entity=event)
            event.page_linked_urls = crawling_object

            [QUEUE.enqueue(url) for url in event.page_linked_urls.urls if QUEUE.size() != event.depth]

            page_rank_object = COUNTER.count(entity=event)
            event.page_rank = page_rank_object

            CACHE.add(entity=event)
            QUEUE.update()

            WRITER.add(current_depth=current_depth, entity=event)
            current_depth += 1

        else:
            continue
    
    LOGGER.info(WRITER.show())
    WRITER.save()
    return 0


if __name__ == "__main__":
    run_and_exit(CommandLineInterface, main, description=__doc__, version="0.1.0")