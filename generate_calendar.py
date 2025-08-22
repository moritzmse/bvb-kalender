import os
import requests
from ics import Calendar, Event
from datetime import timedelta

# --- Configuration ---
API_KEY = "0da701f1beac437284b3ba0c0e6c68ec"
TEAM_ID = 4  # Borussia Dortmund
ICS_FILE_PATH = os.path.join("docs", "bvb_heimspiele.ics")

# --- Main Script ---
def fetch_fixtures():
    """Fetches fixtures from the football-data.org API."""
    headers = {
        "X-Auth-Token": API_KEY
    }
    api_url = f"https://api.football-data.org/v4/teams/{TEAM_ID}/matches"
    response = requests.get(api_url, headers=headers)
    response.raise_for_status()
    return response.json()["matches"]

def create_calendar(fixtures):
    """Creates an ICS calendar from the fixtures."""
    cal = Calendar()
    for fixture in fixtures:
        # Filter for home games
        if fixture["homeTeam"]["id"] == TEAM_ID:
            event = Event()
            event.name = f'{fixture["homeTeam"]["name"]} vs {fixture["awayTeam"]["name"]}'
            event.begin = fixture["utcDate"]
            event.duration = timedelta(hours=2)
            event.location = "Signal Iduna Park, Dortmund"
            
            competition = fixture["competition"]["name"]
            matchday = fixture["matchday"]
            if matchday:
                event.description = f"{competition} - Spieltag {matchday}"
            else:
                event.description = competition

            cal.events.add(event)
    return cal

def save_calendar(cal):
    """Saves the calendar to the ICS file."""
    os.makedirs(os.path.dirname(ICS_FILE_PATH), exist_ok=True)
    with open(ICS_FILE_PATH, "w", encoding="utf-8") as f:
        f.write(str(cal))

if __name__ == "__main__":
    try:
        print("Fetching fixtures from football-data.org...")
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