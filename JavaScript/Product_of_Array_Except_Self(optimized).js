/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function(nums) {
    const n = nums.length;
    let leftProduct = 1;
    let rightProduct = 1;
    const res = new Array(n);

    for (let i = 0; i < n; i++) {
        res[i] = leftProduct;
        leftProduct *= nums[i];
    }

    for (let i = n - 1; i >= 0; i--) {
        res[i] *= rightProduct;
        rightProduct *= nums[i];
    }

    return res;
};
