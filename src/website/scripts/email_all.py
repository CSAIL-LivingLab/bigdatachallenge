from header import *
from django.core.mail import send_mail, send_mass_mail

subject = "Update to prediction challenge specification"
text = """Dear %s,

We want to update you on fixes to the prediction challenge.  

We intended to remove 4 hour time spans and ask you to predict the
ridership within the middle two hours (e.g., we remove 1-5pm, you predict 2-4pm).
We neglected to fully describe this and mistakenly asked you to predict 
ridership counts in all 4 hours.

This error has been corrected, and the test files, submission scores, and 
contest descriptions have been updated.  We will keep a list of clarifications 
on each of the contest pages and notify you when anything else changes.

Thank you,
MIT Big Data Challenge
"""

datas = []
for user in User.objects.all():
  msg = text % user.username
  email = (subject, msg, "bigdatachallenge@gmail.com", (user.email,))
  datas.append(email)
totaln = len(datas)

print "email:   %s" % datas[0][3]
print "subject: %s" % datas[0][0]
print 
print "message:"
print datas[0][1]

send = False
if len(sys.argv) > 1:
  if sys.argv[1] == 'send':
    raw_input("mass sending to %s?  ctrl-c to abort!" % len(datas))
    send = True


if send:
  for n, data in enumerate(datas):
    try:
      print "sending to %d of %d: %s" % (n, totaln, data[3][0])
      send_mail(*data, fail_silently=False)
    except Exception as e:
      print "error %s " % e