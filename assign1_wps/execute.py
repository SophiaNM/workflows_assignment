# WPS Execute Operation

import requests, os

payload = open(os.path.dirname(os.path.abspath(__file__)) +"\\envelope_coord.xml").read()

wpsServerUrl = "https://gisedu.itc.utwente.nl/student/s6040241/gpw/assignment/assign1_wps/wps.py?"

response = requests.post(wpsServerUrl, data=payload)
print("Content-type: application/json")
print()
print(response.text)
