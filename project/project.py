import requests
from bs4 import BeautifulSoup
import json
import pandas as pd

def get_webpage_content(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'} #To mimic a browser request
    response = requests.get(url, headers=headers)
    response.raise_for_status() #To raise exceptions for bad status codes
    return response.content #Raw HTML content

def parse_html(content):
    return BeautifulSoup(content, 'html.parser')

def extract_movie_data(movie, index):
    print(json.dumps(movie, indent=2))  #Debugging line to view entire movie dictionary
    rank = index + 1
    name = movie["item"].get("name", "N/A") #Extract movie name, N/A if not found
    runtime = movie["item"].get("duration", "N/A").replace("PT", "").lower() #Extract runtime, remove "PT" prefix
    rating = movie["item"].get("aggregateRating", {}).get("ratingValue", "N/A") #Extract rating from nested dictionary
    return rank, name, runtime, rating

def scrape_imdb_top_movies(url):
    content = get_webpage_content(url)
    soup = parse_html(content)

    script_tag = soup.find('script', type="application/ld+json") #Script tag containing JSON data
    if not script_tag:
        raise ValueError("Could not find the JSON data in the script tag")

    json_data = script_tag.string
    data = json.loads(json_data)

    movies = data.get("itemListElement", []) #Extract movie list
    if not movies:
        raise ValueError("No movies found in the JSON data")

    movie_data = []
    for index, movie in enumerate(movies):
        movie_data.append(extract_movie_data(movie, index))
    return movie_data

def save_as_csv(movie_data):
    df = pd.DataFrame(movie_data, columns=['Rank', 'Name', 'Runtime', 'Rating'])
    df.to_csv("IMDB_Top_250_Movies.csv", index=False)

def main():
    url = 'https://www.imdb.com/chart/top'
    movie_data = scrape_imdb_top_movies(url)

    if movie_data:
        for movie in movie_data:
            print("Rank: {}, Name: {}, Runtime: {}, Rating: {}".format(*movie)) #Unpack movie tuple
        save_as_csv(movie_data)

if __name__ == "__main__":
    main()
