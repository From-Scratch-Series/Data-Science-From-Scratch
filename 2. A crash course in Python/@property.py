class Employee:
    def __init__(self, first, last) -> None:
        self.first = first
        self.last = last
        self.email = f'{first}.{last}@gmail.com'
    
    def fullname(self):
        return self.first + self.last
    

emp1 = Employee('atul', 'shah')
emp1.first = 'aadarsh'

print(emp1.email) #didn't change
print(emp1.fullname()) #changed


class UpdatedEmployee:
    def __init__(self, first, last) -> None:
        self.first = first
        self.last = last
        # self.email = f'{first}.{last}@gmail.com'
    
    @property
    def email(self):
        return f'{self.first}.{self.last}@gmail.com'
    
    @property
    def fullname(self):
        return self.first + self.last
    
    @fullname.setter
    def fullname(self, name):
        self.first, self.last = name.split(' ')

    @fullname.deleter
    def fullname(self):
        self.first = ''
        self.last = ''
        print('deleted name')

print('-'*50)
emp1 = UpdatedEmployee('atul', 'shah')
emp1.first = 'aadarsh'

print(emp1.email) #changed
print(emp1.fullname)#changed

emp1.fullname = 'Albert Einstein'
print(emp1.fullname)
print(emp1.email)

del emp1.fullname
# print(emp1.fullname)#deleted