from Ticket_Status import checkPNRStatus
from email.message import EmailMessage
import ssl
import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

emailData = ''
PNRNumber = ['2446866371','6508105019']
NameOfPassenger = "Ritik Chahar"
for i in PNRNumber:
    data = checkPNRStatus(i)
    emailData =f"""\
    <html>
    <head></head>
    <body bg-color="black">
    <h1>Hello {NameOfPassenger} your booking status for {data['TrainNo']} {data['TrainName']} from {data['From']} to {data['To']} is {data['CurrentStatus']}. </h1>
        Other Details <br>
    <table>   
    <tr><td>Prediction Percentage</td><td>{data['PredictionPercentage']}</td></tr>
    <tr><td>Prediction</td><td>{data['Prediction']}</td></tr>
    <tr><td>Date of Journery</td><td>{data['DateOfJourney']}</td></tr>
    <tr><td>Class</td><td>{data['Class']}</td></tr>
    <tr><td>Coach</td><td>{data['Coach']}</td></tr>
    <tr><td>Berth</td><td>{data['Berth']}</td></tr>
    <tr><td>CoachPosition</td><td>{data['CoachPosition']}</td></tr>
    <tr><td>Booking Status</td><td>{data['BookingStatus']}</td></tr>
    </table>
    </body>
    </html>
        """

    email_sender = 'ritikchahar47@gmail.com'
    email_password = 'blewtqztkpoaqiar'

    email_reciever ='ritikchahar54@gmail.com'
    subject = f"Ticket Status for {data['TrainNo']} {data['TrainName']}"
    body = emailData

    em = MIMEMultipart()
    em['From'] = email_sender
    em['To']= email_reciever
    em['subject'] = subject
    em.attach(MIMEText(emailData, "html"))
    email_string = em.as_string()

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_reciever, em.as_string())

