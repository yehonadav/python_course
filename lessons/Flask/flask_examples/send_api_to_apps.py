import requests


# response = requests.post(
#     url='http://localhost/bunbun/add_content',
#     data={'content': '<br/> add again'}
# )

# response = requests.post(
#     url='http://localhost:5000/register',
#     data={'username': 'john2', 'password': '123'}
# )

response = requests.post(
    url='http://localhost:5000/login',
    data={'username': 'john2', 'password': '123'}
)

print(response.status_code)
print(response.text)
