/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
    let counts = {};
    let countt = {};

    if (s.length !== t.length) {
        return false;
    }

    for (let i = 0; i < s.length; i++) {
        counts[s[i]] = (counts[s[i]] || 0) + 1;
        countt[t[i]] = (countt[t[i]] || 0) + 1;
    }
    for (let c in counts) {
        if (counts[c] !== (countt[c] || 0)) {
            return false;
        }
    }

    return true;
};
