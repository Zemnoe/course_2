
str = "The quick brown fox jumps over the lazy dog"
print(str)

#length of the string
print(len(str)) 

# print the string in upper case
print(str.upper())

#print string in lower case
print(str.lower ())

#print string in title case
print(str.title())

#we want the string to be printed in reverse method
print(str[::-1])

#Add the title method to reverse
print(str[::-1].title()) 

#count the number of occurance "a" in str
print(str.count('a'))

#count the number of occurance of "the"
print(str.count("the"))

#to replace the "the" with "a"
print(str.replace("the","a"))


str = "The quick brown fox jumps over the lazy dog"
#create dictionary to store key value
dict = {}
for i in str:
    #if i  exist as key in dict, icrement the count
    if i in dict:
        dict[i] += 1
        #else if i appears for the first time, add else
    else:
        dict[i]=1
        print(dict)

people = ['Jane', 'John', 'Jack', 'Janet']
sex = ['Female', 'Male', 'Male', 'Female']
age = [23, 34, 16, 28]



person1 = "Jane"
person2 = "John"
person3 = "Jack"
Person4 = "Janet"

sex1 = "Female"
sex2 = "Male"
sex3 = "Male"
sex4 = "Female"

age1 =23
age2 =34
age3 =16
age4 =28

interpo_str1= (f"{person1} the {sex1} is {age1} years old.")
print(interpo_str1)
interpo_str2= (f"{person2} the {sex2} is {age2} years old.")
print(interpo_str2)
interpo_str3= (f"{person3} the {sex3} is {age3} years old.")
print(interpo_str3)
interpo_str4= (f"{Person4} the {sex4} is {age4} years old.")
print(interpo_str4)







   



