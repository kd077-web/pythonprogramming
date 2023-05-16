                    #requests module
#we can download directly in the python workspacae by using a request module
import requests
response = requests.get("https://www.google.com")
print(response.text)
