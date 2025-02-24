with open("language.txt", "r") as file:
    s=0
    t=0
    for line in file.readlines():
        # print(line)
        s+=line.count('s') + line.count('S')
        t+=line.count('t') + line.count("T")
    if(t>s): print("English")
    else: print("french")