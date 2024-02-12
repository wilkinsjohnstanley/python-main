


#last = m + n - 1
        #merge in reverse order
        #we're gonna keep going while there are elements left in both arrays
'''
while m>0 and n>0:
            #we replace the element in the last position and replace it with
            if nums1[m]>nums2[n-1]: #the index is not the same thing as the number of elements!!! What?
                nums1[last]=nums1[m]
                m -= 1
            else:
                nums1[last]=nums2[n-1]
                n -= 1
            last -= 1

print("result is: ", nums1)

'''
nums1=[1,2,3,0,0,0]
m=3 
nums2=[2,5,6]
n=3

o = len(nums1)
#print(len(nums1))
#print(o)

for i in nums1:
    print("nums1[i] is ", nums1[i])
    print("i is ", i)
    if i == 0:
       # nums1.pop(nums1[i]) #Output: [1, 0, 0, 0]
'''nums1[i] is  2
i is  1
nums1[i] is  3
i is  2
nums1[i] is  0
i is  3
nums1[i] is  1
i is  0
nums1[i] is  1
i is  0
nums1[i] is  1
i is  0'''




    
   
print(nums1)
