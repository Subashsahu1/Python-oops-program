# Instance methods
''' If we use self variable in method implementation then that method is called instance methods.

# Generally we take input data from different way:

# 1. Taking input data from manually / directly.
# 2. Taking input from user using input function.
# 3. Taking input data from database table.
# 4. Taking input data from file.
'''

# 1. Taking input data from manually / directly.
'''
class student:
    iname = 'NTH'
    location = 'Hyd'

    def __init__(self, name, mark):
        self.name = name
        self.mark = mark

    def grade(self):
        print('** Welcome to {} institute**'.format(student.iname))
        if self.mark >= 0 and self.mark < 35:
            print('Hello {},you are failed in the exam'.format(self.name))
        elif self.mark >= 35 and self.mark <= 100:
            print('Hello {},you are passed in the exam'.format(self.name))
        else:
            print('Hello {},you have entered invalid mark'.format(self.name))
        print()

s1 = student('omm', 110)
s1.grade()

s2 = student('Sunil', 30)
s2.grade()
'''

# 2. Taking input from user using input function.

'''
class student:
    iname = 'NTH'
    location = 'Hyd'

    def __init__(self, name, mark):
        self.name = name
        self.mark = mark

    def grade(self):
        print('** Welcome to {} institute**'.format(student.iname))
        if self.mark >= 0 and self.mark < 35:
            print('Hello {},you are failed in the exam'.format(self.name))
        elif self.mark >= 35 and self.mark <= 100:
            print('Hello {},you are passed in the exam'.format(self.name))
        else:
            print('Hello {},you have entered invalid mark'.format(self.name))
        print()

n = int(input('How many students ? '))

for i in range(n):
    name = input('Enter your name: ')
    mark = int(input('Enter your mark: '))
    s = student(name, mark)
    s.grade()
'''

# 3. Taking input data from database table.

'''
class student:
    iname = 'NTH'
    location = 'Hyd'

    def __init__(self, name, mark):
        self.name = name
        self.mark = mark

    def grade(self):
        print('** Welcome to {} institute**'.format(student.iname))
        if self.mark >= 0 and self.mark < 35:
            print('Hello {},you are failed in the exam'.format(self.name))
        elif self.mark >= 35 and self.mark <= 100:
            print('Hello {},you are passed in the exam'.format(self.name))
        else:
            print('Hello {},you have entered invalid mark'.format(self.name))
        print()


import pymysql
connection = pymysql.connect(host = 'localhost', db = 'pythonoopsdb', user = 'root', passwd = 'root')
c =  connection.cursor()
c.execute("select * from studentsdata;")
data = c.fetchall()

for i in data:
    name = i[1]
    mark = i[2]
    s = student(name, mark)
    s.grade()
'''

# 4. Taking input data from file.

'''
from os import read
class student:
    iname = 'NTH'
    location = 'Hyd'

    def __init__(self, name, mark):
        self.name = name
        self.mark = mark

    def grade(self):
        print('** Welcome to {} institute**'.format(student.iname))
        if self.mark >= 0 and self.mark < 35:
            print('Hello {},you are failed in the exam'.format(self.name))
        elif self.mark >= 35 and self.mark <= 100:
            print('Hello {},you are passed in the exam'.format(self.name))
        else:
            print('Hello {},you have entered invalid mark'.format(self.name))
        print()


a = open("note.txt", 'r')
b = a.readlines()

for i in b:
    c = i.split(',')
    name = c[1]
    mark = int(c[2])
    s = student(name, mark)
    s.grade()
'''



