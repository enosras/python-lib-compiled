#this code is vibe coded.... only for familirization and hands on experience with some of these object

import requests

# Define the URL you want to send a GET request to
url = "https://api.github.com/events"

# Send a GET request to the specified URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Print the content of the response (in this case, JSON data)
    print("Request successful!")
    print("Response content (JSON):")
    print(response.json())  # Use .json() to parse JSON response into a Python dictionary
else:
    # Print an error message if the request was not successful
    print(f"Request failed with status code: {response.status_code}")
    print(f"Error message: {response.text}")

# You can also access other properties of the response object
print(f"\nStatus Code: {response.status_code}")
print(f"Response Headers: {response.headers}")
print(f"Content Type: {response.headers.get('Content-Type')}")