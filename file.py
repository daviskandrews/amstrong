if __name__=='__main__':
    n=int(input())
    d={}
    for i in range(n):
        list=input().split()
        d[list[0]]=map(float,list[1:])
    m=0
    query=input()
    for i in d[query]:
        m=m+i
    print("%.2f"%(m/3))