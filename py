import requests
from bs4 import BeautifulSoup

URL = 'https://weather.com/weather/today'  # Replace with your desired weather website URL
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

# Example: Find temperature element (You need to replace the class name based on actual page structure)
temperature = soup.find('div', class_='YourTemperatureClassName').get_text()

# Example: Find other weather details (Replace with actual HTML structure)
humidity = soup.find('div', class_='YourHumidityClassName').get_text()
wind_speed = soup.find('div', class_='YourWindSpeedClassName').get_text()

print(f'Temperature: {temperature}')
print(f'Humidity: {humidity}')
print(f'Wind Speed: {wind_speed}')
