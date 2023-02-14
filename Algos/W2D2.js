// *
//   Given a string,
//   return a new string with the duplicates excluded
//   //Bonus: Keep only the last instance of each character.
// */

const str1 = "abcABC";
const expected1 = "abcABC";

const str3 = "";
const expected3 = "";

const str4 = "aa";
const expected4 = "a";

// 1. Driver 🚗
// 2. Presenter 👩‍💻
// 3. Navigator 🧭

// pseudocode here

// create the function and decide what params it needs and what it will return

const str2 = "helloooool";
const expected2 = "helo";

function dedupe(str) {
  var expected = "";
  for (var i = 0; i < str.length; i++) {
    for (var j = 0; j < i; j++) {
      // check for duplicate characters
      if (str[i] == str[j]) {
        break;
        // break out of "if statement" if the letters are the same
      }
    }
    // add character to expected string, when the if statement is true
    if (j == i) {
      expected = expected + [str[i]];
    }
  }
  return expected;
}

console.log(dedupe(str2));

// function removeIfRepeat(str) {
//   var newStr = "";
//   if (str.length == 0) {
//     return "";
//   } else {
//     for (var i = 0; i < str.length; i++) {
//       if (newStr.includes(str[i])) {
//         continue;
//       } else {
//         newStr += str[i];
//       }
//     }
//   }
//   return newStr;
// }

// function remove_dup(str){
//     let tempObj = {};
//     let newString = '';
//     for (let i = 0; i < str.length; i++){
//         if (str[i] in tempObj){
//             tempObj[str[i]] += 1;
//         }
//         else{
//             tempObj[str[i]] = 1;
//         }
//     }
//     for (let key in tempObj){
//         newString+= key;
//     }
//     console.log(newString)
// }
// remove_dup(str1);
