from random import sample


class Sample:
    a = 'Omprakash'

obj = Sample()
obj.a = 'Liza'          # This is changed only object/instance attribute
# Sample.a = 'Liza'     # This is changed class attribute

print(Sample.a)
print(obj.a) 