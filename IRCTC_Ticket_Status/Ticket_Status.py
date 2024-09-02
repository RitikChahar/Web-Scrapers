import json
from bs4 import BeautifulSoup
import re
import requests

def checkPNRStatus(PNRNumber):
    url = f'https://www.confirmtkt.com/pnr-status/{PNRNumber}?'
    header = {
            "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
        }
    response = requests.get(url,headers=header)

    soup = BeautifulSoup(response.content, 'html.parser').find_all('script')
    script = ''
    for i in soup:
        if 'var data' in i.text:
            script = i.text

    passengers_data =  json.loads(str(re.findall(r'(?<=var data =).*?(?=};)', script)[0])+'}')
    output ={
        'PNR':passengers_data['Pnr'],
        'TrainNo':passengers_data['TrainNo'],
        'TrainName':passengers_data['TrainName'],
        'DateOfJourney':passengers_data['Doj'],
        'BookingDate':passengers_data['BookingDate'],
        'Quota':passengers_data['Quota'],
        'From':passengers_data['BoardingStationName'],
        'To':passengers_data['ReservationUptoName'],
        'Class':passengers_data['Class'],
        'ChartPrepared':passengers_data['ChartPrepared'],
        'PassengerCount':passengers_data['PassengerCount'],
        'TicketFare':passengers_data['TicketFare'],
        'Prediction':passengers_data['PassengerStatus'][0]['Prediction'],
        'PredictionPercentage':passengers_data['PassengerStatus'][0]['PredictionPercentage'],
        'Coach':passengers_data['PassengerStatus'][0]['Coach'],
        'Berth':passengers_data['PassengerStatus'][0]['Berth'],
        'BookingStatus':passengers_data['PassengerStatus'][0]['BookingStatus'],
        'CurrentStatus':passengers_data['PassengerStatus'][0]['CurrentStatus'],
        'CoachPosition':passengers_data['CoachPosition'],

    }
    return output

# PNRNumber = '2446866371'
# print(checkPNRStatus(PNRNumber))