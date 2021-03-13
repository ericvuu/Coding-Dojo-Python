/*
  Zip Arrays into Map


  Given two arrays, create an associative array (aka hash map, an obj / dictionary)
  containing keys from the first array, and values from the second.
  Associative arrays are sometimes called maps because a key (string) maps to a value
 */

const keys1 = ["abc", 3, "yo"];
const vals1 = [42, "wassup", true];
const expected1 = {
  abc: 42,
  3: "wassup",
  yo: true,
};

function zipArray(key_array, value_array) {
  let some_dict = {};
  if (key_array.length !== value_array.length) {
    return false;
  } else {
    // loop adding each key value pair as entry
    for (let i = 0; i < key_array.length; i++) {
      // some_dict[key_array[i]] = vals1[i]
      some_dict[key_array[i]] = value_array[i];
      console.log(some_dict);
    }
  }

  return some_dict;
}
// some_dict.push([key])
console.log(zipArray(keys1, vals1));

module.exports = { zipArraysIntoMap };

/*
  Invert Hash
  A hash table / hash map is an obj / dictionary
  Given an object / dict,
  return a new object / dict that has the keys and the values swapped
  so that the keys become the values and the values become the keys
*/

const obj1 = { name: "Zaphod", charm: "high", morals: "dicey" };
const expected1 = { Zaphod: "name", high: "charm", dicey: "morals" };


function invertObj(obj) {
  let output = {};
  for (let property in obj) {
    output[obj[property]] = property;
  }
  return output;
}

module.exports = { invertObj };
