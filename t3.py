import requests

# Sample JSON API URL
url = 'https://jsonplaceholder.typicode.com/posts/1'

# Make the GET request
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Print the response JSON
    print(response.json())
else:
    print(f"Failed to retrieve data. Status Code: {response.status_code}")
