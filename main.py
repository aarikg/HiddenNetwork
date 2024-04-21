import os
os.system("pip install scratchattach")
sessionId = ".eJxVkLtuhDAQRf_FdUKwAduh20RIifIoaKKtkB8DeAEbYaPdJMq_x5a22XbOzNGd-4t2D5sVC6AaXT6-fTBKzO8wgNXoDgU3gY2kkoSTR6Upx7RkveB5D6qgmrBCUKJxncPb0Tft8xet2pcTlk1OX9nerRfdRM3sBmPvzRpNjGUY44yUNMNlRJ3Yw9ilEJ3RkVNeEYoZi0ifhB1cF8wCP86mgIcFtpjv4RPO3dFt0-39KPwYlyRnjCgNDHMihMJC57zCQKgimJU9SJpLWpSQ3gMflHOTSfJzFIK-VUqhptREjdIMbGonGGezK_BZC-t8HT5dl__-AeB9bgQ:1ryFoc:1mDcN_Lu6O6zSpj-5sqa_hkrOkM"

import scratchattach as scratch3
from scratchattach import Encoding
import requests, json

api_key = "63f81b36f9ad7beb082dad037aa12b91"

def get_temperature(city_name):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()
    print(city_name)
    print(x)
    if x["cod"] != "404":
        print(x)
        y = x["main"]
        return y["temp"]
    return "error"

f = open("data.txt", "a+")
"""f.write("test.com`hey this is a test file.")
f.write("\neasteregg.com`yup, this is an easter egg. congrats on finding it.")
f.close()"""
f.close()

with open("data.txt", "r") as file:
        for line in file:
            newLine = line.replace("\n","")
            print(newLine.split("`"))

session = scratch3.Session(sessionId, username="xMysticalLegend") 
project = session.connect_project("1005001052")
conn = session.connect_cloud("1005001052")


while True:
    
    mostRecentComment = project.comments(limit=1, offset=0)[0]["content"]
   # print(mostRecentComment)
    if mostRecentComment.startswith("WEBSITE(") and mostRecentComment.endswith(")"):
        #print(mostRecentComment)
        mostRecentComment = mostRecentComment.split(",")
        createWebsite = mostRecentComment[0].split("WEBSITE(")[1]
        createWebsiteData = mostRecentComment[1].split(")")[0]
        #print(createWebsite, createWebsiteData)
        exist = False
        with open("data.txt", "r") as file:
            for line in file:
                newLine = line.replace("\n","")
                #print(newLine.split("`")[0])
                if str(createWebsite) == str(newLine.split("`")[0]):
                    exist = True
        if not exist:
            f = open("data.txt", "a+")
            f.write(f"\n{createWebsite}`{createWebsiteData}")
            f.close()
            print("Website created successfully")
        else:
            print("Website exists")

            


    value = scratch3.get_var("1005001052", "search")
    if value != 0:
         value = Encoding.decode(value)
         with open("data.txt", "r") as file:
            for line in file:
                newLine = line.replace("\n","")
                if value == newLine.split("`")[0]:
                     
                     conn.set_var("result", Encoding.encode(newLine.split("`")[1]))
                     conn.set_var("search", 0)

                     break
    location = scratch3.get_var("1005001052", "location")
    if location != 0:
        
        location = Encoding.decode(location)
        if get_temperature(location) == "error":
            conn.set_var("temperature", 1)
        else:
            conn.set_var("temperature", Encoding.encode(get_temperature(location)))
        conn.set_var("location", 0)

        
              

    print("looping")
                    
