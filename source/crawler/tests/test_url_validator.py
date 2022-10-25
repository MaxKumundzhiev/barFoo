import json

from os.path import dirname, abspath
from unittest import TestCase, main as run_tests

from source.crawler.urls_validator.base import UrlsValidator


class TestUrlsValidator(TestCase):
    ROOT_DIR = dirname(abspath(__file__))
    SCAFFOLDING_DATA_PATH = f'{ROOT_DIR}/assets/test_suites.json'

    @classmethod
    def setUpClass(self):
        self.test_suits = json.load(open(self.SCAFFOLDING_DATA_PATH))

    def test_url_protocol(self):
        _tests = self.test_suits['url_validator']['test_url_protocol']

        if _tests is not None:
            for test in _tests:
                _url, _expected_result, _description = test['data'], test['expected_result'], test['description']
                _obtained_result = UrlsValidator.url_protocol(url=_url)
                self.assertEqual(_obtained_result, _expected_result, _description)

    def test_url_domain(self):
        _tests = self.test_suits['url_validator']['test_url_domain']

        if _tests is not None:
            for test in _tests:
                _url, _expected_result, _description = test['data'], test['expected_result'], test['description']
                _obtained_result = UrlsValidator.url_domain(url=_url)
                self.assertEqual(_obtained_result, _expected_result, _description)

    def test_url_path(self):
        _tests = self.test_suits['url_validator']['test_url_path']

        if _tests is not None:
            for test in _tests:
                _url, _expected_result, _description = test['data'], test['expected_result'], test['description']
                _obtained_result = UrlsValidator.url_path(url=_url)
                self.assertEqual(_obtained_result, _expected_result, _description)


if __name__ == '__main__':
    run_tests()