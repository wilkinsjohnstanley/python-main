
var names = ["Maddie", "Emily", "Ellie", "George", "Brittany", "Maddie"];
var name = prompt("Enter a name to search for: ");
var position = names.indexOf(name);
if (position >=0){
    console.log("Found "+name+" at position "+ position);
}
else {
    print(name + "not found in the array.");
}
var firstPos = names.indexOf(name);
print("First found " + name + " at position " + firstPos);
var lastPos = names.lastIndexOf(name);
print("Last found " + name + " at position " + lastPos);