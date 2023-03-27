import pytest
import requests

class TestAPI:
    def test1(self1):
        url ='https://api.dictionaryapi.dev/api/v2/entries/en/success'
        response = requests.get(url)
        assert 400>response.status_code>=200



    def test2(self):
            url = 'https://api.dictionaryapi.dev/api/v2/entries/en/success'
            response = requests.get(url)
            dict1 = response.json()
            actual = dict1[0]['word']
            expected = 'success'
            assert actual == expected



    def test3(self):
            url = 'https://api.dictionaryapi.dev/api/v2/entries/en/human'
            response = requests.get(url)
            dict1 = response.json()
            actual = dict1[0]['word']
            expected = 'human'
            assert actual == expected


