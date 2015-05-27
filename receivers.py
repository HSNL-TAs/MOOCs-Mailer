import re
import csv
from templates.final_notify import (NOTIFY_TEMPLATE_UNDER_NINETY,
                                    NOTIFY_TEMPLATE_EXCEED_NINETY)

EMAIL_REGEX = re.compile('([\w\-\.]+@(\w[\w\-]+\.)+[\w\-]+)')

def get_email_from_csv(filename, score_th=0):
    email_list = []
    TO_ADDRESSES = ()

    with open(filename, 'rb') as csvfile:
        for row in csv.reader(csvfile):
            if EMAIL_REGEX.match(row[1]):
                if float(row[-1]) > score_th:
                    TO_ADDRESSES = TO_ADDRESSES + (row[1], )
                else:
                    # We don't care final socre < 0
                    pass

    return TO_ADDRESSES

def get_scores_str(email, filename):
    if not EMAIL_REGEX.match(email):
        print 'Email invalid'
        return None

    with open(filename, 'rb') as csvfile:
        for row in csv.reader(csvfile):
            # This for loop is making null data to 0
            for i in range(2, len(row)):
                if row[i] == '':
                    row[i] = '0'

            if email in row[1]:
                return ', '.join(row[1:])

def under_ninety(email, filename):
    if not EMAIL_REGEX.match(email):
        print 'Email invalid'
        return None

    with open(filename, 'rb') as csvfile:
        for row in csv.reader(csvfile):
            if email in row[1]:
                return True if float(row[-1]) <= 90.0 else False

def make_notify(email, filename):
    under = under_ninety(email, filename)

    if under:
        return NOTIFY_TEMPLATE_UNDER_NINETY % get_scores_str(email, filename)
    else:
        return NOTIFY_TEMPLATE_EXCEED_NINETY % get_scores_str(email, filename)


if __name__ == '__main__':
    filename = './Final_scores/MOOCS_students_final.csv'
    print len(get_email_from_csv(filename))
    print get_email_from_csv(filename)
    print get_scores_str('a901002666@hotmail.com', filename)
    print under_ninety('s103062648@m103.nthu.edu.tw', filename)
    # print get_scores_str('ireri339@gmail.com', filename)
    # print make_notify('ireri339@gmail.com', filename)
