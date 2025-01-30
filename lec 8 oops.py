#oops

# #creating class
# class Student:
#     name="ishaan"


# #creating object
# s1=Student()
# print(s1.name)

# s2=Student()
# print(s2.name)



#constructor

# class student:
    
#     def __init__(self,fullname):
#         self.name=fullname
#         print("adding to your world")



# s1=student("karan")
# print(s1.name)

# class car:
#     def __init__(self,fullname):
#         self.paint=fullname
#         print("lki")
        
        

# car1=car("blue")
# print(car1.paint)


# class student:
#     college_name="abc collge"
#     name="anonymous"#class attributes

#     #default constructors
#     # def __init__(self,):
#     #     pass
        

#     #paramertic constructors
#     def __init__(self,name,marks):#obj>>class atr
#         self.name=name
#         self.marks=marks
#         print("adding")



# s1=student("karan")
# print(s1.name)

# attributes

#self.abcd is used to tell us object have diferent

# print(student.college name ) # will give us common data for all student if it is written outside def function

#creating function
# class student:
#     def welcome(self):
#         print("lol")


# s1=student()
# s1.welcome()



# class student:
#     collge_name="abc"

#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks

#     def welcome(self):
#         print("welcome",self.name)
#     def get_marks(self):
#         print(self.marks)
#         return self.marks
# s1=student("karan",90)
# s1.welcome()
# s1.get_marks()


# class student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#     def avg(self):
#         print(int(m+n)/2)


# nam=student("karan","ayush")
# mark=student(97,99)

# l=print(nam.name)
# k=print(nam.marks)
# m=print(mark.name)
# n=print(mark.marks)

# student.avg()



# in classes exteriable variable is not accessible 
# above is the live example of this



# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def avg(self):
#         print(sum(self.marks) / len(self.marks)
# )
#         return sum(self.marks) / len(self.marks)

# # Initializing student instances
# student1 = Student("Karan", [97, 99])
# student2 = Student("Ayush", [88, 90])

# # Printing names and marks
# print(student1.name)
# print(student1.marks)
# print(student2.name)
# print(student2.marks)

# # Calculating and printing averages
# print(student1.avg())
# print(student2.avg())




# class student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks

#     def avg(self):
#         sum=0
#         for val in self.marks:
            
                

#             sum=sum+val
#             print(sum/3)
# s1=student("ishaan",[99,98,99])
# s1.avg()


#s1.name="zero"

# static methods

#Decorators in Python are a very powerful and useful tool for modifying the behavior of functions or classes. A decorator is essentially a function that wraps another function or method, modifying its behavior.

# Here’s a simple example to illustrate how decorators work:

# Example 1: Function Decorator
# This is a decorator function
# def my_decorator(func):
#     def wrapper():
#         print("Something is happening before the function is called.")
#         func()
#         print("Something is happening after the function is called.")
#     return wrapper

# # This is a function we'll decorate
# @my_decorator
# def say_hello():
#     print("Hello!")

# # Calling the decorated function
# say_hello()

# this example:

# my_decorator is the decorator function.

# say_hello is the function being decorated.

# The @my_decorator syntax is a shortcut for applying the decorator to the function.

# When say_hello is called, it actually calls the wrapper function created inside my_decorator, which adds additional behavior before and after calling the original say_hello function.

# When you call say_hello(), the following happens:

# The wrapper function from my_decorator is called.

# It prints "Something is happening before the function is called."

# It then calls func(), which is say_hello. This prints "Hello!".

# Finally, it prints "Something is happening after the function is called."


# abstraxction

#enscapulatin



# class account():
#     def __init__(self,balance,account_no):
#         self.balance=int(balance)
#         self.account_no=int(account_no)
#     def credit(self,l):
        
#         l=self.balance+l
#         print(l)

#     def debit(self):
        
#         m=self.balance-m
#         print(m)

# balance=account(300,999)
# print(balance.balance)




# balance.credit(66)
# balance.debit(8)

# #
# # Yes, you can write `m = self.balance + l` instead of `self.balance += l`, but they serve different purposes. Here’s a breakdown:

# # - `self.balance += l` is a shorthand operation that updates `self.balance` directly by adding `l` to it. It modifies the original `self.balance`.

# # - `m = self.balance + l` assigns the sum of `self.balance` and `l` to a new variable `m`. It does not change `self.balance`.

# # Here's how each approach would look in your `credit` method:

# # ### Using `self.balance += l`:
# # ```python
# # def credit(self):
# #     l = int(input("Enter your amount: "))
# #     self.balance += l  # Update the balance directly
# #     print("Updated balance:", self.balance)
# # ```

# ### Using `m = self.balance + l`:
# ```python
# def credit(self):
#     l = int(input("Enter your amount: "))
#     m = self.balance + l  # Create a new variable 'm'
#     print("New balance calculation:", m)
#     # Note: This does not update self.balance
# ```

# If you use `m = self.balance + l`, you need to also update `self.balance` if you want to maintain the account's current balance. Here's a combined approach:

# ```python
# def credit(self):
#     l = int(input("Enter your amount: "))
#     self.balance += l
#     print("Updated balance:", self.balance)
# ```

# This way, `self.balance` is updated, and the balance is reflected correctly when you print it.

# It's all about what you need: if you want to update the balance directly, use `self.balance += l`. If you want to calculate a new balance without updating the existing one, use `m = self.balance + l`. 😃

# class Account:
#     def __init__(self, balance, account_no):
#         self.balance = int(balance)
#         self.account_no = int(account_no)

#     def credit(self):
#         l = int(input("Enter your amount: "))
#         self.balance += l
#         print("Updated balance:", self.balance)

#     def debit(self):
#         m = int(input("Enter your amount: "))
#         if m <= self.balance:
#             self.balance -= m
#             print("Updated balance:", self.balance)
#         else:
#             print("Insufficient balance")

# # Create an instance of the Account class
# my_account = Account(300, 999)
# print("Initial balance:", my_account.balance)

# # Call the credit and debit methods
# my_account.credit()
# my_account.debit()



# class acount:
#     def __init__(self,bal,acc):
#         self.balance=bal
#         self.account_no=acc
#     def debit(self,amount):
#         self.balance-=amount
#         print(amount)

#     def credit(self,amount):
#         self.balance+=amount
#         print(amount)

# s1=acount(300,4000)
# print(s1.balance)
# print(s1.account_no)


# s1.credit(50)