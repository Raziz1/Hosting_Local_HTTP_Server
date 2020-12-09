#!/usr/bin/env python3
#====================Import Libraries====================
import serial
import time
import requests
import json
import datetime
import re
from bs4 import BeautifulSoup
import os
import sys
import threading
from http.server import HTTPServer, CGIHTTPRequestHandler
import webbrowser
import subprocess


#====================Variables====================
#Snow Day predictor Variables
zip_code = XXXXX
URL = "https://www.snowdaycalculator.com/prediction.php?zipcode="+zip_code+"&snowdays=0&extra=-0.4&"
res = requests.get(URL)
html_page = res.content
soup = BeautifulSoup(html_page, 'html.parser')

# Get tomorrows date
date_tomorrow = datetime.date.today() + datetime.timedelta(days=1)
set_time = datetime.datetime.now()

# Get OSTA
URL1 = "http://www.ottawaschoolbus.ca/"
res1 = requests.get(URL1)
html_page1 = res1.content
soup1 = BeautifulSoup(html_page1, 'html.parser')

#====================BUS STATUS====================
def busStatus():
    try:
        #osta_status = soup1.find("h4", attrs={"class": "alert"}).get_text()  # get_text() strips the HTML tags
        osta_status = soup1.find("div", attrs={"class": "light red"})
        if osta_status==None:
            osta_status = soup1.find("div", attrs={"class": "light yellow"})
            if osta_status==None:
                osta_status = soup1.find("div", attrs={"class": "light green"})
                osta_status = "green"
            else:
                osta_status="yellow"
        else:
            osta_status="red"
                
        #print(osta_status)
        return osta_status
    except:
        osta_status = "Failed"
        return osta_status
    
#====================SNOW DAY PREDICTOR====================
def getPredictor():
    # Gets tomorrows date and prints it like the following: 20201101
    snowDate = ''.join((str(date_tomorrow.year), str(date_tomorrow.month), str(date_tomorrow.day).zfill(2)))
    try:
        # Get the text under the following html tag
        gdp_table = soup.find("table", attrs={"class": "prediction"})
        gdp_data = gdp_table.getText
        data_str = str(gdp_data)  # Convert the text to string

        # Find the string containg the prediction percentage
        for item in data_str.split("\n"):
            if "theChance[" + snowDate + "]" in item:
                # print(item.strip())
                # Strip the item and remove unnecessary strings
                s = item.strip()
                s = s.replace("theChance[" + snowDate + "] = ", "")
                s = s.replace("//PREDICTION", "")
                s = s.replace(";", "")
                s = s.replace("\t", "")
                # print(s)
                # Convert and round the float
                s = float(s)
                s = round(s)
                # print(s)
                # The predictor can return numbers larger than 100 and smaller 0 so round those so round them
                if s < 0:
                    s = 0
                elif s > 100:
                    s = 100
                return s
    except:
        print("error")
        return s

#====================MAIN FUNCTION====================
if __name__=='__main__':
    date_tomorrow = datetime.date.today() + datetime.timedelta(days=1)  # Get the current date
    set_time = datetime.datetime.now()  # Get the current time
    get_time = set_time.strftime("%H:%M")  # Get the only the hours and minutes
    
    percentage = getPredictor()
    status = busStatus()
    
	#Write the data to a seperate text file
	# The included spaces and line breaks are for the website to read so you can ignore those for now
    f = open ("scrapeddata.txt", "w")
    if (percentage<10):
        f.write("  "+str(percentage)+","+status+"\n")
    elif (percentage>=10 and percentage<=99):
        f.write(" "+str(percentage)+","+status+"\n")
    else:
        f.write(str(percentage)+","+status+"\n")
    f.close()
    
	#Read the data and print it
    f=open("scrapeddata.txt", "r")
    print(f.read())
    
	#Turn on the display
    subprocess.call('xset dpms force on', shell=True)
    
    # Make sure the server is created at current directory
    os.chdir('.')
    print("FOUND DIRECTORY")
    
    #Create server object listening to the port 8000
    server_object = HTTPServer(server_address=('',8000),RequestHandlerClass=CGIHTTPRequestHandler)
    print("CREATED SERVER")
    
    #Start the server on a different thread otherwise it will deadlock
    server_thread =  threading.Thread(target=server_object.serve_forever)
    server_thread.daemon=True
    print("STARTING")
    server_thread.start()
    
    #Open the url in the webbrowser
    webbrowser.open_new("http://localhost:8000")
    
    #Wait 10 seconds
    time.sleep(10)
    print("CLOSING")
    #Close and cleanup the server
    server_object.shutdown()
    sys.exit(0)
    
    
    
    