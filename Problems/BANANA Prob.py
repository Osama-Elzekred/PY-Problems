def minion_game(string):
    # your code goes here
    vowels=['O','A','I','U','E']

    kevin,stuart=0,0
    for i in range(len(string)):
      if string[i] in vowels :
         kevin+= len(string)-i
      else:
        stuart+=len(string)-i
    
    if kevin > stuart :
      print(f"Kevin {kevin}",end="")
    if kevin < stuart :
       print(f"Stuart {stuart}",end="")
    else : print("Draw ",end="") 
    
if __name__ == '__main__':
    s = input()
    minion_game(s)





# vowels=['O','A','I','U','E']

# dic1={}
# dic2={}
# str=input()
# for i in range(len(str)):
#   if str[i] in vowels :
#     for j in range(i ,len(str)):
#       sub_str=str[i:j+1]
     
#       dic1[sub_str]=dic1.get(sub_str,0)+1
#   else :
#     for j in range(i ,len(str)):
#       sub_str2=str[i:j+1]
   
#       dic2[sub_str2]=dic2.get(sub_str2,0)+1
      
# if sum(dic1.values()) > sum(dic2.values()) :
#   print(f"Kevin {sum(dic1.values())}")
# elif sum(dic2.values()) > sum(dic1.values()) :
#    print(f"Stuart {sum(dic2.values())}")
# else : print("Draw")





