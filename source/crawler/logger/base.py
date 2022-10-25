import logging
from os import environ

from dataclasses import dataclass, field


@dataclass
class InternalLogger:
    """ Interface, which stands for outputting processes logs. """
    
    writer: logging = field(default_factory=lambda: logging.getLogger(__doc__))

    def __post_init__(self):
        logging.basicConfig(level=environ.get("LOGLEVEL", "INFO"))