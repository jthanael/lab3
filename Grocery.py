grocery = []

print("Welcome to Your Shopping List!")

while True:

    print = int(input("Please make a selection from one of the following options:"))
    list = '''
1. Add an item to the shopping list.
2. Display the shopping list.
3. Display the item count.
4. Display the first item in the shopping list.
5. Display the last item in the shopping list.
4. Clear the shopping list.'''


print(list)
selection  = input("Enter your selection: ") 

if selection == "1":
    list_item = input("Enter the item you would like to add: ")
    grocery.append(list_item)