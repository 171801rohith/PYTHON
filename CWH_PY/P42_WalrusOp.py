# Walrus Operator

a = True
print(a := False)

num = [2, 3, 4, 6]

while (n := len(num) )> 0:
    print(num.pop(), n)

while len(num) > 0:
    print(num.pop())

foods = list()

while True:
    food = input("Enter a food item (or 'quit' to stop): ")
    if food.lower() == 'quit':
        break
    foods.append(food)

    # OR

foods = list()

while (food := input("Enter a food item (or 'quit' to stop): ") != 'quit'):
    foods.append(food)

