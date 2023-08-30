# formas de pasar datos al programa
import sys

print(sys.argv)
print(sys.argv[0]) # program name
print(sys.argv[1]) # first arg

# mediante input
print("Welcome to the greeter program")
name = input("Enter your name: ")
print("Greetings " + name)

print("calculator program")
first_number = input("first number: ")
second_number = input("second number: ")
print(int(first_number) + int(second_number))

