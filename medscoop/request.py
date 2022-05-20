import json
import requests
import urllib3


def get_drug():
    """
    Function to consume http request and return an iteration of all drugs
    """

    url = "https://disease-drug-matching.p.rapidapi.com/search_disease/ad"

    headers = {
        "X-RapidAPI-Host": "disease-drug-matching.p.rapidapi.com",
        "X-RapidAPI-Key": "e4fa28b2d1msh62f65794a69ea7fp1e3b27jsncb86e159f234"
    }
    drug_list = []
    response = requests.request("GET", url, headers=headers)
    response.raise_for_status
    respo_list = response.json()
    i = 0

    for item in respo_list:
        drug = respo_list[i]['drug']
        i += 1
        drug_list.append(drug)
    print(drug_list)

    return drug_list

def get_drug_info():
    url = "https://drugapi.p.rapidapi.com/Drug/Summary/Azithromycin"

    headers = {
        "X-RapidAPI-Host": "drugapi.p.rapidapi.com",
        "X-RapidAPI-Key": "f7725bf91bmsh8b9c4b9c66c3030p1e178ejsn96a72c0ea9dd"
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


# def search_drug(disease_name):
#     search_drugs_url = 'https://disease-drug-matching.p.rapidapi.com/get_drug/{}'.format(api_key,disease_name)
    
#     headers = {
#         "X-RapidAPI-Host": "disease-drug-matching.p.rapidapi.com",
#         "X-RapidAPI-Key": "e4fa28b2d1msh62f65794a69ea7fp1e3b27jsncb86e159f234"
#     }
    
#     with urllib3.request.urlopen(search_drugs_url) as url:
#         search_drug_data = url.read()
#         search_drug_response = json.loads(search_drug_data)

#         search_drug_results = None

#         if search_drug_response['results']:
#             search_drug_list = search_drug_response['results']
#             i = 0
#             for result in search_drug_list:
#                 result = search_drug_list[i]['drug']
#                 i += 1
#                 print(result)
#             search_drug_results = process_results(search_drug_list)


#     return search_drug_results

