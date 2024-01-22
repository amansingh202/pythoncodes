#make module to find the largest number in a list
#use this module in another program called app1.py

def listMax(arr):
    max = arr[0]

    for numbers in arr:
        if numbers > max:
            max = numbers

    return max

numbers = [12,34,56,1,90,3]
print(listMax(numbers))