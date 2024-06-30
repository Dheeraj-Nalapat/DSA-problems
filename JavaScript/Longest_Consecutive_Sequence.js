/**
 * @param {number[]} nums
 * @return {number}
 */
var longestConsecutive = function(nums) {
    let numSet = new Set(nums);
    let longest=0;
    for (n of numSet){
        if (!numSet.has(n-1)){
            let length = 1;
            while (numSet.has(n+length)){
                length +=1;
            }
            longest = Math.max(length,longest);
        }
    } 
    return longest;
};
