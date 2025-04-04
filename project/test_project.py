import pytest
import requests
import requests_mock
from bs4 import BeautifulSoup
from project import get_webpage_content, parse_html, extract_movie_data

def test_get_webpage_content(requests_mock):
    url = "https://www.example.com"
    mock_html = "<html><head><title>Test</title></head><body>Content</body></html>"
    requests_mock.get(url, text=mock_html)
    content = get_webpage_content(url)
    assert content is not None
    assert "Content" in content.decode('utf-8')

def test_parse_html():
    html_content = "<html><head><title>Test</title></head><body>Content</body></html>"
    soup = parse_html(html_content)
    assert isinstance(soup, BeautifulSoup)
    assert soup.title.string == "Test"

def test_extract_movie_data():
    movie = {
        "item": {
            "name": "The Shawshank Redemption",
            "duration": "PT142M",
            "aggregateRating": {
                "ratingValue": "9.3"
            }
        }
    }
    rank, name, runtime, rating = extract_movie_data(movie, 0)
    assert rank == 1
    assert name == "The Shawshank Redemption"
    assert runtime == "142m"
    assert rating == "9.3"
