import smtplib
import string
 
SUBJECT = "INCOMING COMM"
TO = "********@messaging.sprintpcs.com"
FROM = "instantiate@whatever.org"
i = 0
while i < 5:
	FROM = "ANYTHINGBUTYOURNAME" + str(i) + "@spamhous.org"
	text = "ALL HAIL THE SPAM GOD."
	BODY = string.join((
        	"From: %s" % FROM,
        	"To: %s" % TO,
        	"Subject: %s" % SUBJECT ,
        	"",
        	text
        	), "\r\n")
	server = smtplib.SMTP(HOST)
	server.sendmail(FROM, [TO], BODY)
	server.quit()
