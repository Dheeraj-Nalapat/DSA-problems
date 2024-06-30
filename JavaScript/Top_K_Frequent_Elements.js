/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function(nums, k) {
    let count = {};
    let freq = [];
    for(let i=0;i<(nums.length + 1);i++){
        freq.push([]);
    };
    for (n in nums){
        count[n] = (count[n]||0)+1;
    }
    for (n in Object.keys(count)){
        freq[count[n]].push(n);
    }
    let res=[];
    for (let i=nums.length;i>0;i--){
        for (n in freq[i]){
            res.push(n);
            if (res.length == k){
                return res;
            }
        }
    }
};
