/*
To add elements to an array using splice(), you have to provide the following arguments:
1. The starting index(where you want to begin adding elements)
2. The number of elements to remove(0 when you are adding elements)
3. The elements you want to add to the array
*/
var nums = [1, 2, 3, 7, 8, 9];
//index 3, 0 to remove, then the numbers you want to add (4, 5, 6)
nums.splice(3, 0, 4, 5, 6);
console.log(nums);
//start at index 3, and remove four elements
var letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k"];
console.log('Currently, the letters are: '+letters);
letters.splice(3, 3);
console.log('Now, they are some missing: '+letters);
