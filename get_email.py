import json

def get_email(data:dict) -> list:
    """
    Take the email of the users and return the list.

    Args:
        data(dict): data
    Returns:
        list: users email
    """
    answer = []
    for i in data['results']:answer.append(i['email'])
    return answer
f = open('randomuser_data.json').read()
data = json.loads(f)