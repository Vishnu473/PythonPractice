# 3. Install an external module and use it to perform an operation of your interest.
import requests

response = requests.get('https://api.github.com/users/Vishnu473')
if response.status_code == 200:
    user_data = response.json()
    print(f"Username: {user_data['login']}")
    print(f"Bio: {user_data['bio']}")
else:
    print("Failed to fetch data")