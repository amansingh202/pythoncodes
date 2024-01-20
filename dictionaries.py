#dictionaries

#key value pairs
#Example, name: Aman, mail:wde@gmail.com, phone: 312763487234

#curly braces for dictionary

customer = {
    "name" : "Aman Kumar",
    "age" : 26,
    "is_verified": True,
}

print(customer["name"])
print(customer.get("birthdate")) #if the key is not present it'll give the None in the output

#if we want a default value for a key we'll use the below way:-

print(customer.get("birthdate", "Jan 1, 1995"))

#updating the values
customer["name"] = "Jack Smith"

print(customer.get("name"))