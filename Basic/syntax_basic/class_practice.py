"""
单继承
"""


class Person:
    """父类，基类"""
    Name = 'Person'

    def sleep_info(self):
        print('I am sleeping')

class stu_info(Person):
    """
    子类、基类
    """
    school = 'School'
    def learning_info(self):
        print(self.Name)
        self.sleep_info()
        print('I am learning')


daniel = stu_info()
print(daniel.Name)
daniel.learning_info()

