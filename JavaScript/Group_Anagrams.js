/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function(strs) {
    let ans={};
    for(let i=0;i<strs.length;i++){
        let sortedStr = strs[i].split("").sort().join("");
        if (!ans[sortedStr]) {
            ans[sortedStr] = [];
        }
        ans[sortedStr].push(strs[i]);
    }
    return Object.values(ans);
};
