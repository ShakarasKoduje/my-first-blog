import requests

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'

r = requests.get(url)

print("Kod stanu: ", r.status_code)

response_dict = r.json()

print(response_dict.keys())
repo_dicts = response_dict['items']
for i in range(10):
    repo_dict = repo_dicts[-i]
    print('---------')
    print(repo_dict['name'])
    print(repo_dict['owner']['login'])
          
