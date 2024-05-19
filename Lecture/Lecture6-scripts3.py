l1 = ["eat", "sleep", "repeat"]

for ele in l1:
    print (ele)



l1 = ["eat", "sleep", "repeat"]

for count, ele in enumerate(l1):
    print (count, ele)


###############################################

for letter in 'HelloWorld!':

    if letter == 'o' or letter == 'w':
        continue
    print('Current Letter :', letter)


for i in range(0,10):

    if i%2==0:
        continue
    else:
        print("Odd",i)

################################################
for i in range(0,10):

    if i==5:
        break
    else:
        print(i)