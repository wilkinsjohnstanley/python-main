var numbers = [];
//wheny ou create an array this way, the length is zero. Check!
console.log(numbers.length); //output is zero
//but you can also use a constructor
var nums = new Array(1, 2, 3);
console.log(nums.length);
//you can create an array only specificying it's length
var numero = new Array(10);
console.log(numero.length);
//unlike many other programming languages, but common for most scripting languages
//JavaScript array elements do not all have to be of the same type:
var objects = [1, "Joe", true, null];
//We can check if an object is an array like this:
var numb = 3;
var array = [7, 4, 1776];
console.log(Array.isArray(numb)); //displays false
console.log(Array.isArray(array)); //displays true
