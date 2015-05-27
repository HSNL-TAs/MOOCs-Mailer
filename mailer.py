# -*- coding: utf-8 -*-

# http://tomekwojcik.github.io/envelopes/#short-example
from settings import LOGIN_ONE, PASSWORD_ONE, LOGIN_TWO, PASSWORD_TWO
from receivers import get_email_from_csv, make_notify

from envelopes import Envelope, GMailSMTP

FILENAME = './Final_scores/MOOCS_students_final.csv'

TO_ADDRESSES = get_email_from_csv(FILENAME)
# TO_ADDRESSES = ('ireri339@gmail.com', 'a901002666@hotmail.com', 's103062648@m103.nthu.edu.tw')

# print TO_ADDRESSES

confirm = raw_input('[*] Sent mail to %s (y/n)' % str(TO_ADDRESSES))

if confirm == 'y' or confirm == 'Y':
    for idx, addr in enumerate(TO_ADDRESSES):
        # print make_notify(addr, FILENAME)
        envelope = Envelope(
            from_addr=(u'device@hsnl.cs.nthu.edu.tw', u'MOOCs-Mailer'),
            to_addr=addr,
            subject=u'【清華 MOOCs 2015 電腦網路概論 線上課程期末成績通知】',
            text_body=make_notify(addr, FILENAME)
        )
        # envelope.add_attachment('/Users/bilbo/Pictures/helicopter.jpg')
        print '[*] Sent to %s' % addr
        if idx >= 350:
            # Send the envelope using an ad-hoc connection...
            envelope.send('smtp.googlemail.com', login=LOGIN_ONE, password=PASSWORD_ONE, tls=True)
        else:
            envelope.send('smtp.googlemail.com', login=LOGIN_TWO, password=PASSWORD_TWO, tls=True)
else:
    print "[*] Sent fail"
