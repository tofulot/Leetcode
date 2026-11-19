/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    for (let i= 0; i< nums.length; i++) {
            for (let v= i+1; v< nums.length; v++) {
                
                if (nums[i]+nums[v]==target) {
                    console.log(nums[i]+nums[v])
                    return [i, v];
                }
            }
        }
};