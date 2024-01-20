#emoji's in python

#using application of dictionaries

message = input(">")

words = message.split(" ")

emojis = {
    ":)" : "😀",
    ":(" : "😔",
    "drink": "🍻"
}

output = ""

for word in words:
    output += emojis.get(word, word) + " "

print(output)