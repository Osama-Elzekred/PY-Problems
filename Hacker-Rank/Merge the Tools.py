def merge_the_tools(string, k):
    # your code goes here
    l=[]    
    for i in range(len(string)):
        if string[i]  not in l:
            l.append(string[i])
        
        if (i+1)%k==0:
            print(''.join(l))
            l.clear()
        
            
     
        
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
