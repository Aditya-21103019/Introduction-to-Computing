#Assignment_2

#Aditya_Gupta(SID-21103019)

#question1

#let string be denoted by 'st'


st="Python is a case sensitive language"

#(a) part
print("a) The length of input string is",len(st))

#(b) part
print("b) The reverse order of string is:",st[::-1])

#(c) part
#let new string be denoted as 'st2'
st2=st[10:26]
print("c)New string is :\t",st2)

#(d) part
st.replace("a case sensitive","object oriented")
print("d)The replaced string is :",st)

#(e) part
print('e)The index of substring "a" is',st.find('a'))

#(f) part
print("f)The string after removing white places is",st.replace(" ",""))

#__________________________________________________________________________
print("*************************************************************")

#question2

#let department name be denoted by 'dn'
name=input("Enter your name here:\t")
SID=int(input("Enter your SID here:\t"))
dn=input("Enter your Department here:")
cgpa=float(input("Enter your CGPA here:\t"))

print(f"\nHey, {name}  Here!\n"
      f"My SID is {SID}\n"
      f"I am from {dn} department and my CGPA is {cgpa}\n") 

#__________________________________________________________________________
print("*************************************************************")

#question3

a=56
b=10

#(a) part
print("a) a&b is:",a&b)

#(b) part
print("b) a|b is:",a|b)

#(c) part
print("c) a^b is:",a^b)

#(d) part
print("d) a after being shifted to left by 2 bits is:",a<<2)
print("   b after being shifted to left by 2 bits is:",b<<2)

#(e) part
print("e) a after being shifted to right by 2 bits is:",a>>2)
print("   b after being shifted to right by 4 bits is:",b>>4)

#__________________________________________________________________________
print("*************************************************************")

#question4

#let number be denoted by 'n'
n1=int(input("Enter First number here:\t"))
n2=int(input("Enter Second number here:\t"))
n3=int(input("Enter Third number here:\t"))

N=[n1,n2,n3]
print("The greatest number is\t",max(N))

#__________________________________________________________________________
print("*************************************************************")

#question5

string=input("Enter String here:\t")
print('name' in string)

#__________________________________________________________________________
print("*************************************************************")

#question6

#let side of the triangle be denoted by 's'
s1=int(input("Enter length of first side here:\t"))
s2=int(input("Enter length of second side here:\t"))
s3=int(input("Enter length of third side here:\t"))

if (s1>s2+s3) or (s2>s1+s3) or (s3>s1+s2):
	print("No")
else :
	print("Yes")