count = 0
with open('4output.txt', 'w') as out:
    while count < 100:
        a = input("how many 1s?\n")
        b = input("how many 2s?\n")
        c = input("how many 3/4s?\n")

        if int(a) + int(b) + int(c) == 5:
            out.writelines(f"{a},{b},{c}\n")
            count += 1
        else:
            print("input error")

        print('\n'+str(count)+'\n')       
