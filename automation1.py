import openpyxl as xl

wb = xl.load_workbook('transactions.xlsx')
sheet = wb['Sheet1']


#below, both are the same ways to get 1st row and 1st column
#either by using a1 which means row1, column1
#or by using .cell method in the sheet object
cell = sheet['a1']

cell = sheet.cell(1,1) #1,1 represents row 1 and column 1

print(cell.value)