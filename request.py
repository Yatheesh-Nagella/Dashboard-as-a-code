import requests

# Assuming your FastAPI server is running on http://127.0.0.1:8000
url = "http://10.0.5.2:8000"

# Sending a GET request to the root path
response = requests.get(url)
print("Response from root path:", response.json())

# Sending a GET request to /items/{item_id}
item_id = 42
query_param = "example"
response = requests.get(f"{url}/items/{item_id}", params={"query_param": query_param})
print(f"Response from /items/{item_id}:", response.json())
