
l=[]

for i in range(21):
    l.append(i)   #list 만들고 끝
for _ in range(10):
  s, e = map(int, input().split()) #map = input().split()을 int 형으로 바꾸어 준다리
  for j in range ((e-s+1)//2):
     l[s+j], l[e-j]=l[e-j], l[s+j]

print(l)                  