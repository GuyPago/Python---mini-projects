import smtplib
import datetime

now = datetime.datetime.now()

now+datetime.timedelta(days=10)

server = smtplib.SMTP( "smtp.gmail.com", 587 )
server.starttls()
server.login( 'Pago.Corp.industries@gmail.com', 'Ta112233' )
from_mail = 'Pago.Corp.industries@gmail.com'
to = 'guypago@outlook.com'
# subject = "You've been fired from Pago-Corp."

message = """From: Pago-Corp industries <Pago.Corp.industries@gmail.com>
To: {to} <guypago@outlook.com>
Subject: You've been fired from Pago-Corp

{mail_date}


Dear {to},

This letter is to inform you that as of {date}, we will no longer require your services.
We've enjoyed working with you, but due to {reason}, we have decided to terminate your contract.

All outstanding deliverables should be completed before our contract is officially terminated.
Please note that as of {date} you will no longer have access to our system.

Thank you for all your work over [fire_time - emp_time] days. If you have any questions feel free to reach out at {phone} or {mail}.

Sincerely,
{sender}
""".format(date=(now+datetime.timedelta(days=10)).strftime('%x'),to='ram',mail_date=now.strftime('%c'),
reason='various reasons',phone='0525797331',mail='mail',sender='Guy Taggar, CEO')

# message = ("From: Pago-Corp industries %s\r\n" % from_mail + "To: %s\r\n" % to + "Subject: {} %s\r\n".format(subject) % '' + "\r\n" + body)
server.sendmail(from_mail, to, message)
