import requests

url = "https://disease-drug-matching.p.rapidapi.com/get_disease/bethanechol"

headers = {
	"X-RapidAPI-Host": "disease-drug-matching.p.rapidapi.com",
	"X-RapidAPI-Key": "56d9de641bmshce72ffca6d5ab55p1effe9jsn25da4cf58d27"
}

response = requests.request("GET", url, headers=headers)

print(response.text)


# import requests

# url = 'https://dailymed.nlm.nih.gov/dailymed/services/v2/drugnames.json?name_type=both&pagesize=5&page=3
# '

# def get_drugs():
#     """
#     Function to consume http request and return a Quote class instance
#     """
#     response = requests.get(url).json()
