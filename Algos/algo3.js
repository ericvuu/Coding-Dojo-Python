/*
  String: Is Palindrome
  Create a function that returns a boolean whether the string is a strict palindrome.
    - palindrome = string that is same forwards and backwards

  Do not ignore spaces, punctuation and capitalization
 */

const str1 = "a x a";
const expected1 = true;

const str2 = "racecar";
const expected2 = true;

const str3 = "Dud";
const expected3 = false;

const str4 = "oho!";
const expected4 = false;

function isPalindrome(str) {
  for (let i = 0; i < Math.floor(str.length / 2); i++) {
    if (str[i] !== str[str.length - 1 - i]) {
      return false;
    }
  }
  return true;
}

// console.log(isPalindrome(str1));
// console.log(isPalindrome(str2));
// console.log(isPalindrome(str3));
// console.log(isPalindrome(str4));


const str1 = "what up, daddy-o?";
const expected1 = "dad";

const str2 = "uh, not much";
const expected2 = "u";

const str3 = "Yikes! my favorite racecar erupted!";
const expected3 = "e racecar e";

/**
 * Finds the longest palindromic substring in the given string.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @return {string} The longest palindromic substring from the given string.
 */

function longestPalindromicSubstring(str) {
  var sub = "";
  var longestsub = "";
  var longestsublength = sub.length;
  for (var i = 0; i < str.length; i++) {
    for (var j = i + 1; j < str.length + 1; j++) {
      sub = str.slice(i, j);
      if(isPalindrome(sub)) {
        if (sub.length > longestsublength) {
          longestsub = sub;
          longestsublength = sub.length;
        }
      }
    }
  }
  return longestsub;
}


console.log(longestPalindromicSubstring(str1));
console.log(longestPalindromicSubstring(str2));
console.log(longestPalindromicSubstring(str3));
