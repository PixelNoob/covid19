import json
import requests
from covid import Covid

covid = Covid()
cases = covid.get_data()

cases= json.dumps(cases)

with open('cases.json', 'w') as f:
    print(cases, file=f)
