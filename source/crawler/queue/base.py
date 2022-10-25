from typing import List
from dataclasses import dataclass, field


@dataclass
class Queue:
    """ Interface, which stands for queue. """

    urls: List = field(default_factory=lambda: [])
    processed_urls_count: int = field(default_factory=lambda: 0)

    def enqueue(self, item):
        self.urls.insert(0, item)

    def dequeue(self):
        return self.urls.pop()

    def update(self):
        self.processed_urls_count += 1

    def size(self):
        return len(self.urls)