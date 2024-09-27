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
        total_results = data.get('total_results', 0)  
        total_pages = data.get('total_pages', 0)      

        return results, total_results, total_pages 
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return [], 0, 0 

def get_movie_details(id):
    movie_url = f"{BASE_URL}/movie/{id}?language=en-US"
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {TOKEN}"
    }

    response = requests.get(movie_url, headers=headers)
    
    if response.status_code != 200:
        print(f"Error fetching movie details: {response.status_code} - {response.text}")
        return None

    movie_data = response.json()

    credits_url = f"{BASE_URL}/movie/{id}/credits?language=en-US"
    credits_response = requests.get(credits_url, headers=headers)
    
    if credits_response.status_code != 200:
        print(f"Error fetching movie credits: {credits_response.status_code} - {credits_response.text}")
        return None

    credits_data = credits_response.json()
    director = next((member['name'] for member in credits_data['crew'] if member['job'] == 'Director'), None)

    movie_data['director'] = director if director else "Unknown"
    
    return movie_data