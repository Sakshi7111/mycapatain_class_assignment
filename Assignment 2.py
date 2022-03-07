#!/usr/bin/env python
# coding: utf-8
if marks(x)
x>=90 and x<=100-"A grade"
x>=80 and x<89-"B grade"
x>=70 and x<79-"C grade"
else "Fail"
# In[1]:


x=int(input("Enter the Marks-"))
if x>=90 and x<=100:
    print("A grade")
elif x>=80 and x<=89:
    print("B grade")
elif x>=70 and x<=79:
    print("C grade")
else :
    print("Fail")


# In[2]:


movie=str(input("enter movie"))
if movie == "raid" or movie=="ddlj":
    print("I will watch")
else:
    print("I will not watch")


# In[3]:


x = 10
if not x > 10:
    print("True")
else:
    print("False")


# In[4]:


print("1 for addition")
print("2 for subtraction")
print("3 for multiplication")
print("4 for division")
print("5 for modulo")
print("6 for square")
print("7 for cube")
print("8 for square root")
print("9 for cube root")
choice = input("Enter your choice")
if choice=='1':
    a = int(input("Enter the 1 number"))
    b = int(input("Enter the 2 number"))
    print("Add-",a, "+", b, "=",a+b)
elif choice=='2':
    a = int(input("Enter the 1 number"))
    b = int(input("Enter the 2 number"))
    print("Subtract-",a, "-", b, "=",a-b)
elif choice=='3':
    a = int(input("Enter the 1 number"))
    b = int(input("Enter the 2 number"))
    print("Multiply-",a, "*", b, "=",a*b)
elif choice=='4':
    a = int(input("Enter the 1 number"))
    b = int(input("Enter the 2 number"))
    print("Divide-",a, "/", b, "=",a/b)
elif choice=='5':
    a = int(input("Enter the 1 number"))
    b = int(input("Enter the 2 number"))
    print("Module-",a, "%", b, "=",a%b)
elif choice=='6':
    a = int(input("Enter the 1 number"))
    print("Square-",a, "**", "2", "=",a**2)
elif choice=='7':
    a = int(input("Enter the 1 number"))
    print("Cube-",a, "**", "3", "=",a**3)
elif choice=='8':
    a = int(input("Enter the 1 number"))
    print("Squareroot-",a, "**", "1/2", "=",a**(1/2))
elif choice == '9':
    a = int(input("Enter the 1 number"))
    print("Cuberoot-",a, "**", "1/3", "=",a**(1/3))
else:
    print("Input a valid choice")


# In[ ]:




