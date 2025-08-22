
import os
import requests
from ics import Calendar, Event
from datetime import timedelta

# --- Configuration ---
API_KEY = "b835824104e32e9364252581d5e56e1b"
API_URL = "https://v3.football.api-sports.io/fixtures"
TEAM_ID = 165  # Borussia Dortmund
LEAGUE_ID = 78  # Bundesliga
SEASON = 2025
ICS_FILE_PATH = os.path.join("docs", "bvb_heimspiele.ics")

# --- Main Script ---
def fetch_fixtures():
    """Fetches fixtures from the API-Football."""
    headers = {
        "x-rapidapi-host": "v3.football.api-sports.io",
        "x-rapidapi-key": API_KEY
    }
    params = {
        "league": LEAGUE_ID,
        "season": SEASON,
        "team": TEAM_ID
    }
    response = requests.get(API_URL, headers=headers, params=params)
    response.raise_for_status()  # Raise an exception for bad status codes
    return response.json()["response"]

def create_calendar(fixtures):
    """Creates an ICS calendar from the fixtures."""
    cal = Calendar()
    for fixture in fixtures:
        # Filter for home games
        if fixture["teams"]["home"]["id"] == TEAM_ID:
            event = Event()
            event.name = f'BVB vs {fixture["teams"]["away"]["name"]}'
            event.begin = fixture["fixture"]["date"]
            event.duration = timedelta(hours=2)
            event.location = "Signal Iduna Park, Dortmund"
            
            competition = fixture["league"]["name"]
            round_info = fixture["league"]["round"]
            event.description = f'{competition} - {round_info}'
            
            cal.events.add(event)
    return cal

def save_calendar(cal):
    """Saves the calendar to the ICS file."""
    os.makedirs(os.path.dirname(ICS_FILE_PATH), exist_ok=True)
    with open(ICS_FILE_PATH, "w", encoding="utf-8") as f:
        f.write(str(cal))

if __name__ == "__main__":
    try:
        print("Fetching fixtures...")
        all_fixtures = fetch_fixtures()
        
        print("Creating calendar...")
        bvb_calendar = create_calendar(all_fixtures)
        
        print(f"Saving calendar to {ICS_FILE_PATH}...")
        save_calendar(bvb_calendar)
        
        print("Successfully generated BVB home games calendar.")
        
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from API: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
