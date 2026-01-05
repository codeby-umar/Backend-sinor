my_Tuple = (0 ,1 , 2 ,3 ,4 ,5 ,6 ,7 ,8 ,9 )

i1 , i2 , i3 , *i4 , i5 = my_Tuple
print("i1 =", i1)
print("i2 =", i2)
print("i3 =", i3)
print("i4 =", i4)
print("i5 =", i5) 




mydict = {"id:" : 1 , "Name" : "Muhammad Umar" , "Age" : 20 , "City" : "Karachi"}
mydic2 = dict(id = 2, Name = "Muhammad Ali" , Age = 15 , City = "Lahore", Country = "Pakistan")
print(mydic2)
print(mydict)
mydict["email"] = "codingbyumar@gmail.com"
mydict["work"] = "Software Engineer"
print(mydict)



lists = ['olma' , 'anor' , 'banan' , 'shaftoli' , 'tarvuz' , 'qovun']
print(lists)
print(lists[0])
print(lists[5:])
print(lists[-1])
print(lists[2:5])



malumot = ['Umar' , 20 , 'Manak' , 'student' , 'programmer'] 
adds =  malumot.append('Turgunov Muhammad Umar')
print(malumot)


# Uyga vazifa

#1
nums = [1, 2, 3, 4, 5 , 6 ,7 ,8 ,9 ,10 , 40]
print(nums)
nums1 = max(nums)
print("Max number is :" , nums1)
nums2 = min(nums)
print(f"Min number is : {nums2}")
print(f"O'rtacha qiymat soni : {nums1 + nums2}")


#2

lists1 = ['olma' , 'anor' , 'banan' , 'shaftoli' , 'tarvuz' , 'qovun']
print(lists1)


#3

words = ['hello' , 'world' , 'python' , 'is' , 'awesome']
print(f"Length of the list is : {len(words)}")
print(f"Max word is : {max(words)}")
print(f"min word is : {min(words)}")


#4

numbers = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10]
suma = numbers[::-1] # teskari qilish bitta usuli
print(suma)
suma = reversed(numbers)
print(list(suma))


#5  Tuples homewrok

data = (10 , 20 , 30 , 40 , 50 , 60 , 70 , 80 , 90 , 100)
data1 = data[2]
print(f"Bu ikinchi indexdagi qiymat: {data1}")
data1 = data[-1]
print("Bu oxirgi indexdagi qiymat: ", data1)


#6 
# use = int(input("Iltimos istalgan son kiriting: "))

t = (1 , 3 , 5 , 7 , 9 , 11 , 13 , 15)  #use)
print(t)


#7
list2 = ['apple' , 'banana' , 'cherry' , 'date' , 'fig' , 'grape']
my_tuples = tuple(list2)
print(my_tuples)
print(type(my_tuples))


#8

student = {
    'name' : "Muhammad Umar",
    'age' : 18,
    'grade' : 85
}

# if 'grade' in student:
#     print("Excelent !")
# elif 'name' in student:
#     print("Good !")
# elif 'age' in student:
#     print("You need to work hard !")
# else : 
#     print("Invalid data !")

greade = student['grade']
age = student['age']

if greade > 80:
    print("Excelent !")
elif age > 18:
    print("Good !")
else: 
    print("You need to work hard !")

#9

# ism = input("Ismingizni kiriting: ")
# yosh = int(input("Yoshingizni kiriting: "))

# jami = {'ism' : ism , 'yosh' : yosh}
# print(jami)
# print(type(jami))


#10 

text = "python is easy to learn and fun to code"
result = {}

for i in text.split():
    if i in result:
        result[i] += 1
    else :
        result[i] = 1


print(result)



#11

a = {1 , 2 , 3 , 4 , 5}
b = {2 , 3 , 5 , 6 , 7}
jami = a.union(b)
print(jami)
kesi = a.intersection(b)
print(kesi)
farqi = a.difference(b)
print(farqi)


#12 

nums = [10 , 20 , 30 , 40 , 50 , 60 , 70 , 80 , 90 , 100]
jami = set(nums)
print(jami)
print(type(jami))

#13 



print("###################################")

kop = [10 , 20 , 30 , 40 , 50 , 60 , 70 , 80 , 90 , 100]


def maxwithout (kops):
    en_katta = max(kops)
    en_kichik = min(kops)
    ortacha = sum(kops) / len(kops)
    return en_katta , en_kichik , ortacha

print(maxwithout(kop))



################################################################

contact = []



def add_intormation( contact , id , name , phone , email):
    new_Contend = {
    "id" : id,
    "name" : name,
    "phone" : phone,
    "email" : email
    }
    contact.append(new_Contend)
    return contact


add_intormation(
    contact,
    1,
    "Muhammad Umar",
    "+998937981208",
    "codingbyumar@gmail.com"
)
add_intormation(
    contact,
    2,
    "Muhammad Umar",
    "+998937981208",
    "codingbyumar@gmail.com"
)

print(contact)
print(type(contact))


