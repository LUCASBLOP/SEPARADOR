#1) 0, 1, 2 3, 4, 5, 6, 7,
a="0, 1, 2 3, 4, 5, 6, 7,"
a=a.replace(",",";")
print(a)

#2), 1 2 3, 4,5 ,7
b=", 1 2 3, 4,5 ,7"
b=b.replace(",",";")
print(b)

#3), "afsg,mhaj", "abs," 2
c=", \"afsg,mhaj\", \"abs,\" 2"
c=list(c)
i=0
while i< len(c):
    if c[i]=="," and (i==0 or i==13):
         c.pop(i)
         c.insert(i,";")
    i=i+1
c="".join(c)  
print(c)

#4) 0.9, 9;2, 2 3, "def;", 12
c="0.9, 9;2, 2 3, \"def;\", 12"
c=c.replace(",",";")
print(c)

#5) 0.12, "asd,as", "1,2", 1.2
d="0.12, \"asd,as\", \"1,2\", 1.2"
d=list(d)
i=0
while i< len(d):
    if d[i]=="," and (i==4 or i==14 or i==21):
         d.pop(i)
         d.insert(i,";")
    i=i+1
d="".join(d)  
print(d)

#6)0, "ab\",bc;\"de", "asgdte"
d= """0, "ab\\",bc;\\"de", "asgdte" """
d=list(d)
i=0
while i< len(d):
    if d[i]=="," and (i==1 or i==8 or i==17):
         d.pop(i)
         d.insert(i,";")
    i=i+1
d="".join(d)  
print(d)




    




        
        
        



            



   

        


    



