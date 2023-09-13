import ast, sys
#input_str = sys.stdin.read()

input_str = input("Enter a string: ")
input_str=input_str.lower()

vowels=['a','e','i','o','u']

if input_str[0] in vowels:
    print("YES")
else:
    print("NO")