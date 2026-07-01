#Constructors in python (__init__)
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
s1= Student("Clement",25)

print(s1.name)
print(s1.age)


#INFORMAL REPRESENTATIONIn Python, the __str__() method is a special method used to define an informal or human-readable string representation of an object. It’s what gets called when you use print() on an object, or when you convert it to a string with str().
class Student:
     def __init__(self,name):
         self.name=name
     def __str__(self):
         return f"student: {self.name}"

s= Student("Clement")
print(s)


 #FORMAL REPRESENTATION The __repr__() method in Python defines the formal string representation of an object. It’s intended for developers and debugging, not end users. The idea is that __repr__() should return a string that is unambiguous and, ideally, one that could be used to recreate the object if passed back into Python.
class Student:
     def __init__ (self,name):
         self.name=name
     def __repr__(self):
         return f"student: {self.name}"
s= Student("Clement")
print(s)



#LENGTH METHOD The __len__() method in Python is another special method that lets you define how the built-in len() function should behave for your custom objects.
class Playlist:
    def __init__(self,songs):
        self.songs=songs
    def __len__(self):
        return len(self.songs)
p=Playlist(["song1","song2","song3"])
print(p)
print(len(p))


#EQUALITY COMPARISON The __eq__() method in Python is a special method that defines how objects of your class should be compared for equality using the == operator. By default, == compares whether two variables point to the same object in memory. But with __eq__(), you can customize what “equal” means for your class.
class Student:
    def __init__(self,student_id):
        self.student_id=student_id
    def __eq__(self,other):
        return self.student_id==other.student_id
s1= Student(101)
s2= Student(101)
print(s1==s2)



#OPERATOR OVERLOADING  in Python means redefining how built-in operators (like +, -, *, etc.) behave when applied to your custom objects. This is done by implementing special methods (dunder methods) in your class. It allows your objects to act more like native Python types.
#ADDITION
class Vector:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self,other):
        return Vector(
            self.x+other.x,self.y+other.y
        )
    def __str__(self):
        return f"x: {self.x}, y: {self.y}"
v1 = Vector(2,3)
v2 = Vector(4,5)
print(v1+v2)
#SUBTRACTION
class Vector:
    def __init__(self,x,):
        self.x=x
    def __sub__(self,other):
        return Vector(self.x-other.x)
    def __str__(self):
        return str(self.x)
v1 = Vector(10)
v2 = Vector(3)
print(v1-v2)


#MULTIPLICATION
class Number:
    def __init__(self,value):
        self.value=value

    def __mul__(self,other):
            return Number(self.value*other.value)

    def __str__(self):
        return f"number: ({self.value})"
n1 = Number(5)
n2 = Number(4)
print(n1*n2)


#ITEM ACCESS The __getitem__() method in Python lets your custom objects support indexing and item access just like lists, tuples, or dictionaries. It’s what gets called when you use square brackets [] on an object.
# ITEMS ACCESS__GETITEM__()
#EXAMPLE
class Grades:
    def __init__(self):
        self.data = [85, 90, 78]
    def __getitem__(self, index):
        return self.data[index]
g = Grades()
print(g[0])
print(g[1])


#7 ITEM ASSIGNMENT:__SETITEM__()
class Grades:
    def __init__(self):
        self.data = [85, 90, 78]
    def __setitem__(self, index, value):
        self.data[index] = value
g = Grades()
g[1] = 100
print(g.data)


#8 MEMBERSHIP TESTING The __contains__() method in Python is a special method that lets your custom objects support the in keyword for membership testing. It’s what gets called when you write item in obj.
#MEMBERSHIP TESTING:__CONTAINS__()...
#EXAMPLE
class Course:
    def __init__(self):
        self.students = ["Ella", "Sandra", "Joe"]
    def __contains__(self, student):
        return student in self.students
c = Course()
print("Joe" in c)
print("Clement" in c)



#9 CALLABLE OBJECTS The __call__() method in Python is what makes an object callable — meaning you can use it like a function. If a class defines __call__(), then instances of that class can be invoked with parentheses () just like regular functions.
#CALLABLE OBJECT:__CALL__()
#EXAMPLE
class Multiplier:
    def __init__(self, factor):
        self.factor = factor
    def __call__(self, number):
        return number * self.factor
double = Multiplier(2)
print(double(10))
#double now behaves like a function



#10 ITERATION SUPPORT In Python, iteration support is provided by two special methods: __iter__() and __next__(). Together, they allow your custom objects to be used in loops (for ... in ...) and other iterable contexts.
#ITERATION SUPPORT:__()AND__NEXT__()
class Counter:
    def __init__(self, limit):
        self.limit = limit
        self.current = 1
    def __iter__(self):
        return self
    def __next__(self):
        if self.current > self.limit:
         raise StopIteration
        value = self.current
        self.current += 1
        return value
for num in Counter(5):
    print(num)



#11 BOOLEAN EVALUATION The __bool__() method in Python defines how your custom objects behave when evaluated in a Boolean context — for example, inside an if statement or when passed to bool().
class BankAccount:
    def __init__(self,balance):
        self.balance = balance
    def __bool__(self):
        return self.balance > 0
account = BankAccount(500)
if account:
    print("Account is active")



#DESTRUCTOR METHOD he __del__() method in Python is known as the destructor. It’s a special method that gets called when an object is about to be destroyed — usually when it goes out of scope or the program ends. Its main purpose is to allow you to clean up resources (like closing files, releasing memory, or disconnecting from a network) before the object is removed from memory.
#DESTRUCTOR METHOD:__DEL__()
class FileHandler:
    def __init__(self, filename):
        self.filename=filename
        print("File opened")
    def __del__(self):
        print("File closed")
f=FileHandler("data.txt")