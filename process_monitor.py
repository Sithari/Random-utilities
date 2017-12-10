import psutil
import sys
from time import sleep
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime


def sendMail(from_address, from_address_pswd, to_address, now):

    htmlbody = ""

    FROM = from_address
    PWD = from_address_pswd
    TO = to_address

    SUBJECT = "Process has died (" + now + ")"

    msg = MIMEMultipart('alternative')
    msg['Subject'] = SUBJECT
    msg['From'] = FROM
    msg['To'] = TO

    # Prepare actual message

    part2 = MIMEText(htmlbody.encode('utf-8'), 'html')
    # Attach parts into message container.
    msg.attach(part2)
    # Send the mail
    smtpserver = smtplib.SMTP("smtp.gmail.com",587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo
    try:
        smtpserver.login(FROM, PWD)
    except smtplib.SMTPAuthenticationError:
        print ("Pswd was wrong for the FROM gmail account. Exiting..")
        exit(0)
    #print (htmlbody)
    smtpserver.sendmail(FROM, TO, msg.as_string())
    smtpserver.quit()


processes = psutil.pids()

for p in processes:
    p = psutil.Process(p)
    if len(p.cmdline()) > 1:
        #print p.cmdline()
        if sys.argv[1] in p.cmdline()[1]:
            print "found process"
            while True:
                if not psutil.pid_exists(p.pid):
                    print "Proccess has died"
                    sendMail("[from email]", "[from email password]", "[dest email]", datetime.now().strftime("%m/%d/%Y %r %z"))
                    exit()
                sleep(5)

print "process not found"
