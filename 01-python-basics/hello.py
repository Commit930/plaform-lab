
food = input("What is your favorite food?")
if food not in ["biryani", "pizza"]:
    print("please enter a valid food name")
    food = None

try:
    count = int(input("How many times you eat it in a week?"))
except ValueError:
    print("please enter your answer in numbers")
    count = None

if food is not None and count is not None:
    print(f"your favorite food is {food} and you eat it {count} times in a week")