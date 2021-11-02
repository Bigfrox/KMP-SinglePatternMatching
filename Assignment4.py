'''
Bio Computing Assignment 4, Single Pattern Matching
2016253072
명수환(Myeong Suhwan)
\t와 \n을 만나면 종료. 공백 포함 모든 문자 허용
'''

from datetime import datetime
import sys


def getDataFromFile(filename):
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
    
    return data

def processing(data):
    
    data = data.upper()

    return data

def KMP(text,Pattern,Phi):

    Found = False
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
                Found = True
                print("[*] Found! ", end = " ")
                print("Starting pos : ", i-PatternSize+1)
                q = Phi[q]
            else:
                q += 1
    
    if not Found:
        print("No match found")
        
        
        

def PrefixFunc(P): #* Make Phi array
    m = len(P)
    phi = [0 for x in range(m)]
    phi[0] = 0
    k = 0
    for q in range(1,m):
        
        while k > 0 and P[k] != P[q]:
            k = phi[k-1]
        if P[k] == P[q]:
            k += 1
            phi[q] =k

    return phi

def main():
    if len(sys.argv) != 3:
        print("No input file.")
        print("<Usage> assignment4.py input_filename1.txt input_filename2.txt")
        return -1;
    
    input_filename1 = sys.argv[1]
    input_filename2 = sys.argv[2]
    
    data1 = getDataFromFile(input_filename1)
    data2 = getDataFromFile(input_filename2)
    data1 = processing(data1)
    data2 = processing(data2)

    
    if not data1 or not data2:
        print("[!] No string found.")
        exit(1)

    if len(data1) > len(data2):
        TEXT = data1
        Pattern = data2
    elif len(data2) > len(data1):
        TEXT = data2
        Pattern = data1
    else:
        print("두 길이가 같은 경우")
        TEXT = data1
        Pattern = data2

    print("TEXT: ", TEXT)
    print("Pattern: ",Pattern)
    T = list(TEXT)
    P = list(Pattern)
    
    start_time = datetime.now()

    phi = PrefixFunc(P)
    #print(phi)
    KMP(T,P,phi)

    print("\n")
    
    
    
    print("[+] Time Elapsed : ", datetime.now() - start_time, "microseconds")

if __name__ == '__main__':
    main()