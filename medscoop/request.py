import requests


def get_drug_list_func(a_list):
    for item in a_list:
        yield item

def get_drug():
    """
    Function to consume http request and return an iteration of all drugs
    """

    url = "https://disease-drug-matching.p.rapidapi.com/get_drug/malaria"

    headers = {
        "X-RapidAPI-Host": "disease-drug-matching.p.rapidapi.com",
        "X-RapidAPI-Key": "56d9de641bmshce72ffca6d5ab55p1effe9jsn25da4cf58d27"
    }
    response = requests.request("GET", url, headers=headers)
    response.raise_for_status
    respo_list = response.json()
    i = 0
    for result in get_drug_list_func(respo_list):
        result = respo_list[i]['drug']
        i += 1
        print(result)


def get_drug_info():
    url = "https://drugapi.p.rapidapi.com/Drug/Summary/Acetaminophen-and-Codeine-Phosphate-Oral-Solution-acetaminophen-codeine-phosphate-665"

    headers = {
        "X-RapidAPI-Host": "drugapi.p.rapidapi.com",
        "X-RapidAPI-Key": "56d9de641bmshce72ffca6d5ab55p1effe9jsn25da4cf58d27"
    }

    response = requests.request("GET", url, headers=headers)
    response.raise_for_status
    respoDict = response.json()
    results = respoDict.get('results')
    description = results[0]['description']
    commonBrands = results[0]['commonBrands']
    administration = results[0]['administration']   
    adverseReactions = results[0]['adverseReactions']
    precautions = results[0]['precautions']
    print(description, commonBrands, administration, adverseReactions, precautions)
    return (description, commonBrands, administration, adverseReactions, precautions)
