import json

def get_count_users(data:dict) -> int:
    """
    You are given dictionary. Find the number of users.

    Args:
        data(dict): data
    Returns:
        int: number of users
    """
    
    k = (list(data['results']))
    return k
f = open('randomuser_data.json').read()
data = json.loads(f)

    