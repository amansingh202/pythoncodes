#re usable function in python

def emojiMaking(message):
    words = message.split(" ")
    emojis = {
        ":)" : "😀",
        ":(" : "😔",
        "drink" : "🍻"
    }

    output = ""
    for word in words:
        output += emojis.get(word, word) + " "

    return output

msg = input(">: ")

print(emojiMaking(msg))