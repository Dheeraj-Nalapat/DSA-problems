/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function(nums) {
    let left = [1];
    let right = [1];
    for (let i=0;i<nums.length-1;i++){
        left.push(left[i]*nums[i]);
    }
    for (let i=nums.length-1;i>0;i--){
        right.unshift(right[0]*nums[i]);
    }
    let res = []
    for (let i=0;i<nums.length;i++){
        res.push(left[i]*right[i]);
    }
    return res;
};
