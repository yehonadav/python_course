import requests


while True:
    url = input("please enter a valid url, example https://qaviton.com:")
    filename = input("please enter an html file name") + '.html'

    try:
        response = requests.get(url)
        response.raise_for_status()
    except Exception as e:
        print(f'bad request {e}')
        continue

    try:
        with open(filename, 'wb') as file:
            file.write(response.content)
    except Exception as e:
        print(f'could nod write to file {e}')
        continue
    break
print("html file acquired!")
