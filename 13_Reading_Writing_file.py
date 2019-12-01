# for Writing in file
# f= open("C:\\Taran,Courses & others\\Machine Leanring Codebasics\Python\\funny.txt","w")
# f.write("I love Java")
# f.close()

# for appending in the file
# f = open("C:\\Taran,Courses & others\\Machine Leanring Codebasics\\Python\\funny.txt","a")
# f.write("\nOne more time I am appending data by writing that I love Mahcine learning")
# f.close()

# Reading from file
# f = open("C:\\Taran,Courses & others\\Machine Leanring Codebasics\\Python\\funny.txt","r")
# print(f.read())
# f.close()

# for reading line by line from file
# f = open("C:\\Taran,Courses & others\\Machine Leanring Codebasics\\Python\\funny.txt", "r")
# for line in f:
#     print(line)
# f.close()

# Read the number of words in line and push it into the new file

# f = open("C:\\Taran,Courses & others\\Machine Leanring Codebasics\\Python\\funny.txt", "r")
# f_out = open("C:\\Taran,Courses & others\\Machine Leanring Codebasics\\Python\\count.txt", "w")
# Line is justa a variable
# for line in f:
#     tokens=line.split(' ')
#     # print(len(tokens))
#     # print(tokens)
#     # print(str(tokens))
#     f_out.write("word count:"+str(len(tokens))+"\t"+line)
#
#
# f.close()
# f_out.close()

# With statement
# IF we dont want to close the file explicitly for ex while writing big piece of code one is tend to forget so use with to avoid close liek show below:

with open("C:\\Taran,Courses & others\\Machine Leanring Codebasics\\Python\\funny.txt", "r") as f:
    print(f.read())

    # Next statement will show if answer is true or false...it shud be false since used with statement.
    print(f.closed)