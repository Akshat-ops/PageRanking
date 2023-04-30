import tabulate
Aincoming=['C']
Aoutgoing=['B','C']
Bincoming=['A','C']
Boutgoing=['D']
Cincoming=['A','D']
Coutgoing=['A','B','D']
Dincoming=['B','C']
Doutgoing=['C']
probA=[1/4]
probB=[1/4]
probC=[1/4]
probD=[1/4]
sum=0
i=int(input("Enter number of Iterations: "))
for x in range(0,i):
    sum=0
    for y in Aincoming:
        if y=='B':
            sum+=probB[x]/len(Boutgoing)
        elif y=='C':
            sum+=probC[x]/len(Coutgoing)
        elif y=='D':
            sum+=probD[x]/len(Doutgoing)
    probA.append(sum)
    sum=0
    for y in Bincoming:
        if y=='A':
            sum+=probA[x]/len(Aoutgoing)
        elif y=='C':
            sum+=probC[x]/len(Coutgoing)
        elif y=='D':
            sum+=probD[x]/len(Doutgoing)
    probB.append(sum)
    sum=0
    for y in Cincoming:
        if y=='B':
            sum+=probB[x]/len(Boutgoing)
        elif y=='A':
            sum+=probA[x]/len(Aoutgoing)
        elif y=='D':
            sum+=probD[x]/len(Doutgoing)
    probC.append(sum)
    sum=0
    for y in Dincoming:
        if y=='B':
            sum+=probB[x]/len(Boutgoing)
        elif y=='C':
            sum+=probC[x]/len(Coutgoing)
        elif y=='A':
            sum+=probA[x]/len(Aoutgoing)
    probD.append(sum)
l=[probA+list("A"),probB+list("B"),probC+list("C"),probD+list("D")] #formed list of all the pages
l=sorted(l,key=lambda x:x[-2])
Z=l[-1:-len(l)-1:-1]
A=0
B=0
C=0
D=0
for x in Z:
    if "A" in x:
        A=Z.index(x)+1
    elif "B" in x:
        B=Z.index(x)+1
    elif "C" in x:
        C=Z.index(x)+1
    elif "D" in x:
        D=Z.index(x)+1
L=[list("A")+probA+list(str(A)),list("B")+probB+list(str(B)),list("C")+probC+list(str(C)),list("D")+probD+list(str(D))]
headers=["Iteration "+str(x) for x in range(0,i+1)]
headers.append("Page Rank")
print(tabulate.tabulate(L,headers))










