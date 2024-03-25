function copy(arr1, arr2){
    for(var i =0; i<arr1.length;i++){
        arr2[i]=arr1[i];
    }

}
let cars = ["Supra", "Impreza", "Rx7"];
let JDM = [];

copy(cars, JDM);
console.log(cars);
console.log(JDM);
