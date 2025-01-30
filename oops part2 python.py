# del keyboard


# class student:
#     def __init__(self,name):
#         self.name=name

# s1=student("ishaan")
# print(s1.name)
# del s1.name
# print(s1.name)

#private
# class account:
#     def __init__(self,acc,password):
#         self.account=acc
#         self.__password=password
#     def reset_pass(self):
#         print(self.__password)

# acc1=account("1234","anvde")

# print(acc1.account)

# acc1.reset_pass()
# print(acc1.__password)

# #private attribute
# class person:
#     __name="anounymous"
#     def __hello(self):
#         print("hello perosn")
#     def welcome(self):
#         self.__hello()

# p1=person()
# print(p1.__name)
# print(p1.welcome())

# inheritance

#single inheritance

# class car:
#     @staticmethod
#     def start():
#         print("car started...")
#     @staticmethod
#     def stop():
#         print("car stopped")
    
# class toyotacar(car):
#     def __init__(self,name):
#         self.name=name


# car1=toyotacar("fortuner")
# car2=toyotacar("hiliux")
# print(car1.start())


# # multilvel inheritance

# class fortuner(toyotacar):
#     def __init__(self,type):

#         self.type=type

# p1=fortuner("diesel")
# print(p1.start())

# #multiple inheritance


# class a:
#     vara="welcome to class a"
# class b:
#     varb="welcome to class b"
# class c(a,b):
#     varc="welcome to class c"


# c1=c()
# print(c1.varc)
# print(c1.varb)

# #super method

# class car:
#     def __init__(self,type):
#            self.type=type
#     @staticmethod
#     def start():
#          print("car started")
#     @staticmethod
#     def stop():
#          print("stop")

# class toyotacar(car):
#      def __init__(self,name,type):
#           self.name=name
#           super().__init__(type)


# car1=toyotacar("aloo","hybrid")
# print(car1.type)
# car1.stop()
# print(car1.type)


# # class mehods 
# class peroson:
#     name="ishaan"

#     def changename(self,name):
#         #if we write self.name then name of perosn will no be changed to rahul kumar 
#         #for tto change name of class attribute
#         peroson.name=name
    
# p1=peroson()
# p1.changename("rahul kumar")
# print(p1.name)

# # another mwthod
# class peroson:
#     name="ishaan"

#     def changename(self,name):
#         self.__class__.name="rahul"
#         #self__class__.person.
# print(p1.name)


# class methods

# class perosn:
#     @classmethod
#     def changename(cls,name):
#         cls.name=name

# p1=perosn()
# p1.changename("rahul")
# print(p1.name)
# print(perosn.name)

# properthy decorator
# class student:
#     def __init__(self,phy,chem,maths):
#         self.phy=phy
#         self.chem=chem
#         self.maths=maths
#         self.percentage=(self.phy+self.chem+self.maths)/3

# std1=student(98,97,99)
# print(std1.percentage)
# std1.phy=86
# print(std1.percentage)

# # for this ambiquity we use property decorator as you can see variable defined in function does not change as other attributes changes 
# class student:
#     def __init__(self,phy,chem,maths):
#         self.phy=phy
#         self.chem=chem
#         self.maths=maths
#         self.percentage=(self.phy+self.chem+self.maths)/3      
#     def calc_percentage(self):
#         self.percentage=(self.phy+self.chem+self.maths)/3

# std1=student(98,97,99)
# print(std1.percentage)
# std1.phy=86
# std1.calc_percentage()
# print(std1.percentage)


# best method
# class student:
#     def __init__(self,phy,chem,maths):
#         self.phy=phy
#         self.chem=chem
#         self.maths=maths
#     @property
#     def percentage(self):
#         return self.phy+self.chem
# std1=student(98,97,99)
# print(std1.percentage)
# std1.phy=86
# print(std1.percentage)


# getter and  setter more decoratoe to study


# polymorphism


# print(1+2)#3
# print("apna"+"college")#concatate

# # complex number 
# l=1+3j # j imaginary =iota
# print(type(l))




# class complex:
#     def __init__(self,real,img):
#         self.real=real
#         self.img=img
#     def add(self):
    
#      print(self.real,"i+",self.img,"j")
#     def adding(self,k):
#        new_real=self.real + k.real
#        new_img=self.img+k.img
#        return complex(new_real,new_img)
       
# c=complex(1,2)
# c.add()
# k=complex(2,3)
# k.add()
# l=c.adding(k)
# l.add()


# class complex:
#     def __init__(self,real,img):
#         self.real=real
#         self.img=img
#     def show(self):
    
#      print(self.real,"i+",self.img,"j")
#     def __add__(self,k):
#        new_real=self.real + k.real
#        new_img=self.img+k.img
#        return complex(new_real,new_img)
       
# c=complex(1,2)
# c.show()
# k=complex(2,3)
# k.show()
# # l=c.adding(k)
# # l.add()
# l = c + k
# l.show()

# in + dunder function we acually define + for given numbers

# search more dunder function


# question
# class circle:
#     def __init__(self,radius):
#         self.radius=radius
#     def area(self):
#         print(self.radius*self.radius*3.14)



# circle1=circle(4)
# print(circle1.radius)
# circle1.area()































