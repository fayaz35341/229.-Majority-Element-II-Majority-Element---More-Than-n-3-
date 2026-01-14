class Solution {
    findMajority(nums) {
        // code here
        let c1=0
        let c2=0
        let e1= -1
        let e2= -1
        for (let i=0;i<nums.length;i++){
            if (nums[i]===e1){
                c1++
            }
            else if (nums[i]===e2){
                c2++
            }
            else if (c1===0){
                c1++
                e1=nums[i]
            }
            else if (c2===0){
                c2++
                e2=nums[i]
            }
            else{
                c1--
                c2--
            }
        }
        let R=[]
        let n=nums.length
        let c11=0
        let c22=0
        for (let i=0 ;i<nums.length;i++){
            if (nums[i]===e1){
                c11++
            }
            else if (nums[i]===e2){
                c22++
            }
        }
        if (c11 > (n/3)) R.push(e1)
        if (c22 > (n/3)) R.push(e2)
        R.sort((a, b) => a - b)
        return R
    }
}
