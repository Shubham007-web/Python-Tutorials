
# data / varibles
pi = 3.1428

g = 9.8


# functions
def greet(name):
    return f'Hello {name}! How are you?'

def add(a,b):
    return a + b


# class
class student :

    def __init__(self, name, skills):
        self.name = name
        self.skills = skills

    def info(self):
        print(f'Name : {self.name}')
        print(f'Skill : {self.name} know {self.skills}')



if __name__ == '__main__':
    print('This code ruuning from orginal file')

else :
    print('The codes import from another file')
