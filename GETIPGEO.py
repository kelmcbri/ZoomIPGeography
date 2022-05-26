import urllib.request
from urllib.request import urlopen
import json
from datetime import date
import time
usOnly = False


#Create and open file to receive ip address country information
today = date.today()
theFile = (str(today) + "_ZoomIPAddresses.csv")
geoIpFile = open(theFile,"w")
thisline = ('ZoomIP , CountryOfOrigin\n')

#Zooms link to most current IP addresses for Zoom Meetings Only
zoomMeetingsLink = "https://assets.zoom.us/docs/ipranges/ZoomMeetings.txt"
#Parse the zoom link for Zoom Meeting ip address list
f = urlopen(zoomMeetingsLink)
zoomFile = f.read()
t = zoomFile.decode("utf-8")
zoomList = list(t.split())

#Request information about a particular IP address
for eachIp in zoomList:
    ipwhois = 'http://ipwhois.app/json/' + str(eachIp)
    req = urllib.request.Request(ipwhois)
    with urllib.request.urlopen(req) as response:
        the_page = response.read()

    #Convert the response of ip country info to python dictionary
    res_dict = json.loads(the_page)
    dictionary_items = res_dict.items()
    #Parse the python dictionary for ip and country information
    for k,v in dictionary_items:
        if str(k) == "ip":
            ip = str(v)
        if str(k) == "country":
            country = str(v)
    #write the ip country info line to file
    if usOnly:
        if  country.upper() == 'UNITED STATES':
            thisline = (ip + ',' + country + '\n')
            print(thisline)
            geoIpFile.write(thisline)
    if not usOnly:
        thisline = (ip + ',' + country + '\n')
        print(thisline)
        geoIpFile.write(thisline)
    time.sleep(1)

#Close the ip country info file
geoIpFile.close()
print('program run complete')
