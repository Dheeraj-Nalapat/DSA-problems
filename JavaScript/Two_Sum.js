/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    let prevMap = {}
    for (let i=0;i<nums.length;i++){
        let diff = target-nums[i];
        if (Object.keys(prevMap).includes(diff.toString())){
            return [prevMap[diff],i];
        }
        prevMap[nums[i].toString()] = i;
    }
};
