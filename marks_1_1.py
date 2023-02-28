mark1 = int(input('Enter subject 1 marks\n'))
mark2 = int(input('Enter subject 2 marks\n'))
mark3 = int(input('Enter subject 3 marks\n'))
mark4 = int(input('Enter subject 4 marks\n'))
mark5 = int(input('Enter subject 5 marks\n'))

max_mark = 500

total_mark = mark1 + mark2 + mark3 + mark4 + mark5
average_mark = total_mark/5
percentage = (total_mark*100)/max_mark
print(f'''    Total Marks Obtained : {total_mark}
    Average Marks : {average_mark}
    Percentage : {percentage}''')