nums = [1,2,3,3,7,8,7]
target = 6
for i in nums:
    if(target-i == i):
        try:
            start = nums.index(i) +1
            val = [start-1, nums.index(i,start)]
        except ValueError:
            print('Error')
    else:
        try:
            chk = nums.index(target-i)
            val = [nums.index(i),chk]
        except ValueError:
            continue

print(val)