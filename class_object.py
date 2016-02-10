class Student:
    RollNo = 0

    def __init__(self, std_id, name):
        self.id = std_id
        self.name = name
        Student.RollNo += 1 # place the + operator properly

    def displayStudent(self):
        print "ID: %d \t Name: %s" %(self.id, self.name)


if __name__ == "__main__":

    std0 = Student(500, "Arun")
    std1 = Student(501, "Krishna")
    std2 = Student(502, "Hari")
    std3 = Student(503, "Gana")


    std0.displayStudent()
    std1.displayStudent()
    std2.displayStudent()
    std3.displayStudent()
    print "Total Student Count %d" % Student.RollNo

    if hasattr(std0, "name"):
        data = getattr(std0, "name") # it does not print it. so have to capture and then print it .
        print data

        setattr(std0,"name","arunkamaraj")

        data = getattr(std0, "name")
        print data





    # print Student.__name__
    #
    print "---------------------------?"
    print std0.__class__.__name__
    print std0.__class__.__module__ # which is eqUAL to __name__
    print std0.__class__.__doc__
    print std0.__class__.__dict__

