// Reversals
const str1 = "creature";
const expected1 = "erutaerc";

const str2 = "dog";
const expected2 = "god";

const str3 = "hello";
const expected3 = "olleh";

const str4 = "";
const expected4 = "";

// Reverse String (Works on str1-str4)
function reverseString(str) {
    var empty_str = [];
    length = str.length-1;
    for(i=length; i>=0; i--){
        empty_str.push(str[i])
    }
    return empty_str.join("");
}

console.log(reverseString(str4))

// Acronyms

const strA = "object oriented programming";
const expectedA = "OOP";

// The 4 pillars of OOP
const strB = "abstraction polymorphism inheritance encapsulation";
const expectedB = "APIE";

const strC = "software development life cycle";
const expectedC = "SDLC";

// Bonus: ignore extra spaces
const strD = "  global   information tracker    ";
const expectedD = "GIT";

// Acronymize (works on strA-strC)
function acronymize(str) {
    new_string = [];
    new_string.push(str[0]);
    for(i=0; i<=str.length; i++){
        if(str[i] == " "){
            new_string.push(str[i+1])
        }
    }
    return new_string.join("").toUpperCase();
}

// Acronymize (works on strA-strD)
function acronymize2(str) {
    new_string = [];
    if(str[0] != " "){
        new_string.push(str[0])
    }
    for(i=0; i<=str.length; i++){
        if(str[i] == " " && str[i+1] != " "){
            new_string.push(str[i+1])
        }
    }
    return new_string.join("").toUpperCase();
}

console.log(acronymize2(strD))