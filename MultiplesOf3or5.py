for i in range(1001):
    if i == 0:
        print(i)
    elif 0 == i % 3  and 0 == i % 5:
        print(str(i) + " is dividible by 3 and 5")
    elif 0 == i % 3 :    
        print(str(i)+ " is dividible by 3")
    elif 0 == i % 5 :    
        print( str(i) + " is dividible by 5")
    else:
        print(i)


