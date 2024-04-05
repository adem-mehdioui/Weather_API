import requests

# My actual API key from OpenWeather
API_KEY = '071e521f4b844404703f6ce217161cd1'

# Define the base URL for the OpenWeather API
base_url = 'https://api.openweathermap.org/data/2.5/weather'

# Define the city you want to get weather information for
city_name = 'Paris'

# Construct the complete URL with parameters
url = f'{base_url}?q={city_name}&appid={API_KEY}&units=metric'


# Make a GET request to the API
response = requests.get(url)


# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Extract and print the JSON response
    data = response.json()
    print(f"Weather in {city_name}:")
    print(f"Temperature: {data['main']['temp']}°C")
    print(f"Description: {data['weather'][0]['description']}")
    print(f"Humidity: {data['main']['humidity']}%")
    print(f"Wind Speed: {data['wind']['speed']} m/s")
else:
    # Print an error message if the request was not successful
    print("Error:", response.status_code)




