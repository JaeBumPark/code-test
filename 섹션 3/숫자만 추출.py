import sys
sys.stdin=open("input3.txt", "rt")
n=input()
cnt=0
res=0
for x in n: #s가 x를 하나하나 접근
    if x.isdecimal(): #isdecimal는 0~9까지의 숫자만, digit은 알파벳이 아닌 숫자를 찾아줌
       res=res*10+int(x) #첫자리  0은 거르고, 숫자를 계속 쌓아감
print(res)
for i in range(1, res+1):
    if res%i==0: #약수 찾기
        cnt+=1
print(cnt)       #약수 갯수

