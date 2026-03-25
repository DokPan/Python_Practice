def statistics(*nums):
    print(sum(nums),sum(nums)/len(nums),
          max(nums),min(nums),len(nums))

statistics(5,8,3,9)
statistics(6,45,3,4,45,78)
statistics(3,2)