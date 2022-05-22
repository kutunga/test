import requests

secret_key = 'Nmko01hba12mqnf2367'

url = http://127.0.0.1:8000/admin/dashboard

headers = {'X-Key-Test': 'f"{secret_key}"'}

resp = requests.get(url, headers = headers)


print(resp.content)
