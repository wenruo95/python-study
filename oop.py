#!/usr/bin/python
# encoding: utf-8

if __name__ == "__main__":
    print("main")
else:
    print("another")

# Person
class Person:
    """人员信息"""
    name = ""
    age = 0

    def __init__(self, name = "", age = 0) :
        self.name = name
        self.age = age

    def __str__(self) :
        return "这里重载了__str__专有方法," + str({"name" : self.name, "age" : self.age})

    def set_age(self, age) :
        self.age = age

class Account:
    """账户信息"""
    __balance = 0
    __total_balance = 0

    def balance(self):
        return self.__balance
    
    def balance_add(self, cost):
        self.__balance  += cost
        self.__class__.__total_balance += cost

    @classmethod
    def total_balance(cls):
        return cls.__total_balance

    @staticmethod
    def exchange(a, b):
        return b, a

# Teacher
class Teacher(Person, Account):
    """教师"""
    def __init__(self, name) :
        super(Teacher, self).__init__(name)

    def get_info(self) :
        return {
            "name" : self.name,
            "age" : self.age,
            "class_name" : __name__,
            "balance" : self.balance(),
        }

    def balance(self) :
        return Account.balance(self) * 1.1

# Student
class Student(Person, Account):
    """学生"""
    _teacher_name = ""

    def __init__(self, name, age = 18) :
        Person.__init__(self, name, age)

    def get_info(self) :
        return {
            "name" : self.name,
            "age" : self.age,
            "teacher_name" : self._teacher_name,
            "balance" : self.balance(),
        }





john = Teacher('John')
john.balance_add(20)
john.set_age(36)  # 子类的实例可以直接调用父类的方法
print("John's info:", john.get_info())
# 学生 Mary
mary = Student('Mary', 18)
mary.balance_add(18)
print("Mary's info:", mary.get_info())
# 学生 Fake
fake = Student('Fake')
fake.balance_add(30)
print("Fake's info", fake.get_info())
# 三种不同的方式调用静态方法
print("john.exchange('a', 'b'):", john.exchange('a','b'))
print('Teacher.exchange(1, 2)', Teacher.exchange(1, 2))
print('Account.exchange(10, 20):', Account.exchange(10, 20))
# 类方法、类属性
print('Account.total_balance():', Account.total_balance())
print('Teacher.total_balance():', Teacher.total_balance())
print('Student.total_balance():', Student.total_balance())
# 重载专有方法
print(fake)













