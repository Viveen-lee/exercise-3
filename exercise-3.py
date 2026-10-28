# question 1
def Greet():
    print("Hello, world!")

Greet()

# question 2
def personalized_greeting(name):
    print("hello, " + name + ", how are you?")

personalized_greeting("Viveen")

# question 3
def square(num):
  return num**2

print(square(5))

# question 4
def rectangle_area(length, width):
    return "area of rectangle is: " + str(length * width)

print(rectangle_area(4, 5))

# question 5
def apply_operation(function, num):
    return function(num)

apply_operation(square, 4)

def double(num):
    return num * 2 
  
print(double(5))
print(apply_operation(double, 7))
print(apply_operation(square, 3))