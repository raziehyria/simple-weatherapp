#use good weather api
#format code with example api, aka philly location
#optimize the code to allow user city input
#prompts user input for city, and calls on functions to answer multiple questions
#additional acquiries defined for userability and


import requests
import json

#holds API KEY and empty string for later user input
apiKey = "48f89bf7b90f351925c8e98c64820f27"
cityName =''
#holds incomplete api url
baseweatherURL= 'https://api.openweathermap.org/data/2.5/weather?'

#def pulls in the url, and reads and stores the data
def weatherApp():
    completeURL= baseweatherURL + "q=" +cityName+ "&appid=48f89bf7b90f351925c8e98c64820f27"
    response = requests.get(completeURL)
    rawData = response.json()
    print(rawData)

#asks the user for their name for the fun
#while loop that keeps running until the user  wants weather forcast, otherwise stop
userName=input("Please enter your name: ")
while (input("Would you like to see your local weather? [Y/N]: ") == 'y'):
    userCity =input("Please enter the name of your city: ")
    cityName = cityName + userCity
    print("Searching....")
    weatherApp()

    #if its a valid url then locate city and print temps


    #if the url doesnt work, catch and print error, and give chance to run again

else:
    print("Thank you ", userName, " for using our weather app! Come again!")

#print the currently temp, humidity,
