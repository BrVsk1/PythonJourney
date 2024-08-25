f0 = 0
f1 = 1
f2 = 0
List = []
while f2 < 3524578:
	f0 = f1
	f1 = f2
	f2 = f1 + f0
	if False == f2 % 2:
         print(f2)
         List.append(f2)
print("The sum of all Numbers is:" + str(sum(List)))