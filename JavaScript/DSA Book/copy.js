var nums=[];
for (var i=0;i<10;i++){
    nums[i]=i+1;
}
var samenums=nums;
console.log(samenums);
nums[0]=11;
console.log(samenums);
//it was all the same nums the whole time