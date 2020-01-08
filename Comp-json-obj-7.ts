let expected = {foo: 5, bar: 6};
let actual = {foo: 5, bar: 6};
function assertObjectsEqual(actual, expected)
{
 if(JSON.stringify(actual) == JSON.stringify(expected))
 {
 console.log("Passed");
 }
 else
 {
 console.log("FAILED");
 }
}
assertObjectsEqual(actual, expected);