var = 3.435453
full = "Hello John"
my_string = "the varibles is %s" % full
mystrings = "the varibles is %.3f" % var
print(mystrings)
print(my_string)

print("--------------------------------------------------")

my_format = "the varible is {}".format(full)
my_formats = "the varible if {:.2f}".format(var)
print(my_formats)
print(my_format)


print("--------------------------------------------------")


#01 Homework

title = "python      hello John , How are you doing today ? python is fun"
jami = title.strip()
jami = jami.lower()
jami = title.find("python")
jami = title.count("python")
print(jami)


print("--------------------------------------------------")

#02 Homework

number = ["1" , "2" , "3" , "4" , "5" , "6" , "7" , "8" , "9" , "10"]
run = number.append("11")
print(run)


#03 Homework

# t = (10 , 20 , 30 , 40 , 50)
# t['0'] = 200
# print(t)  # tuble o'zgaritilmaydi


#04 Homewrok

por = "Hello world"

for i in por:
    set(i)
    print(set(i))
    continue


#05 Homework

n = [1 , 2  , 3 , 4 , 5 , 10]
jami = sum(n)
print('Jami somma is : %i' % jami)



#06 Homework

number = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10]
total = 0
i = 0

while i < len(number):
    total += number[i]
    i += 1
print(total)


if i < len(number):
    total += number[i]
    i += 1

print(f"Total is : {total}")






