import os
import numpy as np, numpy.random

def dec_to_bin(input): ## function for quick conversions later
    return ("{0:b}".format(input))

os.chdir(os.path.dirname(os.path.realpath(__file__))) # necessary, otherwise I had trouble finding the probabilities.txt, even though it was in the same directory

prob_list = list(map(float, (open("probabilities.txt").read().splitlines())))

code_list = []
code_words = []



for c in range(len(prob_list) - 1): #adds index to each array in the list
    code_words.append(str(c))

prob_match = zip(prob_list, code_words)


prob_match = sorted(prob_match, key=lambda x:x[0], reverse=True)

final_order = []
prob1 = prob_match[:]
temp1 = []
x = "_"

while len(prob1) > 2:    #sorts the probabilities in huffman style
    if (prob1[-1][1] != x):
        comb_prob = [float(prob1[-1][0]) + float(prob1[-2][0]),x]
        final_order.append(prob1[-1])
        final_order.append(prob1[-2])
        prob1.pop()
        prob1.pop()
        prob1.append(comb_prob)
#    if the previous comb_prob < the next combine comb_prob and the next, add the next and replace comb_prob
#    if the previous comb_prob > the next TWO combines, add the next two, replace com prob
    elif ((prob1[-1][0]) < float(prob1[-2][0])):
        comb_prob = [(comb_prob + float(prob1[-2][0])),x]

        final_order.append(prob1[-2])
        prob1.pop()
        prob1.pop()
        prob1.append(comb_prob)
    else:
        comb_prob = [(comb_prob[0] + float(prob1[-2][0]) + float(prob1[-3][0])),x]
        final_order.append(prob1[-2])
        final_order.append(prob1[-3])
        prob1.pop()
        prob1.pop()
        prob1.pop()
        prob1.append(comb_prob)

    print(comb_prob)


final_order.append(prob1[0])


final_codes = []
for v in range(0,len(final_order)): #adds codewords to the array
    temp = []
    temp = [final_order[v][0],final_order[v][1]]
    temp.append(dec_to_bin(len(final_order)-v))
    final_codes.append(temp)


hopefullyThisWorksSoHarishWillLetMeGraduate = []

for i in range(0,len(final_codes)): #was having trouble using other methods of accesing the array, this works
    hopefullyThisWorksSoHarishWillLetMeGraduate.append(1)



for o in range(0,len(final_order)): # this sorts the current arangment back into the original line order
    temp = final_codes[o]
    temp2 = temp[1]
    hopefullyThisWorksSoHarishWillLetMeGraduate[int(temp[1])] = temp[2]

iApoligizeForMyMessyCode= open("codes.txt","w+")
for fourPointOGPA in range(len(hopefullyThisWorksSoHarishWillLetMeGraduate)): ## prints into the text file line by lin
#     iApoligizeForMyMessyCode.write(hopefullyThisWorksSoHarishWillLetMeGraduate[fourPointOGPA])
     iApoligizeForMyMessyCode.write( hopefullyThisWorksSoHarishWillLetMeGraduate[fourPointOGPA]+ "\n")

iApoligizeForMyMessyCode.close()
