from math import radians, sin, cos, sqrt, atan2

def distance(city1, city2):
    
    """
    >>> city1 = make_city('city1', 0, 1)
    >>> city2 = make_city('city2', 0, 2)
    >>> distance(city1, city2)
    1.0
    >>> city3 = make_city('city3', 6.5, 12)
    >>> city4 = make_city('city4', 2.5, 15)
    >>> distance(city3, city4)
    5.0
    """

    city1_lat, city1_lon = city1["latitude"], city1["longitude"]
    city2_lat, city2_lon = city2["latitude"], city2["longitude"]
    
    lat1, lon1, lat2, lon2 = map(radians, [city1_lat, city1_lon, city2_lat, city2_lon])

    R = 6371
    d_lat = lat2 - lat1
    d_lon = lon2 - lon1
    a = sin(d_lat/2)**2 + cos(lat1) * cos(lat2) * sin(d_lon/2)**2
    c = 2 * atan2(sqrt(a), sqrt(1-a))
    distance = R * c
    
    return distance
