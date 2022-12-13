#!/bin/bash

# Store the two strings in variables
string1="taupeman"
string2="gravierboy"

# XOR the two strings and store the result in a third variable
result=""
for ((i=0; i<${#string1}; i++)); do
  # Use the XOR operator (^) to combine the characters at position i in each string
  result+=`printf '%x' "'${string1:$i:1}"^"${string2:$i:1}"`
done

# Output the result as a hexadecimal string
printf "%s[%s]" "P=" $result | pbcopy
echo "Done"
