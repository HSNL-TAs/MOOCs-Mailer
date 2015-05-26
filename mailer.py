# -*- coding: utf-8 -*-

# http://tomekwojcik.github.io/envelopes/#short-example
from settings import LOGIN, PASSWORD
from receivers import get_email_from_csv, make_notify

from envelopes import Envelope, GMailSMTP

FILENAME = './Final_scores/MOOCS_students_final.csv'

# TO_ADDRESSES = get_email_from_csv(FILENAME)
TO_ADDRESSES = ('ireri339@gmail.com', )

# print TO_ADDRESSES

for addr in TO_ADDRESSES:
    # print make_notify(addr, FILENAME)
    envelope = Envelope(
        from_addr=(u'device@hsnl.cs.nthu.edu.tw', u'MOOCs-Mailer'),
        to_addr=addr,
        subject=u'【清華 MOOCs 2015 電腦網路概論 線上課程期末成績通知】',
        text_body=make_notify(addr, FILENAME)
    )
    # envelope.add_attachment('/Users/bilbo/Pictures/helicopter.jpg')
    print 'Sent to %s' % addr
    # Send the envelope using an ad-hoc connection...
    envelope.send('smtp.googlemail.com', login=LOGIN, password=PASSWORD, tls=True)
