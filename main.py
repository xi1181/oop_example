class Student:
    def __init__(self, n, a, s, friend):
        self.name = n
        self.age = a
        self.school = s
        self.friend = friend

    def getdetails(self):
        print(self.name)
        print(self.age)
        print(self.school)

    def newyear(self):
        self.age += 1

    def changeschool(self, newschool):
        self.school = newschool

    def whoismyfriend(self):
        print(self.friend.name)


studentlist = []
studentlist.append(Student("Hubert", 24, "Maris Stella High School", 0))
studentlist.append(Student("Chin Xi", 13, "Anglican High", studentlist[0]))
studentlist.append(Student("Daven", 13, "Yusof Ishak Sec", studentlist[1]))

for index in range(len(studentlist)):
    if index == 0:
        continue
    print(studentlist[index].whoismyfriend())