# The MU puzzler Complete!
# You start with the string 'MI'
# Use the rules to make the string 'MU'

# Rules:
#Rule 1: if you possess a string whose last letter is 'I', you can add on a 'U' at the end.

#Rule 2: Suppose you have 'Mx'.  Then you may add 'Mxx' to your collection.

#Rule 3: If 'III' occurs in one of the strings in your collection, you may make a new string with U in place of III.

#Rule 4: if 'UU' occurs inside one of your strings, you can drop it.


# 1 add U if string ends in I
def op1(string):
    if string[-1] == 'I':
        return string + 'U'
    else:
        print "string doesn't end in 'I'."
    return string

# 2 double string content after M
def op2(string):
    x = string[1:]
    return string + x
    
# 3 replace instance of III with U
def op3(string, case):
    # input: string, set of 'III' to be changed
    # find cases of 'III' and increment a variable each time 
    #   one is found.  When the variable matches the case
    #   ammend it.
    incidence = 0  #to track incidence of 'III'
    prestring = ''
    instance = string.find('III')
    
    if case == 'all':
        while instance != -1:
            string = prestring + string[:instance] + 'U' + string[instance + 3:]
            instance = string.find('III')
        return string
    
    while instance != -1:
        incidence += 1
        
        # once intended case of "III" is found, it's rplcd with "U"
        if incidence == case:
            string = prestring + string[:instance] + 'U' + string[instance + 3:]
            return string
            
        # if incidence is not instance specified in arg, searches rest of string
        else:
            prestring = prestring + string[:instance +1]
            string = string[instance +1:]
            
        #returns original string if case > actual incidence.
        if len(string) < 3:  
            return prestring + string
        instance = string.find('III')
    return string
    
# 4 omit instance of UU,   ***should add an "all" case to mutate all instances
def op4(string, case):
    incidence = 0  #to track incidence of 'UU'
    prestring = ''
    instance = string.find('UU')
    
    if case == 'all':
        while instance != -1:
            string = prestring + string[:instance] + string[instance + 2:]
            instance = string.find('UU')
        return string
    
    while instance != -1:
        incidence += 1
        
        # once intended case of "UU" is found, it's rplcd with ""
        if incidence == case:
            string = prestring + string[:instance] + string[instance + 2:]
            return string
            
        # if not instance specified in arg, searches rest of string
        else:
            prestring = prestring + string[:instance +1]
            string = string[instance +1:]
            
        #returns original string if case > actual incidence.
        if len(string) < 2:
            print "case doesn't exists."
            return prestring + string
        instance = string.find('UU')
        
    # if case of UU does NOT exist concatenate prestring with string
    if string[0] != 'M':
        print "case doesn't exists."
        return prestring + string
        
    return string
    
def repeat(op, case, iterations, string):
    i = 0
    while i < iterations:
        if op == 1:
            string = op1(string)
        if op == 2:
            string = op2(string)
        if op == 3:
            string = op3(string, case)
        if op == 4:
            string = op4(string, case)
        i += 1
    return string
    
string = 'MI'
print string
string = repeat(2, 0, 3, string)
print string
string = op3(string, 1)
print string
string = op1(string)
print string
string = op2(string)
print string
string = op4(string,1)
print string
string = op3(string, 'all')
print string
string = op2(string)
print string
