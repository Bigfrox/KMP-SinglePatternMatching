import re
import random
from datetime import datetime
import string
import sys


def KMP(text,Pattern,Phi):
    print(text,"\n",Pattern)
    TextSize = len(text)
    PatternSize = len(Pattern)
    q = 0
    for i in range(0,TextSize):
        
        while q > 0 and Pattern[q] != text[i]: #* mismatch
            #print("Mismatch! ", Pattern[q], text[i])
            q = Phi[q-1]
            

        if Pattern[q] == text[i]:#* match
            #print("Match! ", Pattern[q], text[i])
            if q == PatternSize -1:
                print("found!")
                print("Starting pos : ", i-PatternSize+2)
                q = Phi[q]
            else:
                q += 1
        
        
        

def PrefixFunc(P): #* Make Phi array
    m = len(P)
    phi = [0 for x in range(m)]
    phi[0] = 0
    k = 0
    for q in range(1,m):
        # print("k = ", k)
        # print("q = ", q)
        while k > 0 and P[k] != P[q]:
            k = phi[k-1]
        if P[k] == P[q]:
            k += 1
            phi[q] =k
        
        # print(phi)
        # print("======")
    
    
    return phi

def main():

    TEXT = "ababacabacaabacaaba"
    T = list(TEXT)
    
    Pattern = "abacaaba"
    P = list(Pattern)
    filename = "test2.txt"
    input_file = open(filename, 'r')
    
    tmp_data = input_file.read()
    data = tmp_data
    if '\t' in tmp_data:
        tab_index = tmp_data.index('\t')
        min_index = tab_index
        data = tmp_data[:min_index]
        
    if '\n' in tmp_data:
        newline_index = tmp_data.index('\n')    
        min_index = newline_index
        data = tmp_data[:min_index]

    if '\n' in tmp_data and '\t' in tmp_data:
        min_index = min(tab_index,newline_index)
        data = tmp_data[:min_index]
    print(data)
    
    
    #phi = PrefixFunc(P)
    
    #KMP(T,P,phi)



if __name__ == '__main__':
    main()