import time
import statistics
import xlsxwriter
l=list()
i=0
while i<10:
    start_time = time.time()
    time.sleep(1)
    print("hello world")
    l.append(time.time() - start_time)
    print("--- %s seconds ---" % (time.time() - start_time))
    i = i+1
x = statistics.mean(l)

# Printing the mean
print("Mean is :" + str(x))

# import xlsxwriter module

# workbook = xlsxwriter.Workbook ('hello.xlsx')
#
#
# worksheet = workbook.add_worksheet ()
#
# worksheet.write('A1', 'Hello..')
# worksheet.write('B1', 'Geeks')
# worksheet.write('C1', 'For')
# worksheet.write('D1', 'Geeks')
# workbook.close()

workbook = xlsxwriter.Workbook ('Example2.xlsx')
worksheet = workbook.add_worksheet ()

# Start from the first cell.
# Rows and columns are zero indexed.
row = 0
column = 0

#content = ["ankit", "rahul", "priya", "harshita",
           #"sumit", "neeraj", "shivam"]

# iterating through content list
for item in l:
    # write operation perform
    worksheet.write (row, column, item)

    # incrementing the value of row by one
    # with each iteratons.
    row = row+1

workbook.close ()