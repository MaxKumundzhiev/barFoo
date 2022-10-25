import pandas as pd

from typing import List, Dict

from dataclasses import dataclass, field
from source.crawler.models.entity import ProcessEntity


@dataclass
class Writer:
    """ Interface to write resulting format to local machine. """
    
    _COLUMNS = ['url', 'depth', 'ratio']

    rows: List[Dict] = field(default_factory=lambda: [])
    
    filename: str = 'crawler'
    extension: str = 'tsv'
    separator: str = '\t'

    def add(self, current_depth: int, entity: ProcessEntity):
        row = {'url': entity.url, 'depth': current_depth, 'ratio': entity.page_rank.value}
        self.rows.append(row)

    def save(self):
        dataframe = pd.DataFrame(data=self.rows, columns=self._COLUMNS)
        dataframe.drop_duplicates(subset=['url'], keep=False).to_csv(f'{self.filename}.{self.extension}', sep=self.separator)
    
    def show(self):
        dataframe = pd.DataFrame(data=self.rows, columns=self._COLUMNS)
        return dataframe.drop_duplicates(subset=['url'], keep=False)
        


