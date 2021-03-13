/*
  Parens Valid
    Given an str that has parenthesis in it
    return whether the parenthesis are valid
*/

/**
 * Determines whether the parenthesis in the given string are valid.
 * Each opening parenthesis must have exactly one closing parenthesis.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @return {boolean} Whether the parenthesis are valid.
 */

function parensValid(str) {
  var open = 0;
  var close = 0;
  for (var i = 0; i < str.length; i++) {
    if (str[i] == ")" && open <= close) {
      return false;
    } else if (str[i] == ")") {
      close++;
    } else if (str[i] == "(") {
      open++;
    }
  }
  if (open == close) {
    return true;
  } else {
    return false;
  }
}

// Test Cases

const str1 = "(()(()))";
const expected1 = true;

const str2 = "(()";
const expected2 = false;
// Explanation: not every parenthesis is closed.

const str3 = "())(";   //
const expected3 = false;
// Explanation: because the underlined ")" is premature: there is nothing open for it to close.

const str4 = "))(("; // "))((" ")()("
const expected4 = false;
// Explanation: same number of opens and closes but the 2nd closing closes nothing

console.log(parensValid(str1));
console.log(parensValid(str2));
console.log(parensValid(str3));

/*
  Braces Valid
  Given a string sequence of parentheses, braces and brackets, determine whether it is valid.
*/

/**
 * Determines whether the string's braces, brackets, and parenthesis are valid
 * based on the order and amount of opening and closing pairs.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @return {boolean} Whether the given strings braces are valid.
 */
function bracesValid(str) {

}

const str1 = "({}[({})])[{}]";
const expected1 = true;

const str2 = "({}[]){";
const expected2 = false;

const str3 = "()[(]{)}";
const expected3 = false;

module.exports = { bracesValid };
