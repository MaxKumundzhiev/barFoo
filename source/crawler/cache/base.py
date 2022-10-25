from typing import Dict
from dataclasses import dataclass, field

from source.crawler.models.entity import ProcessEntity


@dataclass
class Cache:
    """ Interface, which mimics cache for processed pages. 
    
    Note:
        - it was used hash map (dict) as a simplicity representation of cache
        - each entity will be represented as:
            {
                'urlSampleNameOne': ProcessEntity,
                'urlSampleNameTwo': ProcessEntity,
                            ...
            }
    """

    entities: dict = field(default_factory=lambda: {})

    def __len__(self):
        return len(self.entities)

    def __getitem__(self, key: str):
        return False if key not in self.entities.keys() else self.entities.get(key)

    def __del__(self):
        return ' Cache cleaned. '
    
    def add(self, entity: ProcessEntity):
        self.entities[entity.url] = entity
