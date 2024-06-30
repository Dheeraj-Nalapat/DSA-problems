/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function(nums, k) {
    let count = {};
    for (let num of nums) {
        count[num] = (count[num] || 0) + 1;
    }
    
    let freq = [];
    for (let i = 0; i <= nums.length; i++) {
        freq.push([]);
    }
    
    for (let num in count) {
        let frequency = count[num];
        freq[frequency].push(parseInt(num)); 
    }

    let res = [];
    for (let i = freq.length - 1; i >= 0 && res.length < k; i--) {
        if (freq[i].length > 0) {
            for (let j = 0; j < freq[i].length && res.length < k; j++) {
                res.push(freq[i][j]);
            }
        }
    }
    
    return res;
};
