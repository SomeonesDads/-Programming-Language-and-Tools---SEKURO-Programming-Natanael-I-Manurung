
Parse_int(arg):

Receives one argument in a form of a string, then converts said string into an integer. The strings simply represent the numbers in words.

---

Examples:

"one" => 1

"twenty" => 20

"two hundred forty-six" => 246

"seven hundred eighty-three thousand nine hundred and nineteen" => 783919
***
Additional Notes:

The minimum number is "zero" (inclusively)

The maximum number, which is supported is 1 million (inclusively)

The "and" in e.g. "one hundred and twenty-four" is optional, in some cases it's present and in others it's not

The code doesn't have measures in case the input isn't valid
