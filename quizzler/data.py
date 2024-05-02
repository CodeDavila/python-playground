# Importing the requests module to make HTTP requests
import requests

# Setting up parameters for the API request
parameters = {
    "amount": 10,  # Number of questions to fetch
    "type": "boolean",  # Type of questions (boolean in this case)
}

# Sending a GET request to the Open Trivia Database API with specified parameters
response = requests.get("https://opentdb.com/api.php", params=parameters)
response.raise_for_status()  # Checking for any request errors

# Parsing the response data as JSON format
data = response.json()

# Extracting the question data from the response
question_data = data["results"]

