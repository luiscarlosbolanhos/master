# -*- coding: utf-8 -*-
class Student:
    number_of_students = 0
    
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname
        Student.number_of_students += 1
        
    def get_fullname(self):
        fullname = self.name + " " + self.lastname
        return fullname

andres = Student("Andres", "Lopez")
print "The fullname of student is " + andres.get_fullname()

pablo = Student("Pablo","Salas")
print "Number of student is " + str(pablo.number_of_students)

student_list = []
student_list.append(andres)
student_list.append(pablo)

for est in student_list:
    print "fullname: " + est.get_fullname() +" #: " + str(est.number_of_students)
