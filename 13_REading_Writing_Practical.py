with open("C:\\Taran,Courses & others\\Machine Leanring Codebasics\\Python\\Practise1.txt","r") as f1:
    # print(f1.read())
    # a = 0
    # for i in f1:
    #     if f1 == 9:
    #         a = a+1

    for line in f1.readlines():
        tokens = line.split(",")
        print(tokens)

    # print("Value of search function is :", a)


