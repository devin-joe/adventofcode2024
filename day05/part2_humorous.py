t=[i.strip()for i in open('day05/input.txt').readlines()]
r=t[:t.index('')]
u=[eval('['+i+']')for i in t[t.index(''):]]
s=0
for v in u:
    if (v!=(p:=sorted(v,key=lambda x:' '.join([i if int(i[:2]) in v and int(i[3:]) in v else''for i in r]).count('|'+str(x))))):
        s += p[len(p)//2]
print(s)