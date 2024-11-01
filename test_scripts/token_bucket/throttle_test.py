import time
import random
import requests

url = "http://localhost:8000/bucket/bucket_stats/"

while True:
    response = requests.get(url)
    print(response.json())
    if response.status_code != 200:
        time.sleep(random.randint(1, 10))
        continue
