# Assignment 3

# Aditya_Gupta(SID=21103019)


# question 1
print("Solution 1:\n")

# Main_String is the string entered by user
Main_String = input("Enter string here: ")
print(" ")

# Main_List is list of characters(or words) in Main_String
Main_List = Main_String.split()

# List_char is list of characters(or words) in string without repetition
List_char = []

# Dict_char is the final dictionary containing number of occurrences of every character(or word)
Dict_char = {}

if len(Main_List) == 0:
    print("No string")

elif len(Main_List) == 1:
    # set1 is a random set which stores characters of Main_String without repetition
    set1 = set(Main_String)

    for i in set1:
        List_char.append(i)
        List_char.sort()

    for i in List_char:
        # b is a random variable which counts the occurrences of characters in Main_String
        b = Main_String.count(i)
        Dict_char[i] = b

    print(Dict_char)

elif len(Main_List) > 1:
    # set1 is a random set which stores words of Main_String without repetition
    set1 = set(Main_List)

    for i in set1:
        List_char.append(i)
        List_char.sort()

    for i in List_char:
        # b is a random variable which counts the occurrences of characters in Main_String
        b = Main_List.count(i)
        Dict_char[i] = b

    print(Dict_char)

# ____________________________________________________________________________________________________
print("*" * 80)
# ____________________________________________________________________________________________________


# question 2
print("Solution 2:\n")

# inputs taken in float due to remove decimal inputs
day = float(input("Enter day here[1-31]:"))
mon = float(input("Enter number of month here[1-12]:"))
year = float(input("Enter year here[1800-2025]:"))

if day > 31 or day <= 0 or (day % 1) != 0:
    print("\n Invalid day")

elif mon > 12 or mon <= 0 or (mon % 1) != 0:
    print("\n Invalid month")

elif year > 2025 or year < 1800 or (year % 1) != 0:
    print("\n Invalid year")

else:

    # for months with 31 days (except december)
    if mon == 1.0 or mon == 3.0 or mon == 5.0 or mon == 7.0 or mon == 8.0 or mon == 10.0:

        if day == 31:
            next_day = 1
            next_mon = mon + 1
            next_year = year

        else:
            next_day = day + 1
            next_mon = mon
            next_year = year

    # for months with 30 days (except february)
    if mon == 4.0 or mon == 6.0 or mon == 9.0 or mon == 11.0:

        if day == 30:
            next_day = 1
            next_mon = mon + 1
            next_year = year

        else:
            next_day = day + 1
            next_mon = mon
            next_year = year

    # for the month of february
    if mon == 2:

        # for february 29 in a leap year
        if day == 29 and year % 4 == 0:
            next_day = 1
            next_mon = 3
            next_year = year

        # for february 29 in a non leap year
        elif day == 29 and (year % 4) != 0:
            print("****Invalid date****")

        # for february 28 in a leap year
        elif day == 28 and year % 4 == 0:
            next_day = 29
            next_mon = 2
            next_year = year

        # for february 28 in a non leap year
        elif day == 28 and (year % 4) != 0:
            next_day = 1
            next_mon = 3
            next_year = year

        # for february 1-27
        else:
            next_day = day + 1
            next_mon = mon
            next_year = year

    # for the month of december
    if mon == 12:

        # for december 31
        if day == 31:
            next_day = 1
            next_mon = 1
            next_year = year + 1

        # for december 1-30
        else:
            next_day = day + 1
            next_mon = mon
            next_year = year

    # converting all outputs from float to integer
    next_day = int(next_day)
    next_mon = int(next_mon)
    next_year = int(next_year)

print("\nThe date of next day is: %d/%d/%d" % (next_day, next_mon, next_year))

# ____________________________________________________________________________________________________
print("*" * 80)
# ____________________________________________________________________________________________________


# question 3
print("Solution 3:\n")

print("If you don't want to input more element, type 'end' ")
print(" ")

# lst is the list which contains input elements
lst = []

i = 1
while i >= 1:
    a = input(f"Enter number {i} here:")

    if a == 'end' or a == 'END':
        break

    b = int(a)
    lst.append(b)
    i += 1

print("\nEntered list is :", end=' ')
lst.sort()
print(lst)

# lst2 is the list which contains output elements
lst2 = []

for j in lst:
    lst2.append((j, j ** 2), )

print("\nOutput is:", end=" ")
print(lst2)

# ____________________________________________________________________________________________________
print("*" * 80)
# ____________________________________________________________________________________________________


# question 4
print("Solution 4:\n")

print("Kindly enter grade point as an integer from 4-10")

# let grade point be referred as 'gp'
gp = float(input("Enter your grade point here:"))

if gp == 10:
    print("Your Grade is 'A+' and Outstanding")

elif gp == 9:
    print("Your Grade is 'A' and Excellent")

elif gp == 8:
    print("Your Grade is 'B+' and Very Good")

elif gp == 7:
    print("Your Grade is 'B' and Good")

elif gp == 6:
    print("Your Grade is 'C+' and Average")

elif gp == 5:
    print("Your Grade is 'C' and Below Average")

elif gp == 4:
    print("Your Grade is 'D' and Poor")

else:
    print("****ERROR****")

# ____________________________________________________________________________________________________
print("*" * 80)
# ____________________________________________________________________________________________________


# question 5
print("Solution 5:\n")

s = "ABCDEFGHIJK"

i = 0
while i < 6:
    print(" " * i, end=' ')
    b = 11 - 2 * i
    print(s[0:b])
    i += 1

# ____________________________________________________________________________________________________
print("*" * 80)
# ____________________________________________________________________________________________________


# question 6
print("Solution 6:\n")

print("Type 'Y' if you want to enter details")
print("Type 'N' if you don't want to enter more details\n")

# 'a' asks if user wants to input data
a = input("You want to add details? ")

# dic is the dictionary where all data is entered
dic = {}
# dic2 is the dictionary which contains data sorted by student names
dic2 = {}
# dic3 is the dictionary which contains data sorted by student's SID
dic3 = {}

if a == 'y' or a == 'Y':
    i = 0
    while i >= 0:
        sid = int(input("Enter SID here: "))
        name = input("Enter Name here: ")
        print("  ")
        dic[sid] = name
        a = input("You want to add details? ")
        i += 1

        if a == 'n' or a == 'N':
            break
else:
    print("****ERROR****")

print(" ")

# (a) part
print("a) ", end=' ')
print("The dictionary containing student's names and their SIDs is: ")
print(dic)

# (b) part
print("\nb) ", end=' ')

# let list2 is a list which contains data sorted by names

list2 = sorted(dic.items(), key=lambda x: x[1])  # (this creates a list sorted by student's names)

dic2 = dict(list2)

print("The dictionary sorted by names of students is: ")
print(dic2)

# (c) part
print("\nc) ", end=' ')

# let dic3 is the dictionary which is sorted by SID's
for j in sorted(dic):
    dic3.update({j: dic[j]})

print("The dictionary sorted by SIDs of students is: ")
print(dic3)

# (d) part
print("\nd) ", end=' ')

b = int(input("Enter the SID of student you want to find: "))
print("   ", end=" ")

if b in dic.keys():
    print(f"The name of student with SID {b} is:", end=" ")
    print(dic[b])

else:
    print(f"\n\t No student with the SID {b}")

# ____________________________________________________________________________________________________
print("*" * 80)
# ____________________________________________________________________________________________________


# question 7
print("Solution 7:\n")

# n is the number of terms in Fibonacci Sequence
n = float(input("Enter number of terms in Fibonacci sequence: "))
print(" ")

# let Fibo is the list for storing the terms of Fibonacci Sequence
Fibo = [0, 1]

if n == 0:
    print("No Sequence")

elif n > 0:
    n = int(n)

    for i in range(2, n):
        Fibo.insert(i, Fibo[i - 1] + Fibo[i - 2])
        i += 1

    for i in range(0, n):
        print(Fibo[i])

    Average = sum(Fibo) / n
    print(f"The Average of Sequence is {Average}")

else:
    print("Invalid Number of Terms")

# ____________________________________________________________________________________________________
print("*" * 80)
# ____________________________________________________________________________________________________


# question 8
print("Solution 8:\n")

Set1 = {1, 2, 3, 4, 5}
Set2 = {2, 4, 6, 8}
Set3 = {1, 5, 9, 13, 17}

# a) part
SetA = Set1.symmetric_difference(Set2)
print("a.) ", SetA)

# b) part
SetB = SetA.symmetric_difference(Set3)
print("b.) ", SetB)

# c) part

Set1and2 = Set1.intersection(Set2)
Set2and3 = Set2.intersection(Set3)
Set1and3 = Set1.intersection(Set3)
Set1and2and3 = Set1.intersection(Set2, Set3)

SetZ = Set1and2.union(Set2and3, Set1and3)

SetC = SetZ.difference(Set1and2and3)
print("c.) ", SetC)

# d) part


Set1to10 = set()

# adding integers 1 to 10 in Set1to10
for i in range(1, 11):
    Set1to10.add(i)
    i += 1

SetD = Set1to10.difference(Set1)
print("d.) ", SetD)

# e) part

Set1or2or3 = Set1.union(Set2, Set3)

SetE = Set1to10.difference(Set1or2or3)
print("e.) ", SetE)