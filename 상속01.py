#부모class
class Person:
    def __init__(self, name, phoneNumber):
        self.name = name
        self.phoneNumber = phoneNumber

    def printInfo(self): # f-string
        print(f"Info(Name:{self.name}, Phone Number: {self.phoneNumber})")
#자식
class Student(Person): #상속받음
    def __init__(self, name, phoneNumber, subject, studentID): #변수추가
        #부모생성자 호출
        super().__init__(name, phoneNumber) #부모꺼는 부모가
        self.subject = subject
        self.studentID = studentID
        
    def printInfo(self): # f-string
        print(f"Info(Name:{self.name}, Phone Number: {self.phoneNumber}, Subject: {self.subject}, StudentID: {self.studentID})")


p = Person("전우치", "010-222-1234")
s = Student("이순신", "010-111-1234", "컴공", "991122")
p.printInfo()
s.printInfo()

