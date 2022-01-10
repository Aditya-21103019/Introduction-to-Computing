#Assignment1

#Aditya_Gupta(SID =21103019)

#question1
#let numbers be denoted by 'n'
n1=int(input("Enter number 1: "))
n2=int(input("Enter number 2: "))
n3=int(input("Enter number 3: "))

print("the average is :",(n1+n2+n3)/3)

#________________________________________________________
print("*********************************************")

#question2

#gross income is referred as 'gi'
gi=float(input("Enter your Gross Income here(in $): "))

#number of dependents are referred as 'nod'
nod=int(input("Enter number of dependents here: "))

#taxable income is referred as 'ti'
ti=gi-10000-3000*nod

print("Your Income Tax is ",ti*0.2)

#___________________________________________________________
print("*********************************************")

#question3

sid=int(input("Enter your SID here: "))
name=input("Enter your name here: ")
gender=input("Enter your Gender: {M for male,F for female and U for unknown}\n")
course=input("Enter your course here: ")
cgpa=float(input("Enter your CGPA here: "))

student=[sid,name,gender,course,cgpa]
print(student)

#___________________________________________________________
print("*********************************************")

#question4

#let marks of students be denoted by 'm'
m1=int(input("Enter marks of student 1 here :"))
m2=int(input("Enter marks of student 2 here :"))
m3=int(input("Enter marks of student 3 here :"))
m4=int(input("Enter marks of student 4 here :"))
m5=int(input("Enter marks of student 5 here :"))

student=[m1,m2,m3,m4,m5]
student.sort()

print(student)

#___________________________________________________________
print("*********************************************")

#question5

#Part(a)
color=['Red','Green','White','Black','Pink','Yellow']
color.pop(3)
print(color)

#Part(b)
color2=['Red','Green','White','Black','Pink','Yellow']
color2[3:5]=['Purple']
print(color2)