class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # ls=[]
        # n=len(nums)
        # for i in range(n):
        #     if len(ls)==0 or ls[0]!=nums[i] :
        #         c=0
        #         for j in range(n):
        #             if nums[j]==nums[i]:
        #                 c+=1
        #         if c>(n//3):
        #             ls.append(nums[i])
        #     if len(ls)==2:
        #         break
        # return ls
        # Time Limit Exceeded --

        # ls=[]
        # mpp= {}
        # n=len(nums)
        # m=(n//3)+1
        # for i in range(n):
        #     mpp[nums[i]]= mpp.get(nums[i],0)+1
        #     if mpp[nums[i]]==m:
        #         ls.append(nums[i])
        # return ls
        # 15 ms ,23.43MB 
        
        # 14ms, 22.03MB
        # c1=0
        # c2=0
        # e1=float("-Inf")
        # e2=float("-Inf")
        # for i in range(len(nums)):
        #     if (c1==0 and e2 != nums[i]):
        #         c1=1
        #         e1=nums[i]
        #     elif (c2==0 and e1 != nums[i]):
        #         c2=1
        #         e2=nums[i]
        #     elif (nums[i]==e1):
        #         c1+=1
        #     elif (nums[i]==e2):
        #         c2+=1
        #     else:
        #         c1-=1
        #         c2-=1
        # c1=0
        # c2=0
        # ls=[]
        # for i in range(len(nums)):
        #     if (e1==nums[i]):
        #         c1+=1
        #     if (e2==nums[i]):
        #         c2+=1
        # mini=(len(nums)//3)+1
        # if (c1>=mini):
        #     ls.append(e1)
        # if (c2>=mini):
        #     ls.append(e2)
        # ls.sort
        # return ls
        
        # 7ms,22.22MB
        c1=c2=0
        e1=e2=-1
        for i in nums:
            if i==e1:
                c1+=1
            elif i==e2:
                c2+=1
            elif c1==0:
                c1+=1
                e1=i
            elif c2==0:
                c2+=1
                e2=i
            else:
                c1-=1
                c2-=1
        R=[]
        n=len(nums)
        c1=c2=0
        for i in nums:
            if i==e1:
                c1+=1
            elif i==e2:
                c2+=1
        if c1>(n//3):
            R.append(e1)
        if c2>(n//3):
            R.append(e2)
        return R
