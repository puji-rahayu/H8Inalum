#!/usr/bin/env python
# coding: utf-8

# In[1]:


print('trial')


# # 1. Integer
# 
# Integer is a numerik data type.
# 

# In[69]:


print(1,2,3)
type(1)


# # 2. Floating-poin
# 
# Floating-poine is a decimal data type for pytho

# In[70]:


print(4.0)


# In[71]:


2.


# In[72]:


.8


# In[73]:


.4e7


# In[74]:


4.2e-2


# # 3. String
# 
# String is a sequence of character data

# In[75]:


print('trial for string data type')


# In[76]:


a=('trial for string data type')
type(a)


# In[77]:


print("this is contain quote (') character")


# # 4. Boolean
# 
# Boolean has 2 values, they are True or False

# In[78]:


False


# In[79]:


True


# In[80]:


type(False)


# In[81]:


type(True)


# In[82]:


type("True")


# # 5. Variables
# ## 5.1. Variables Assignment
# 
# Variable is a notation with value

# In[83]:


n=300
n


# In[84]:


a=400
print(a)


# ## 5.1. Variables Names

# In[85]:


name = 'Puji'
age = 17
has_laptop = True
print(name, age, has_laptop)


# In[86]:


age=1
Age=10
print(age, Age)


# # 6. Operator and Expression in Python

# In[87]:


a=5
b=2
c=a+b
d=a%b
e=a**b
print(c)
print(d)
print(e)


# ## 6.2 Comparison Operators

# In[88]:


a=10
b=20
print(a==b)
print(a!=b)
print(a<=b)
print(a>=b)


# # 7. String Manipulation

# In[89]:


# + operator

a='foo'
b='bar'
c='bats'

print(a+b)


# In[90]:


print('Hactiv8 ' + 'Inalum')


# In[91]:


# * operator

print('fuu' * 5)


# In[92]:


a*8


# In[93]:


# in operator

s='foo'

s in 'that is food for us'


# In[94]:


s in 'that is ice for us'


# In[95]:


# Case convertion

z="HackTIivAte InAlUm"


# In[96]:


z.capitalize()


# In[97]:


z.title()


# In[98]:


#Lowercase

print(z.lower())


# In[99]:


#Uppercase
z.upper()


# In[100]:


print(z.upper(), z.lower())


# In[101]:


#swapcase : menukar (yang upper jadi lower dan sebaliknya)
z.swapcase()


# # 8 List
# 
# Ditandai dengan adanya []

# In[102]:


a=['foo','bar','buz','ice']
a


# In[103]:


b=[21.22, 'foo', 1, 3.64]
b


# In[104]:


s=['foo','bar','buz','ice']
s[2]


# In[105]:


#slicing

s[0:3]


# In[106]:


#slicing no. urut awal sampai 3-1
print(a)
s[:3]


# In[107]:


#slicing no. urut 2 sampai akhir

s[2:]


# In[108]:


s+['value', 'value']


# In[109]:


s * 3


# In[110]:


print(s)
len(s)


# In[111]:


#karena abjad, maka diambil abjad terkecil

min(s)


# In[112]:


max(s)


# In[113]:


a=[1,2,3,4,6,7]
print(min(a))
print(max(a))


# ## 8.1 Modifying Single Value

# In[114]:


s=['foo','bar','buz','ice']


# In[115]:


s[1]=16
s


# In[116]:


s[-1]=20
s


# In[117]:


del s[2]
s


# ## 8.2 Modifying Multiple List Value

# In[118]:


s=['foo','bar','buz','ice']
s


# In[119]:


s[1:3]


# In[120]:


s[1:3]=[1.1, 2.2]
s


# # 9. Tuples

# In[121]:


s=('foo','bar','buz','ice')
s


# In[122]:


s[0]


# In[123]:


s[-1]


# In[125]:


#Isi data Tuple tidak bisa diganti -> error

s[1]='newValue'


# ## 9.1 Dictionary

# In[126]:


identitas = {
    'Fname' : 'Arda',
    'Lname' : 'Nadila',
    'age' : 17   
}


# In[127]:


identitas


# In[128]:


identitas['Lname']


# In[129]:


identitas['Profesion']='Teacher'


# In[130]:


identitas


# In[131]:


identitas['Profesion']='Lecture'


# In[132]:


identitas


# In[133]:


del identitas['Profesion']


# In[134]:


type(identitas)


# In[135]:


person={}


# In[136]:


type(person)


# In[137]:


person['Fname']='Puji'
person['Lname']='Rahayu'
person['Age']=27
person['brothers']=['borther1', 'brother2']


# In[138]:


person


# In[139]:


#List berisi dictionary

person['pets']={'Fish':'fish1', 'Rabbit':'Rabbit1'}


# In[140]:


person


# In[141]:


person['brothers'][1]


# In[142]:


person['pets']['Rabbit']


# In[143]:


d={'a':10, 'b':20, 'c':30}


# In[144]:


d


# In[145]:


#keys

d.keys()


# In[146]:


#values

d.values()


# In[147]:


#Python statement

print('Helo World!')


# In[148]:


#Line continuation

person1_age=42
person2_age=26
person3_age=71


# In[149]:


someone_is_on_working_age = (
    person1_age >= 18 and person1_age <= 65 or
    person2_age >= 18 and person2_age <= 65 or
    person3_age >= 18 and person3_age <= 65
)

someone_is_on_working_age


# In[150]:


someone_is_on_working_age = (
    person1_age >= 18 and person1_age <= 65 and
    person2_age >= 18 and person2_age <= 65 and
    person3_age >= 18 and person3_age <= 65
)

someone_is_on_working_age


# In[151]:


d=[1, 2, [3,4,5], 6]
d[2]


# In[152]:


a=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
a


# In[153]:


b=[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 8]
]
b


# In[154]:


a=
    'Hello'


# In[155]:


a=    'Hello'


# In[156]:


a


# In[157]:


#Multiple Statement per Line

x=10; y=20; z=20
print(x); print(y); print(z)


# In[158]:


#Comment
a=[1, 2] #I'm a comment
a


# In[159]:


b="#I'm not a comment"
b


# In[160]:


'''
Initial value of radius of circle
The calculation as below
'''

pi=3.14
r=12
area=pi * (r ** 2)
print('the area for circle is', area)


# In[161]:


area


# # 11. Condition

# In[162]:


#If Statement

x=0
y=5

if x<y :
    print('yes')

if 'aul' in 'grault' :
    print('yes')


# In[163]:


if 'foo' in ['bar', 'baz', 'quxx']:
    print('Expression was true')
    print('Execution statement')
    print('...')
    print('Done')

print('After conditional')


# In[164]:


if 'foo' in ['foo', 'baz', 'quxx']:
    print('outer condition is true')
    
    if 10>20 :
        print('inner condition 1')
    
    print('Between inner condition')
    
    if 10<20 :
        print('inner condition 2')
    
    print('End of outer condition')

print('After outer condition')


# In[165]:


# else and elif

if<expr>:
    <statement>
else:
    <statement>


# In[166]:


x=20

if x>20:
    print('x is small')
else:
    print('x is large')


# In[167]:


if<expr>:
    <statement>
elif<expr>:
    <statement>
elif<expr>:
    <statement>
...
else:
   <statement> 


# In[168]:


name = 'Hacktiv8'

if name=='Fred':
    print('Hello Fred')
elif name=='Puji':
    print('Hello Puji')
elif name=='Hacktiv8':
    print('Hello Arlnod')
else:
    print('no name')


# In[169]:


if 'a' in 'bar':
    print('right')
elif 1/0:
    print('wrong')
elif var:       #tidak ada variabel var
    print('srong also')


# In[170]:


#One Line if Statement

if 'f' in 'foo': print('1'); print('2'); print('3')


# In[171]:


x=2

if x==1: print('foo'); print('coy');
elif x==2: print('qux'); print('try');
else: print('SALAH')


# In[172]:


##Ternary operator (Conditional Expression)

age=22

'teen' if age<21 else 'adult'


# In[173]:


if a>b:
    m=a
else:
    m=b
    
m=a if a>b else b


# In[174]:


##Pass statement

if True:
    pass

print('foo')


# In[175]:


##while -> untuk looping / pengulangan

n=5

while n>0:
    n -= 1
    print(n)


# In[176]:


#Break and Continue Statement

n=5

while n > 0:
    n -=1
    if n==1:
        break #pass
    print(n)
print('Loop Ended')


# In[177]:


n=5

while n > 0:
    n -=1
    if n==1:
        continue #pass
    print(n)
print('Loop Ended')


# In[178]:


n=5

while n > 0:
    n -=1
    print(n)
else:
    print('Loop Ended')


# In[179]:


n=5

while n > 0:
    n -=1
    if n==1:
        break #pass
    print(n)
else:
    print('Loop Ended')


# In[180]:


#One Line while loops

n=5

while n > 0: n -= 1; print(n);


# In[181]:


n=5
while n>0: n-=1; print(n)


# In[182]:


a = ['foo', 'bar', 'baz']

for i in a:
    print(i)


# In[183]:


d = {'foo':1, 'bar':2, 'baz':3}

for k in d:
    print(k)


# In[184]:


d['foo']


# In[185]:


#Range Fnction

x=range(10)
x


# In[186]:


for i in x:
    print(i)


# In[187]:


#break and continue

for i in ['foo', 'bar', 'baz']:
    if 'z' in i:
        break
    print(i)


# In[188]:


for i in ['foo', 'bar', 'baz']:
    if 'z' in i:
        continue
    print(i)


# In[189]:


for i in ['foo', 'bar', 'baz']:
    print(i)
else :
    print("Done")


# In[190]:


for i in ['foo', 'bar', 'baz']:
    if 'z' in i:
        break
    print(i)
else:
    print('Done')


# In[191]:


#TEMPERATURE CONVERTER

temp=input("Ketik temperatur yang ingin dikonversi")


# In[192]:


#TEMPERATURE CONVERTER

temp=input("Ketik temperatur yang ingin dikonversi")


# In[193]:


#TEMPERATURE CONVERTER

temp=input("Ketik temperatur yang ingin dikonversi, eg. 45F, 28C: ")
degree = int(temp[:-1])
i_convertion = temp[-1]

if i_convertion == "C":
    result = (9 * degree) / 5 + 32
elif i_convertion == "F":
    result = (degree - 32) * 5/9
else:
    print("masukkan yang benar")

print("Temperaturnya adalah", result)


# In[194]:


temp


# In[195]:


result


# In[196]:


#TEMPERATURE CONVERTER

temp = input("Ketik temperatur yang ingin dikonversi, eg. 45F, 28C: ")
degree = int(temp[:-1])
i_convertion = temp[-1]

if i_convertion == 'C':
    result = int(round((9 * degree) / 5 + 32))
elif i_convertion == 'F':
    result = int(round((degree - 32) * 5 / 9))
else:
    print('masukkan yang benar')

print('Temperaturnya adalah', result)


# In[198]:


while True:
    mag = input("Ketikkan karakter: ")
    print(mag)
    if mag == 'stop':
        break


# In[ ]:




