var nums = [2, 3, 4, 5];
var newnum=9;
// var N = nums.length;
// for(var i =N; i>=0; --i){
//     nums[i]=nums[i-1];
// }
// nums[0]=newnum;
nums.unshift(0, 1, 1, 1, 1, 1);
console.log(nums);
nums.shift();
console.log(nums);