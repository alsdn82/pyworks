# 중첩 if
# 조건 : 10을 기준으로 큰수와 작은수 구분하고 짝수, 홀수도 구분

n = 19
if n > 10:
    if n % 2 == 0:
        print("10보다 큰 짝수입니다.")
    else:
        print("10보다 큰 홀수입니다.")
else:
    if n % 2 == 0:
        print("10이하의 짝수입니다.")
    else:
        print("10보다 작은 홀수입니다.")
        

# if ~ elif ~ else
if n > 10 and n % 2 == 0:
    print("10보다 큰 짝수입니다.")
elif n > 10 and n % 2 != 0:
    print("10보다 큰 홀수입니다.")
elif n <= 10 and n % 2 == 0:
    print("10이하의 짝수입니다.")
else:
    print("10보다 작은 홀수입니다.")
    
    
    
