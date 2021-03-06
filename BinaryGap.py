#-*- coding:utf-8 -*-

# Find longest sequence of zeros in binary representation of an integer.

# decimal -> binary 변환을 위한 함수
def int2bin(i):
    binary = ""
    if i < 0:
        return -1
    if i == 0:
        return 0

    while(i):
        binary = str(i%2) + binary
        i = i/2
    
    return binary
    
    
def solution(N):
    binary = int2bin(N) # bin 은 String 형태 
    GapLength = 0  #  1과 1 사이의 0의 길이 값을 저장하는 변수
    max = 0 # 여러 GapLength 들 중 가장 큰 값을 저장하는 변수
   
    for pos in range(0,len(binary)-1):
        if binary[pos] == '1' and binary[pos+1] == '0':
            GapLength += 1
        elif binary[pos] == '0' and binary[pos+1] == '0':
            GapLength += 1
        elif binary[pos] == '0' and binary[pos+1] == '1':
            if GapLength > max:
                max = GapLength
            GapLength = 0
    return max

    
	
	
	
	
	
