#!/usr/bin/env python
# coding: utf-8

# # Q1

# In[1]:


l1=[22,33,44]


# In[2]:


l1[1]=55


# In[3]:


l1


# In[4]:


dict={"Ramesh":33,"Disha":44,"Sunil":66}


# In[5]:


dict["Sunil"]=55


# In[6]:


dict


# # Q2 Methods of Lists

# In[7]:


list=[1,33,55,66,"sakshi","3.4",33,66,33]


# In[8]:


list.append("priya")
list


# In[9]:


list.copy()


# In[10]:


list.count(33)


# In[11]:


list2=[45,"Rakesh"]
list.extend(list2)
list


# In[12]:


list.index(45)


# In[13]:


list.insert(3,"8.9")
list


# In[14]:


list.pop(6)
list


# In[15]:


list.remove("8.9")
list


# In[16]:


list.reverse()
list


# In[17]:


l=[1,44,66,2,5]


# In[18]:


l.sort()
l


# In[19]:


l.clear()
l


# # Q3 Methods of Dictionary

# In[20]:


dict1={"Ramesh":33,"Disha":44,"Sunil":66}


# In[21]:


dict1.copy()


# In[22]:


d=dict.fromkeys(dict1)
d


# In[23]:


dict1.get("Disha")


# In[24]:


dict1.items()


# In[25]:


dict1.keys()


# In[26]:


dict1.pop("Sunil")
dict1


# In[27]:


print(dict1.popitem())
dict1


# In[28]:


x=dict1.setdefault("Ramesh",66)
print(dict1)
x


# In[29]:


dict1.update({"Priya":77})
dict1


# In[30]:


dict1.values()


# In[31]:


dict1.clear()
dict1


# # Q3 Methods of Strings

# In[32]:


str= "hi I am Sakshi Agrawal and Welcome to my world."


# In[33]:


str.capitalize()


# In[34]:


str.casefold()


# In[35]:


str1="apple 2"
str1.center(30)


# In[36]:


str.count("i")


# In[37]:


str.encode()


# In[38]:


str.endswith(".")


# In[39]:


str2="B\ta\tt"
str2.expandtabs(2)


# In[40]:


str.find("am")


# In[41]:


str4="My name is {fname}"
print(str4.format(fname="Sakshi"))


# In[42]:


str.index("to")


# In[43]:


str="123"
str.isalnum()


# In[44]:


str="sakshi"
str.isalpha()


# In[45]:


str="4.5"
str.isdecimal()


# In[46]:


str="sa7111"
str.isascii()


# In[47]:


str="24350"
str.isdigit()


# In[48]:


str="sakshi"
str.isidentifier()


# In[49]:


str.islower()


# In[50]:


str="1234"
str.isnumeric()


# In[51]:


str.isprintable()


# In[52]:


str= "hi I am Sakshi Agrawal and Welcome to my world."
str.isspace()


# In[53]:


str="Hello, And Welcome To My World!"
str.istitle()


# In[54]:


str="HAPPY WORLD"
str.isupper()


# In[55]:


x=str1.join(str)
x


# In[56]:


x=str1.ljust(4)
print(x, "= 4")


# In[57]:


str.lower()


# In[58]:


str4 = "     apple 2    "

x = str4.lstrip()

print("of all fruits", x, "is my favorite")


# In[59]:


str= "Hi Pveryone"
m = str.maketrans("P", "E")
print(str.translate(m))


# In[60]:


str= "hi I am Sakshi Agrawal and Welcome to my world."
str.partition("and")


# In[61]:


str.replace("hi","Hi")


# In[62]:


str.rfind('a')


# In[63]:


str.rindex("my")


# In[64]:


str.rjust(12)


# In[65]:


str.rpartition("my")


# In[66]:


str.rsplit(".")


# In[67]:


str4 = "     apple 2    "

x = str4.rstrip()

print("of all fruits", x, "is my favorite")


# In[68]:


str.split(".")


# In[69]:


str= "hi I am Sakshi Agrawal and\n Welcome to my world."
str.splitlines()


# In[70]:


str.startswith("h")


# In[71]:


str4 = "     apple 2    "

x = str4.strip()

print("of all fruits", x, "is my favorite")


# In[72]:


str.swapcase()


# In[73]:


str.title()


# In[74]:


str= "Hi Pveryone"
m = str.maketrans("P", "E")
print(str.translate(m))


# In[75]:


str.upper()


# In[76]:


str.zfill(6)

