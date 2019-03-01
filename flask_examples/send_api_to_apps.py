import requests


response = requests.post(
    url='http://localhost/bunbun/add_content',
    data={'content': '<br/> add again'}
)

print(response.status_code)