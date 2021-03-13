/*

  String: Reverse
  Given a string,
  return a new string that is the given string reversed

*/


const str1 = "creature";
const expected1 = "erutaerc";

const str2 = "dog";
const expected2 = "god";

function reverseString(str) {
  let newStr = "";
  let i = str.length - 1;

  while(i >= 0){
    newStr += str[i]
    i--
  }
  return newStr;
}

console.log(reverseString(str1), reverseString(str1) == expected1);
console.log(reverseString(str2), reverseString(str2) == expected2);


/*****************************************************************************/

/* case insensitive string compare */

const strA1 = "ABC";
const strB1 = "abc";
const expected1 = true;

const strA2 = "ABC";
const strB2 = "abd";
const expected2 = false;

const strA3 = "ABC";
const strB3 = "bc";
const expected3 = false;


function caseInsensitiveStringCompare(strA, strB) {
  return strA.toUpperCase() === strB.toUpperCase()
}

console.log(caseInsensitiveStringCompare(strA1, strB1));
console.log(caseInsensitiveStringCompare(strA2, strB2));
console.log(caseInsensitiveStringCompare(strA3, strB3));

module.exports = { caseInsensitiveStringCompare };
