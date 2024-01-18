#logical operations in python

#if applicant has high income "AND" has good credit then eligible for loan

hasHighIncome = True

hasGoodCredit = True

if hasHighIncome and hasGoodCredit:
    print(f"Eligible for loan")
else:
    print(f"Not eligible for loan")


#If atleat one of the condition is true "OR"
    
if hasGoodCredit or hasHighIncome:
    print(f"Eligible for loan")
else:
    print(f"Not eligible for loan")

#If doesn't have a criminal record "NOT" operator
    
hasCriminalRecord = False

if hasGoodCredit and not hasCriminalRecord:
    print(f"Person is eligible for loan")
else:
    print(f"Not eligible for loan")