# Assignment 3

# Aditya_Gupta(SID=21103019)

# question 1
print("Solution 1:\n")


# n = number of discs (3)
# We are transferring all the 3 discs from rod A to rod C
def Tower_Of_Hanoi(n, source, destination, subsidiary):
    if n == 0:
        return
    Tower_Of_Hanoi(n - 1, source, subsidiary, destination)
    print("Move disk", n, "from rod", source, "to rod", destination)
    Tower_Of_Hanoi(n - 1, subsidiary, destination, source)


n = 3
Tower_Of_Hanoi(n, 'A', 'C', 'B')
print("\n")
# ____________________________________________________________________________________________________
print("*" * 80)
# ____________________________________________________________________________________________________

# question 2
print("Solution 2:\n")

# n is number of lines
n = int(input("Enter n(Number of lines of Pascal's triangle): "))

# Pascal's Triangle using Iterative procedures
print("\nPascal's Triangle using Iterative procedures")
for i in range(1, n + 1):
    for j in range(0, n - i + 1):
        print(' ', end='')

    # first element is always 1
    Y = 1
    for j in range(1, i + 1):
        # first value in a line is always 1
        print(' ', Y, sep='', end='')

        # using Binomial Coefficient
        Y = Y * (i - j) // j
    print()

# Pascal's Triangle using Recursion
print("\nPascal's Triangle using Recursion")


def pascal_triangle(n, original_length=n):
    if n == 0:
        return
    pascal_triangle(n - 1, original_length)
    print('  ' * (original_length - n), end='')

    # first element is always 1
    Z = 1
    for k in range(1, n + 1):
        print(Z, end='   ')

        # using Binomial Coefficient
        Z = Z * (n - k) // k
    print()


pascal_triangle(n)
print("\n")

# ____________________________________________________________________________________________________
print("*" * 80)
# ____________________________________________________________________________________________________

# question 3
print("Solution 3:\n")

# let num1 be the first number
# let num2 be the second number

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# divmod is the in-built function which returns a tuple of quotient and remainder
# quo_rem_tuple is the tuple containing Quotient and Remainder
quo_rem_tuple = divmod(num1, num2)

print(f"\nQuotient of {num1} and {num2} is {quo_rem_tuple[0]}")
print(f"Remainder of {num1} and {num2} is {quo_rem_tuple[1]}")

print("\na)", end='')

print("The function 'divmod' is callable-", callable(divmod))

print("\nb)", end='')


# zero_function is a function printing about the number is zero or not
def zero_function(x):
    if int(x) == 0:
        print("is zero")

    else:
        print("is non-zero")


print(f"First number({num1}) ", end='')
zero_function(num1)
print(f"  Second number({num2}) ", end='')
zero_function(num2)
print(f"  Quotient({quo_rem_tuple[0]}) ", end='')
zero_function(quo_rem_tuple[0])
print(f"  Remainder({quo_rem_tuple[1]}) ", end='')
zero_function(quo_rem_tuple[1])

print("\nc)", end='')

# new_tuple is the tuple which is sum of quotient, remainder and (4,5,6)
new_tuple = quo_rem_tuple + (4, 5, 6)

print(f"Adding (4,5,6) to initial tuple results in - {new_tuple}")

# new_tuple is the tuple containing all elements of new_tuple greater than 4
new_tuple2 = ()
# new_list is the list containing all elements of new_tuple greater than 4
new_list = []

for i in new_tuple:
    if i > 4:
        new_list.append(i)
        new_tuple2 += (i,)

print(f"The filtered out tuple is - {new_tuple2}")

print("\nd)", end='')

# new_set is the set which contains the elements of new_list
new_set = set(new_list)
print(f"The converted set is ", new_set)

print("\ne)", end='')

# new_frozenset is the immutable set of new_set
new_frozenset = frozenset(new_set)
print("The required immutable set is ", new_frozenset)

print("\nf)", end='')

# As 6 will be surely in the new_frozenset
# the loop below will find any value greater than 6
max_val = 6
for i in new_frozenset:
    if i > max_val:
        max_val = i

print(f"Maximum value from the set is {max_val}")
print(f"Hash value of the Maximum value is {hash(max_val)}")
print("\n")
# ____________________________________________________________________________________________________
print("*" * 80)
# ____________________________________________________________________________________________________

# question 4
print("Solution 4:\n")


class Student:
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number

    def __del__(self):
        print("Destructor called, object destroyed")


s1 = Student('Aditya', 21103019)
print("Name of the student is ", s1.name)
print("SID of the student is ", s1.roll_number)
print("\n")

# ____________________________________________________________________________________________________
print("*" * 80)
# ____________________________________________________________________________________________________

# question 5
print("Solution 5:\n")


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


E1 = Employee('Mehak', 40000)
E2 = Employee('Ashok', 50000)
E3 = Employee('Viren', 60000)

print("\na)", end='')
E1.salary = 70000
print(f"The salary of Employee 1 {E1.name} has been updated to {E1.salary}")

print("\nb)", end='')
del E3
print(f"The record of Employee 3 Viren has been deleted")
print(" ")
# ____________________________________________________________________________________________________
print("*" * 80)
# ____________________________________________________________________________________________________

# question 6
print("Solution 6:\n")

# let george_word be the word spoken by George
george_word = input("Enter George's word here: ")

# all alphabets are converted to lowercase
george_word2 = george_word.lower()

gl = len(george_word2)  # gl is number of alphabets in george_word

# let barbie_word be the word spoken by Barbie
barbie_word = input("Enter Barbie's word here: ")

# all alphabets are converted to lowercase
barbie_word2 = barbie_word.lower()

bl = len(barbie_word2)  # bl is number of alphabets in barbie_word


# list_george is the sorted list containing alphabets of george_word
list_george = []
for i in george_word2:
    list_george.append(i)
    list_george.sort()

# list_barbie is the sorted list containing alphabets of barbie_word
list_barbie = []
for i in barbie_word2:
    list_barbie.append(i)
    list_barbie.sort()

number_of_words_by_george = len(george_word2.split())
number_of_words_by_barbie = len(barbie_word2.split())

# condition below is to make sure that both speaks only a single word
if gl == bl and number_of_words_by_george == number_of_words_by_barbie == 1:
    # Even if there is a single difference in george_list and barbie_list their friendship is fake
    z = 1
    for i in range(gl):
        if list_george[i] == list_barbie[i]:
            z = z * 1

        elif list_george[i] != list_barbie[i]:
            z = z * 0

    if z == 0:
        print("****Friendship is Fake****")

    elif z == 1:
        print("****Friendship is Real****")

elif gl != bl:
    print("****Friendship is Fake****")
