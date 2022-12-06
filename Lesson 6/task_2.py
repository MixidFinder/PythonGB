SYMBOLS = '+-*/%'               
DIGITS = '1234567890'           
ACCEPTABLE = SYMBOLS + DIGITS   

def calc(text):
    groups = []  
    for char in text:
        if char not in ACCEPTABLE:   
            continue
        if (len(groups)==0 or 
            (char in DIGITS  and groups[-1][-1] in SYMBOLS) or
            (char in SYMBOLS and groups[-1][-1] in DIGITS)
           ): 
          groups.append([char])  
        else: 
          groups[-1].append(char)

    if len(groups) < 2 or len(groups) > 3:  
        return None                         
    
    for i in range(len(groups)):            
        groups[i] = ''.join(groups[i])      
    
    operator = groups[1]                    

    if operator not in ['+','-','*','/','**','%']: 
        return None                                
    
    left = int(groups[0])                   
    
    if len(groups) == 2 and operator == '**':      
        groups.append('2')                          
    
    if len(groups) == 3:
        right = int(groups[2])              
        if   operator == "+" :  return left +  right
        elif operator == "-" :  return left -  right
        elif operator == "*" :  return left *  right
        elif operator == "/" :  return left /  right
        elif operator == "%" :  return left %  right
        elif operator == "**":  return left ** right
        else:                   return None
    
    elif operator == '%':
        return float(left) / 100