var myArray = ['GUVI', 'I', 'am', 'Geek'];

function transformFirstAndLast(myArray) {

var firstItem = myArray[0];
var lastItem = myArray[myArray.length-1];

var objOutput = {};
objOutput[firstItem]=lastItem

return objOutput;
}

var display = transformFirstAndLast(myArray);

console.log(display);