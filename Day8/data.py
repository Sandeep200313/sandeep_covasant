import random

weather_data = {
    "Hyderabad": {"temperature": random.randint(25, 35), "condition": "Sunny", "humidity": random.randint(40, 60)},
    "Mumbai": {"temperature": random.randint(28, 36), "condition": "Cloudy", "humidity": random.randint(50, 70)},
    "Delhi": {"temperature": random.randint(30, 40), "condition": "Hazy", "humidity": random.randint(30, 50)},
    "Bangalore": {"temperature": random.randint(20, 30), "condition": "Rainy", "humidity": random.randint(60, 80)},
    "Kolkata": {"temperature": random.randint(26, 34), "condition": "Humid", "humidity": random.randint(55, 75)},
    "Chennai": {"temperature": random.randint(27, 37), "condition": "Hot", "humidity": random.randint(50, 70)},
    "Pune": {"temperature": random.randint(22, 32), "condition": "Pleasant", "humidity": random.randint(45, 65)},
    "Ahmedabad": {"temperature": random.randint(28, 38), "condition": "Dry", "humidity": random.randint(30, 50)},
    "Jaipur": {"temperature": random.randint(25, 38), "condition": "Warm", "humidity": random.randint(30, 55)},
    "Lucknow": {"temperature": random.randint(24, 36), "condition": "Foggy", "humidity": random.randint(40, 60)},
    "Bhopal": {"temperature": random.randint(22, 34), "condition": "Cool", "humidity": random.randint(50, 70)},
    "Visakhapatnam": {"temperature": random.randint(26, 35), "condition": "Windy", "humidity": random.randint(50, 75)},
    "Nagpur": {"temperature": random.randint(28, 40), "condition": "Hot", "humidity": random.randint(35, 60)},
    "Coimbatore": {"temperature": random.randint(20, 30), "condition": "Mild", "humidity": random.randint(55, 75)},
    "Thiruvananthapuram": {"temperature": random.randint(24, 34), "condition": "Rainy", "humidity": random.randint(65, 85)},
    "Indore": {"temperature": random.randint(25, 36), "condition": "Clear", "humidity": random.randint(40, 60)},
    "Guwahati": {"temperature": random.randint(22, 32), "condition": "Humid", "humidity": random.randint(50, 75)},
    "Surat": {"temperature": random.randint(27, 37), "condition": "Warm", "humidity": random.randint(45, 70)},
    "Vijayawada": {"temperature": random.randint(26, 36), "condition": "Cloudy", "humidity": random.randint(55, 75)},
    "Madurai": {"temperature": random.randint(27, 37), "condition": random.choice(["Hot", "Sunny"]), "humidity": random.randint(50, 70)},
    "Amritsar": {"temperature": random.randint(24, 34), "condition": random.choice(["Foggy", "Cloudy"]), "humidity": random.randint(45, 65)},
    "Rajkot": {"temperature": random.randint(26, 36), "condition": random.choice(["Dry", "Clear"]), "humidity": random.randint(30, 55)},
    "Vadodara": {"temperature": random.randint(25, 35), "condition": random.choice(["Clear", "Warm"]), "humidity": random.randint(40, 60)},
    "Mysore": {"temperature": random.randint(22, 32), "condition": random.choice(["Pleasant", "Cloudy"]), "humidity": random.randint(55, 75)},
    "Patna": {"temperature": random.randint(27, 37), "condition": random.choice(["Humid", "Rainy"]), "humidity": random.randint(50, 70)},
    "Jamshedpur": {"temperature": random.randint(26, 36), "condition": random.choice(["Cloudy", "Foggy"]), "humidity": random.randint(55, 75)},
    "Dehradun": {"temperature": random.randint(20, 30), "condition": random.choice(["Cool", "Windy"]), "humidity": random.randint(50, 70)},
    "Meerut": {"temperature": random.randint(24, 34), "condition": random.choice(["Hazy", "Clear"]), "humidity": random.randint(40, 60)},
    "Shimla": {"temperature": random.randint(15, 25), "condition": random.choice(["Snowy", "Cold"]), "humidity": random.randint(60, 80)}
}

cities = {
    "cities" : [key for key in weather_data.keys()]
}