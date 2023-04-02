import sys
sys.stdin = open("1.txt","r")


dic1 = {'0': '0000', '1': '0001', '2': '0010', '3': '0011',
           '4': '0100', '5': '0101', '6': '0110', '7': '0111',
           '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
           'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'
           }
dic2 = { '211':0 , '221':1, '122':2, '411':3, '132':4, '231':5, '114':6, '312':7, '213':8 ,'112':9 }


def solve():
    ans =set()
    for st in sset:
        bst =''
        for ch in st:
            bst += dic1[ch]

        old = 0
        cnt = []
        for i in range(len(bst)):
            if bst[i] != bst[old]:
                cnt.append(i-old)
                old = i

        pwd = []
        for i in range(1,len(cnt),4):
            mn = min(cnt[i:i+3])
            key = str(cnt[i]//mn) + str(cnt[i+1]//mn) + str(cnt[i+2]//mn)
            pwd.append(dic2[key])


        for i in range(0,len(pwd),8):
            ans.add(tuple(pwd[i:i+8]))


    sm = 0
    for code in ans:
        if (sum(code[0:8:2])*3 + sum(code[1:8:2]))%10==0:
            sm += sum(code)
    return sm



T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().strip().split())

    sset = set()
    for _ in range(N):
        st = input().strip()
        if st.count('0') != len(st):
            sset.add(st)

    ans = solve()

    print(f'#{tc} {ans}')