import xlrd 

loc = ("sample.xl")  #change accordingly
wb = xlrd.open_workbook(loc)
sheet=wb.sheet_by_index(0)


print('Sheet name:',sheet.name) # name of sheet
print('number of sheets:',wb.nsheets) # number of sheets
print('number of rows:',sheet.nrows) # number of rows
print('number of cols:',sheet.ncols) # number of cols



#print a particular row
for i in range(sheet.nrows):
    print(sheet.cell_value(i,0))


#print a particular column
for j in range(sheet.ncols):
    print(sheet.cell_value(0,j))    


#extract data of particular cell
data = [[sheet.cell_value(r,c) for c in range(sheet.ncols)] for r in range(sheet.nrows)]
print(data[0][0])


#print whole excel sheet
for r in range(sheet.nrows):
    for c in range(sheet.ncols):
        print(list(sheet.cell_value(r,c))) 


#save data of all rows in a dictionary
d = {}
for i in range(sheet.nrows):
    for j in range(sheet.ncols):
        a = sheet.cell_value(0,j)
        b = sheet.cell_value(i+1,j)
        d[a] = b
    print(d)
