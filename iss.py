import json, turtle, urllib.request, time, webbrowser, geocoder 
# pip install geocoder for lat/lon to work

""" Tracks the International Space Station and using the Turtle module
    plots where on earth the Space Station is currently above in relation
    to your own Latitude and Longitude. Needs the geocoder module to be pip installed
    for your lat/long to work. """

def grab_url(url):
    response = urllib.request.urlopen(url)
    result = json.loads(response.read())
    return result


def output(lat, lon):
    # Output Lat/Long to console
    lat = float(lat)
    lon = float(lon)
    print("\nLatitude: " + str(lat))
    print("Longitude: " + str(lon))


def main():
    # Retrieve names of astronauts aboard the ISS right now and own lat, lon
    result = grab_url("http://api.open-notify.org/astros.json")
        

    a = open("iss.txt", "w")    
    a.write("There are currently " + str(result["number"]) + " astronauts on the ISS:\n\n")

    people = result["people"]

    for p in people:
        a.write(p["name"] + " - on board" + "\n")
    # Gets users current location
    g = geocoder.ip('me')
    a.write("\nYour current Lat/Long is: " + str(g.latlng))
    a.close()
    webbrowser.open("iss.txt") # writes the current Astronauts onboard the ISS to text file

    # World map for Turtle to do it's thing
    screen = turtle.Screen()
    screen.setup(1280, 720)
    screen.setworldcoordinates(-180, -90, 180, 90)
    # Load world image map for Turtle
    screen.bgpic("res/world.gif")
    screen.register_shape("res/iss.gif")
    iss = turtle.Turtle() # creates Turtle
    iss.shape("res/iss.gif") # Turtle is shape of ISS
    iss.setheading(45)
    iss.penup()

    while True:
        result = grab_url("http://api.open-notify.org/iss-now.json")

        # Extract ISS location
        location = result["iss_position"]
        lat = location["latitude"]
        lon = location["longitude"]

        output(lat, lon)
        
        # Update the ISS location on map
        iss.goto(float(lon), float(lat))
        # Refresh every 5 secs
        time.sleep(5)


if __name__ == '__main__':
    main()