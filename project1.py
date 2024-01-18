'''Convert weight in pounds or Kg to the other unit '''

weight = float(input("Enter weight: "))

#boolean to check weather it's kg to pound or otherwise
# kg to pound is "kp" and pound to kg is 'pk'

conversion = input("(K)g or (P)ound: ")
print(conversion)

if conversion.lower() == "p":
    weight_in_kg = 0.456 * weight
    print(f"Weight in kg is {weight_in_kg}")
elif conversion.lower() == "k":
    weight_in_pound = 2.205 * weight
    print(f"Weight in pounds is {weight_in_pound}")
else:
    print("Invalid entry format")