# Thank You
def draw_christmas_tree(height):
    for i in range(height):
        print(' ' * (height - i - 1) + '♥' * (2 * i + 1))
    print(' ' * (height - 2) + '|||')
    print(' ' * (height - 2) + '|||')
    print("\n" "THANK YOU FOR SHARING YOUR KNOWLEDGE")

height = 8  # Adjust the height of the tree
draw_christmas_tree(height)

print("\n\n")

# Calculator
print("DEMO CALCULATOR")
first= input("enter first number: ""\n" )
operator= input("enter operator (+, -, /, *): ")
second= input("enter second number: ")

first= int(first)
second= int(second)

if operator == "+":
    print(first + second)
elif operator == "-":
    print(first - second)
elif operator == "*":
    print(first * second)
elif operator == "/":
    print(first / second)

else:
    print("invalid")


