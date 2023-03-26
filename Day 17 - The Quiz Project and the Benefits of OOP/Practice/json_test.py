from urllib.request import urlopen
import json

number_quiz = 1
url = f"https://opentdb.com/api.php?amount={number_quiz}&type=boolean"

response = urlopen(url)

json_data = json.loads(response.read())

print(json_data)