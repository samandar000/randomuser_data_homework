import json
from pprint import pprint

def get_gender_users(data:dict) -> list:
    """
    Take the gender of the users and return the list.
    
    The list items are as follows:
        If the user is male: {"Male":1}
        If the user is female: {"Female":0}
    
    Args:
        data(dict): data
    Returns:
        list: users get gender list
    """
    answer = []
    for i in data['results']:
        if i['gender'] == 'male':
            answer.append({'Male':1})
        else:
            answer.append({'Female':0})
    return answer
f = open('randomuser_data.json').read()
data = json.loads(f)
