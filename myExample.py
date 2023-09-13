import ast, sys

input_str = "  This is my first         code   "

final_str = input_str.rstrip()
print(final_str)
print(input_str.strip())

print(len('Python'))
print("Ques 2\n********")

input_str = 'Kumar_Ravi_003'
first_name = input_str[6:10]
second_name = input_str[:5]#write your answer here
customer_code = input_str[-3:]#write your answer here
print(first_name)
print(second_name)
print(customer_code)

print("Ques 3\n********")
egSet = ['SAS', 'R', 'PYTHON', 'SPSS']
print('1.', egSet)
print('2.',egSet[:3])
print('3.',egSet.pop(1))
egSet.remove('SPSS')
egSet.append('Scala')
print('4.',egSet)




print("Ques 3:\n********")
print('This is an exercise to  print the values of split ()')
sentence = "Hello Sanil, We are pleased to inform you that effective immediate we are giving you a hike of 30% straight on your current CTC. Please treat this with atomost confdentiality. Pleae do reach out if there are any questions"
wordSplit = sentence.split()
commaSplit = sentence.split(',')
sentenceSplit = sentence.split('.')
print ("Split Result:\n",wordSplit)
print("Comma Split Result:\n",commaSplit)
print("Sentence Split Result:\n",sentenceSplit)

print ("--------------------------------------------------------------------------------------")
wordJoin = " ".join(wordSplit)
commaJoin = ",".join(commaSplit)
sentenceJoin = ".".join(sentenceSplit)
randomJoin = "     #$#$#$     ".join(wordSplit)
print ("Joined at word: \n",wordJoin)
print("joined at comma",commaSplit)
print("Random join: ",randomJoin)


print ("--------------------------------------------------------------------------------------")

word1 = [2, 33, 222, 14, 25]
word2 = [20, 330, 2220, 140, 250]
#word[:] = []
word3 = word1.extend(word2)
print(word3)

print ("--------------------------------------------------------------------------------------")
print("Tuples")

tupleSample = ("UST","Kochi",682002,)
print(tupleSample)
print(tupleSample[1:3])


