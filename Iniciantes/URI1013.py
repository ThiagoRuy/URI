A,B,C = input().split()
A = int(A)
B = int(B)
C = int(C)
if A>=B>=C or A>=C>=B:
  print(A, "eh o maior")
elif B>=C>=A or B>=A>=C:
  print(B, "eh o maior")
else: 
  print(C, "eh o maior") 
