nums = [2,2,1]
n = len(nums)+1
LUT = {}
for i in nums:
    if i in LUT.keys():
        LUT[i] = 'y'
    else:
        LUT[i] = 'x'
print(LUT)
for j in LUT:
    
    if LUT[j] == 'x':
        print(j)


    
