"""This program simulates every possible combination of scores and
outputs them to possibilities.csv. There are 243 possibilities.
"""
import csv

scores = [1,4,8]
Domains = ['C','A','R','E','S']
possibilities = [Domains]
for a in range(3): #C
    for b in range(3): #A
        for c in range(3): #R
            for d in range(3): #E
                for e in range(3): #S
                    possibilities.append([scores[a],scores[b],scores[c],scores[d],scores[e]])
with open('possibilities.csv',"w") as csvfile:
    pwriter = csv.writer(csvfile, lineterminator='\n')
    pwriter.writerows(possibilities)
print(len(possibilities))
