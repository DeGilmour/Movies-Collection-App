import requests
import os

API_KEY = os.getenv("API_KEY")
TOKEN = os.getenv(("TOKEN"))
BASE_URL = 'https://api.themoviedb.org/3'

def search_movie_by_title(title, page=1):
    print(f"Searching for movie: {title}")
    url = f"{BASE_URL}/search/movie?query={title}&include_adult=false&language=en-US&page={page}"

    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {TOKEN}"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        results = data.get('results', [])
        total_results = data.get('total_results', 0)  # Get the total number of results
        total_pages = data.get('total_pages', 0)      # Get the total number of pages

        return results, total_results, total_pages  # Return results, total count, and total pages
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return [], 0, 0  # Return empty list and zero results on error


def get_movie_details(id):
    # hurl = "https://api.themoviedb.org/3/movie/70829?language=en-US"
    url = f"{BASE_URL}/movie/{id}?language=en-US"
    print(url)
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {TOKEN}"
    }

    response = requests.get(url, headers=headers)
    
    data = response.json()
    
    if response.status_code == 200:
        data = response.json()
        
        return data
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return []