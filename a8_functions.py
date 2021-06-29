def sum_digit_string(my_str): 
    """
    -------------------------------------------------------
    Sums all the digits in my_str, ignores non-digit characters
    Use: total = sum_digit_string (my_str)
    -------------------------------------------------------
    Parameters: 
         my_str: string that has single-digit numbers (str) 
    returns total: 
         sum of all the single digit number (integer >= 0) 
    -------------------------------------------------------
    """ 
    total = 0
    if my_str == "":
        total = None
    else:    
        for ch in my_str:
            if ch.isdigit() == True:
                total += int(ch)   
    return total    


def find_frequent(my_str): 
    """
    -------------------------------------------------------
    Find the character(s) that occur the most in a string  
    Use: value = find_frequent(my_str)
    -------------------------------------------------------
    Parameters: 
         my_str: string (str) 
    returns: 
         value - a list of all the ch that occured the most in the string (list) 
    -------------------------------------------------------
    """ 
    maxi = 0
    if my_str == "":
        value = None
    else:   
        value = [] 
        for ch in my_str:
            if ch != " ":
                if my_str.count(ch) > maxi: 
                    maxi = my_str.count(ch)
        for ch in my_str:
            if ch != " ":
                if my_str.count(ch) == maxi: 
                    value.append(ch) 
        value = list(dict.fromkeys(value))                         
    return value 

        
def string_capitalizer(my_str):
    """
    -------------------------------------------------------
    capitalizes all characthers that should be capatilzed in a phrase
    Use: new_str = string_capitalizer(my_str)
    -------------------------------------------------------
    Parameters: 
         my_str: string (str) 
    returns: 
         new_str: capaitalised string
    -------------------------------------------------------
    """ 
    new_str = my_str
    count = 0
    if my_str == "":
        new_str = None
    else:
        for ch in my_str:
            if count == 0:
                new_str = ch.upper() + new_str[count + 1:]             
            elif (ch == "." or ch == "?") and count < len(my_str) - 1:
                count2 = 0
                new_str2 = new_str[count + 1:]
                for ch2 in new_str2:
                    if ch2 != " ":
                        new_str = new_str[0:(count + 1) + (count2)] + new_str2[count2].upper() + new_str2[count2 + 1:]
                        break
                    count2 += 1
            count += 1      
    return new_str

        
def is_word_chain (my_list):
    """
    -------------------------------------------------------
    Checks if a list of words is a word chain
    Use: value = is_word_chain (my_list)
    -------------------------------------------------------
    Parameters: 
         my_list: a list of strings (list)
    returns value: 
         true: if the list is a word chain 
         false: if the list is not a word chain
    -------------------------------------------------------
    """ 
    count = 0
    countF = 0 
    value = False 
    for i in my_list:
        new_i = i.replace(" ", "")
        if count < len(my_list) - 1: 
            if new_i[len(new_i) - 1] == my_list[count + 1][0]:
                value = True
            else:
                countF += 1        
        count += 1
    if countF > 0:
        value = False
    return value
    
