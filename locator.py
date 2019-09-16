# TODO: create a program to fetch html content
# TODO: from a selected website
# TODO: print counters of re-occurring words
# TODO: commit before each time you run this script
# TODO: hint: use the requests module & input build-in function
import requests

url = input("please enter a valid url:")

response = requests.get('https://'+url)
print(response.text)