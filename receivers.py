import re
import csv
from templates.final_notify import NOTIFY_TEMPLATE

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
            if email in row[1]:
                return ', '.join(row[1:])

def make_notify(email, filename):
    return NOTIFY_TEMPLATE % get_scores_str(email, filename)



if __name__ == '__main__':
    filename = './Final_scores/MOOCS_students_final.csv'
    print len(get_email_from_csv(filename))
    print get_email_from_csv(filename)
    # print get_scores_str('ireri339@gmail.com', filename)
    # print make_notify('ireri339@gmail.com', filename)
