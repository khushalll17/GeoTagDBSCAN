# GeoTagDBSCAN
This project is a comprehensive Flask-based web application designed to help users find the optimal location within a city based on a variety of user-defined criteria. By leveraging the Google Maps API, the application performs detailed analysis and clustering of amenities within a specified radius and calculates the best possible location based on travel time, distance, and amenity ratings.

Key Features: Google Maps API Integration:

Fetches real-time data on amenities within a specified radius using the Google Maps Places API. Supports multiple modes of transportation (driving, walking, bicycling, and transit) for travel time calculations using the Google Maps Directions API. Amenity Analysis and Clustering:

Allows users to specify a list of desired amenities (e.g., parks, restaurants, schools) and fetches their locations and details, including names, addresses, and ratings. Utilizes DBSCAN clustering to group amenities based on proximity, helping identify concentrated areas of interest within the city. Custom Scoring Algorithm:

Calculates a score for each potential location based on user preferences for travel time and amenity ratings. Considers factors such as normalized travel time, distance to amenities, and user-defined weights to determine the most suitable location. Dynamic Location Scoring:

Compares multiple candidate locations within a city to find the one that best matches the user’s criteria. Provides detailed output, including the best location’s address, the optimal mode of transportation to the user’s current location, and distances to the nearest amenities. Error Handling and API Optimization:

Handles potential errors such as API request failures gracefully, ensuring a smooth user experience. Includes mechanisms to filter amenities by rating and optimize API calls to reduce costs. Comprehensive Output:

Returns detailed information about the best location, including travel times, the most efficient mode of transport, and proximity to key amenities. Presents results in a structured JSON format, making it easy to integrate with other applications or extend functionality. Technologies Used: Flask: Backend framework for building the web application. Google Maps API: For fetching location data, calculating distances, and determining travel times. DBSCAN (Density-Based Spatial Clustering of Applications with Noise): For clustering amenity locations based on geographic proximity. Geopy: For calculating geographical distances between coordinates. NumPy: For efficient numerical calculations, particularly in the scoring algorithm. Use Cases: City Planning: Assists urban planners in identifying optimal locations for new developments based on existing amenities. Real Estate: Helps real estate agents and buyers find areas with the best access to desired amenities. Relocation Assistance: Provides individuals and families with personalized recommendations for where to live based on their unique preferences. This project offers a powerful tool for making informed decisions about location-based choices in urban environments, backed by real-time data and advanced clustering algorithms.
