

/* 
  Given an arr and a separator string, output a string of every item in the array separated by the separator.
  
  No trailing separator at the end
  Default the separator to a comma with a space after it if no separator is provided
*/



const arr1 = [1, 2, 3];
const separator1 = ", ";
const expected1 = "1, 2, 3";

const arr2 = [1, 2, 3];
const separator2 = "-";
const expected2 = "1-2-3";

const arr3 = [1, 2, 3];
const separator3 = " - ";
const expected3 = "1 - 2 - 3";

const arr4 = [1];
const separator4 = ", ";
const expected4 = "1";

const arr5 = [];
const separator5 = ", ";
const expected5 = "";

// create an empty string, loop through the array, if statement to ensure comma is not included at the end,  make array a string, put seperator in string  

function join(arr, separator) {
    var str = ""
    for (var i = 0; i < arr.length; i++) {

        if (i == arr.length - 1) {
            str += arr[i]
        }
        else {
            str += arr[i] + separator
        }
    }
    return str
}
console.log(join(arr2, separator2))



function join(arr, separator) {
    var expected = ""
    for(var i = 0; i<arr.length; i++){
        if (i == arr.length -1 && arr.length > 1){
            expected += arr[i].toString()
        }
        else{
            expected += arr[i].toString() + separator;
        }
        
    }
    return expected
}

console.log(join(arr4, separator4));

// don't forget to call the function!