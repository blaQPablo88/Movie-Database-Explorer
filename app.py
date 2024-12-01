import requests

API_KEY = 'your_api_key'
BASE_URL = 'https://api.themoviedb.org/3'
# 

def search_movie(title):
    url = f"{BASE_URL}/search/movie"
    params = {
        "api_key": API_KEY,
        "query": title
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()['results']
    else:
        print(f"Error: {response.status_code}")
        return None

    results = search_movie("Inception")
    for movie in results:
        print(f"Title: {movie['title']}")
        print(f"Overview: {movie['overview']}")
        print(f"Poster: https://image.tmdb.org/t/p/w500{movie['poster_path']}\n")


search_movie('Absolution')