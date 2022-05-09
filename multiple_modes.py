# multiple modes of a given list:

nums = [4,5,9,6,3,2,7,3,4]
modes = set()
hc = nums.count(nums[0])
for num in nums:
    temp = nums.count(num)
    if (temp>hc):
        hc = temp

for num in nums:
    if(nums.count(num)==hc):
        modes.add(num)

for num in modes:
    print(num,end=" ")
