# range(start, stop, step)
# for i in [1, 2, 3, 4, 5, 6]:
#     print(i)

# for i in range(1, 7, 1):
#     print(i)

# for i in range(7):
#     print(i)

# for _ in range(5):
#     print("hello")


# Challenge FizzBuzzゲーム
for i in range(1, 51):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)