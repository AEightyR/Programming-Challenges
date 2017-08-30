import json
import requests
import os

def main():
	print("Welcome to the identity generator!")
	gender = raw_input("Would you like to be a male or female? \n").lower()
	if gender == "male" or gender == "female":
		js = reachout(gender)
		printinfo(js)
	else:
		print("Stop trying to put dumb shit in here")
		
def reachout(gender):
	URL = "https://randomuser.me/api/?gender={}&format=pretty".format(gender)
	response = requests.get(URL)
	content = response.content.decode("utf8")
	js = json.loads(content)
	return js
	
def printinfo(js):
	os.system('cls')
	print("\nYour new identity is:")
	print(js["results"][0]["name"]["first"] + " " + js["results"][0]["name"]["last"])
	print("Your new credentials are:")
	print(js["results"][0]["email"] + "\n" + "Your password is: " + js["results"][0]["login"]["password"])
	print("And if you need a new username too: " + js["results"][0]["login"]["username"] + "\n")
	
main()
