# split() results in the list of strings

list1 = input().split()
list2 = []

# conversion of the strings into the integers

for i in list1:
    temp = int(i)
    list2.append(temp)
print(list2)

# mean: sum of elements/total number of elements

sum = 0
for j in list2:
    sum = sum+j
mean = sum/len(list2)
print("mean:",mean)

# median: printing the middle number in both even and odd

sorted_list = list2.sort()
print(list2)
# sort() method is used to print the elements in ascending order.

# median of odd length:
if (len(list2)%2 !=0):
    median = len(list2)//2
    print("median:",list2[median])
# median of even length:
else:
    mid1 = len(list2)//2
    mid2 = mid1-1
    median2 = (list2[mid1]+list2[mid2])/2
    print("median:",median2)

# mode: the number which is occured more number of times:

mode = []
firstcount = list2.count(list2[0])
mode.append(firstcount)
mode.append(list2[0])

for i in range(1,len(list2)):
    tempcount = list2.count(list2[i])
    if (tempcount>mode[0]):
        mode[0] = tempcount
        mode[1] = list2[i]

print("mode" ,mode[1],'count',mode[0])

    










