marks = [10, 23, 34, 90, 29, 78]

# index = 0
# for mark in marks:
#     print(mark)
#     if index == 3:
#         print("Awesome")
#     index += 1

for index, mark in enumerate(marks):
    print(mark)
    if index == 3:
        print("Awesome")

for i in enumerate(marks, start=2):
    print(i)
