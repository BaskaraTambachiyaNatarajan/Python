def fact(n):
    if n>1:
        temp=n*fact(n-1)
        return temp
    else:
        return 1

def rep(word):
    #print(word)
    d={}
    for i in word:
        if i in d:
            x=d.get(i)
            d[i]=x+1
        else:
            d.update({i:1})
    count=1
    for i,j in d.items():
        if j>1 and i in word:
            a=fact(j)
            count=count*a
    #print(count)
    return count

def rank(t,c):
    count=0
    j=0
    for i in range(len(t)-1,-1,-1):
        d=fact(i)*int(t[j])
        count+=d//int(c[j])
        j+=1
    return count+1


a=input("Enter a word:")
word=list(set(a))
word.sort()
d={}
for i in a:
    q=word.index(i)+1
    d.update({i:q})
t=[]
c=[]
for i in range(len(a)):
    temp=0
    for j in a[i:]:
        if d[a[i]]>d[j]:
            temp=temp+1
    count=rep(a[i:])
    z=temp
    t.append(z)
    x=count
    c.append(x)
    #print(a[i],temp,count)
r=rank(t,c)
print("Rank of word",a ,"is",r)