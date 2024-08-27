import requests
import json

coordinates_log = []  # List to store coordinates for each scenario

# Sample scenarios for testing
scenarios = [
    {
        "current_location": "12.9715987,77.5945627",
        "city": "Bangalore",
        "country": "India",
        "best_location_type": "restaurant",
        "time_preference": 4.0,
        "rating_preference": 3.0,
        "min_rating": 4.0,
        "amenities_list": ["hospital", "school", "park"],
        "radius": 5000
    },
    {
        "current_location": "12.9715987,77.5945627",
        "city": "Bangalore",
        "country": "India",
        "best_location_type": "cafe",
        "time_preference": 5.0,
        "rating_preference": 4.0,
        "min_rating": 3.5,
        "amenities_list": ["mall", "pharmacy", "gym"],
        "radius": 6000
    },
    # Add 8 more scenarios with different parameters
    {
        "current_location": "12.935192,77.624480",
        "city": "Bangalore",
        "country": "India",
        "best_location_type": "restaurant",
        "time_preference": 3.0,
        "rating_preference": 4.5,
        "min_rating": 4.0,
        "amenities_list": ["hospital", "school", "supermarket"],
        "radius": 4000
    },
    {
        "current_location": "12.990142,77.617888",
        "city": "Bangalore",
        "country": "India",
        "best_location_type": "shopping_mall",
        "time_preference": 4.5,
        "rating_preference": 4.0,
        "min_rating": 3.5,
        "amenities_list": ["park", "gym", "pharmacy"],
        "radius": 4500
    },
    {
        "current_location": "12.951299,77.580681",
        "city": "Bangalore",
        "country": "India",
        "best_location_type": "hotel",
        "time_preference": 4.0,
        "rating_preference": 3.5,
        "min_rating": 4.0,
        "amenities_list": ["restaurant", "bar", "cafe"],
        "radius": 3500
    },
    {
        "current_location": "12.917174,77.623863",
        "city": "Bangalore",
        "country": "India",
        "best_location_type": "theater",
        "time_preference": 3.5,
        "rating_preference": 4.0,
        "min_rating": 3.5,
        "amenities_list": ["restaurant", "shopping_mall", "park"],
        "radius": 5000
    },
    {
        "current_location": "12.958284,77.700927",
        "city": "Bangalore",
        "country": "India",
        "best_location_type": "park",
        "time_preference": 5.0,
        "rating_preference": 3.5,
        "min_rating": 3.0,
        "amenities_list": ["gym", "cafe", "pharmacy"],
        "radius": 6000
    },
    {
        "current_location": "12.934491,77.609648",
        "city": "Bangalore",
        "country": "India",
        "best_location_type": "museum",
        "time_preference": 4.5,
        "rating_preference": 4.5,
        "min_rating": 4.0,
        "amenities_list": ["restaurant", "theater", "cafe"],
        "radius": 4500
    },
    {
        "current_location": "12.923503,77.678568",
        "city": "Bangalore",
        "country": "India",
        "best_location_type": "cafe",
        "time_preference": 4.0,
        "rating_preference": 4.0,
        "min_rating": 3.5,
        "amenities_list": ["hospital", "school", "gym"],
        "radius": 4000
    },
    {
        "current_location": "12.989172,77.706288",
        "city": "Bangalore",
        "country": "India",
        "best_location_type": "restaurant",
        "time_preference": 3.0,
        "rating_preference": 3.5,
        "min_rating": 3.0,
        "amenities_list": ["shopping_mall", "theater", "pharmacy"],
        "radius": 5000
    }
]

# Define the Flask application's URL
url = "http://127.0.0.1:5000/find_best_location"

# Iterate through each scenario
for scenario in scenarios:
    # Send a POST request to the Flask application
    response = requests.post(url, json=scenario)
    
    if response.status_code == 200:
        print(f"Scenario processed successfully: {scenario['current_location']}")
    else:
        print(f"Error for scenario {scenario['current_location']}: {response.status_code} {response.text}")



print("Coordinates data stored successfully in 'coordinates_log.json'")
