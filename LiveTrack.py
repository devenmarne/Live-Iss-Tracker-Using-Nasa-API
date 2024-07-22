import json
import turtle
import urllib.request
import time
import webbrowser


url= "http://api.open-notify.org/astros.json"
response= urllib.request.urlopen(url)
result= json.loads(response.read())
file=open("iss.txt", "w")
file.write("There are currently " + str(result["number"]) + " astronauts on the ISS: \n\n")
people = result["people"]
for p in people:
    file.write(p['name'] + "- on board" + "\n")
file.close()
webbrowser.open("iss.txt")



screen=turtle.Screen()
screen.setup(1920, 1080)
screen.setworldcoordinates(-180,-90,180,90)

screen.bgpic("world-map6.gif")
screen.register_shape("iss3.gif")
iss = turtle.Turtle()
iss.shape("iss3.gif")
iss.setheading(45)
iss.penup()

while True:
    url="http://api.open-notify.org/iss-now.json"
    response= urllib.request.urlopen(url)
    result= json.loads(response.read())
    
    location=result["iss_position"]
    lat=location['latitude']
    lon=location['longitude']

    lat=float(lat)
    lon=float(lon)
    print("\n Latitude: " +str(lat))
    print("\n Longitude: " +str(lon))

    #turtle.write("Latitude: " +str(lat),"Longitude: " +str(lon),font=("arial", 20, "normal"), align='center' )

    iss.goto(lon, lat)

    time.sleep(2)
    
