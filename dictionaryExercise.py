#Exercise on dictionary

#Enter a phone number and convert that in words 
#Example 1234 => one two three four

print("Enter phone number: ")

number = input("Phone: ")

print(number)

dict_map = {
    "0" : "zero",
    "1" : "one",
    "2" : "two",
    "3" : "three",
    "4" : "four",
    "5" : "five",
    "6" : "six",
    "7" : "seven",
    "8" : "eight"
} 

output = ""
for ch in number:
    output += dict_map.get(ch, "!") + " "

print(output)