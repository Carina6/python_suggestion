#!/usr/bin/python3
# -*- coding: utf-8 -*-

from urllib import parse
import unittest


class TestDict(unittest.TestCase):

    def test_url_parse(self):
        url = r'https://docs.python.org/3.5/search.html?q=parse&check_keywords=yes&area=default'
        parseResult = parse.urlparse(url)
        print(parseResult)
        param_dict = parse.parse_qs(parseResult.query)
        print(param_dict)
        q = param_dict['q'][0]
        print(q)


if __name__ == '__main__':
    unittest.main()




