from fractions import Fraction

t=int(input( ))
for i in range(t):
  x,y=[int(x) for x in input().split()]
  right=x%2 # 0 if even 
  left=y%2
  if right and left :   # odd-odd
    pos_odd_left=(1+x//2)/x
    pos_even_right= (y//2)/y
    pos_even_left= (x//2)/x
    pos_odd_right=(1+y//2)/y
    res= pos_even_left*pos_odd_right+ pos_odd_left*pos_even_right
    print(res)
  if  not right and not left : #even-even
   print("1/2")
  if right and not left : #odd-even
    pos_odd_left=(1+x//2)/x
    pos_even_left= (x//2)/x
    res= pos_even_left*0.5+pos_odd_left*0.5
    print(res)
  if not right and left : #even-odd
    pos_even_right= (y//2)/y
    pos_odd_right=(1+y//2)/y
    res=0.5*pos_even_right+0.5*pos_odd_right
    print(res)

