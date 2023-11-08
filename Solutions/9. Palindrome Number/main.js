/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    if (x < 0) {return false;} // if it's negative, -XXX becomes XXX- which is always false
    x_reversed = x.toString().split("").reverse().join("");
    return x.toString() === x_reversed;
};