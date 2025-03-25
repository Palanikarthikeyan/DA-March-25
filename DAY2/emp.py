'''about emp appln'''
class enrollment:
    '''about enrollment class'''
    def __init__(self,a1,a2,a3):
        '''this is initialization block'''
        self.name = a1
        self.dob = a2
        self.place = a3
        print('Enrollment is done')
    def f2(self):
        '''this is f2 method definition'''
        print(f'Emp name is:{self.name} DOB:{self.dob} City:{self.place}')
    def f3(self,a):
        '''f3 method required single argument'''
        self.place = a
        print(f'{self.name} working city is updated')

