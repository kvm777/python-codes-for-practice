import smtplib
# not Done...

try:
    server = smtplib.SMTP("smtp.gmail.com", 587 )
    server.starttls()
    
    '''
    to get the LOGIN password code. we need to follow the steps below....

    1. open gmail settings -> more settins -> Forwarding and POP/IMAP -> Enable IMAP -> save changes
    2. turn on the 2 step verification 
    3. search app passwords in google account.. -> create app -> and create code -> 
        copy the code and use it as password..
    '''

    server.login("koradamahesh2000@gmail.com", "eoolrwwlumzzefaw")
    server.sendmail("koradamahesh2000@gmail.com", "venkatamaheshkorada2000@gmail.com", "this mail is from python")
    server.close()
    print("mail sent")
except:
    print(smtplib.SMTPConnectError)


