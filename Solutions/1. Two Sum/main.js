/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    for (let i = 0; i < nums.length; i++) {
        for (let i2 = 0; i2 < nums.length; i2++) {
            if (i === i2) {continue;}
            if ((nums[i] + nums[i2]) === target) {return [i, i2];}
        }
    }
};