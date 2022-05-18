import requests
def get_drug():
    """
    Function to consume http request and return a Quote class instance
    """

    url = "https://disease-drug-matching.p.rapidapi.com/get_drug/Acute%20Promyelocytic%20Leukemia"

    headers = {
        "X-RapidAPI-Host": "disease-drug-matching.p.rapidapi.com",
        "X-RapidAPI-Key": "56d9de641bmshce72ffca6d5ab55p1effe9jsn25da4cf58d27"
    }

    response = requests.request("GET", url, headers=headers)
    response.raise_for_status
    this = response.json()
    i = 0
    for item in this:
        theese = this[i]['drug']
        i += 1
        if theese == theese:
            break
        else:   
            print(theese)
    return theese
get_drug()


