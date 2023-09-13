import ast, sys
input_str = sys.stdin.read()
input_list = ast.literal_eval(input_str)

answer = input_list[2][0]
print(answer)
print (input_list)