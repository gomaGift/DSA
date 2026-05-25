def swapParity(s):


    prevNum = None
    currNumber = int(s)

  
    while prevNum == None or prevNum < currNumber:
        
        for i in range(len(s) - 1):
            numChar1 = int(s[i])
            numChar2 = int(s[i+1])

            if numChar1 % 2 == 0 and numChar2 % 2 == 0 and numChar1 < numChar2:
              s = ''.join([s[i+1] if idx == i else s[i] if idx == i+1 else char for idx, char in enumerate(s)])

            elif numChar1 % 2 == 1 and numChar2 % 2 == 1 and numChar1 < numChar2:
              s = ''.join([s[i+1] if idx == i else s[i] if idx == i+1 else char for idx, char in enumerate(s)])
            
           
        if not prevNum:
           prevNum = currNumber
        
        elif prevNum < currNumber:
           prevNum = currNumber
        
        currNumber = max(currNumber, int(s))
    
    return str(prevNum) 

print(swapParity("7596801"))        
           