# author = prabhjot Singh
import random
c=0
d=0
h=0
s=0
for i in range(1000):
   x=random.randint(1,52)
   if (x>=1) and (x<=13):
      c+=1
   elif (x>=14)and(x<=26):
      d+=1
   elif (x>=27) and(x<=39):
      h+=1
   else:
      s+=1
print(f"the total club card are {c}")
print(f"the total diamond cards are {d}")
print(f"the total heart cards are {h}")
print(f"the total spades card are {s} ")
total=(c+d+h+s)
print(f"from all {total} shuffels")