class private_demo():
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def display_name(self):
        print "Display name :", self.name

    def display_age(self):
        print "Display age :", self.__age

    def __authunticated_data(self):
        print "Name %s and %d" %(self.name, self.__age)

if __name__ == "__main__":
    obj = private_demo("Arun", 25)
    obj.display_name()
    obj.display_age()
    obj._private_demo__authunticated_data()


