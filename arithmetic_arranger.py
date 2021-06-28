def arithmetic_arranger(arithmetic_list, return_answer=False):

  arranged_problems = []

  #check if list doesnt contain more than 5 arithmetic problems
  if len(arithmetic_list) > 5:
    return "Error: Too many problems."
  
  for arithmetic_term in arithmetic_list:
    #check if arithmetic expression has + or - signs
    if(('+' not in arithmetic_term) or ('-' not in arithmetic_term)):
      return "Error: Operator must be '+' or '-'."
    
    #find arithmetic operator and slice string to arithmetic terms
    plus_pos = arithmetic_term.find('+')
    minus_pos = arithmetic_term.find('-')

    if plus_pos == True:
      exp1 = arithmetic_term[:plus_pos]
      exp2 = arithmetic_term[plus_pos:]
      sign = '+'
    else:
      exp1 = arithmetic_term[:minus_pos]
      exp2 = arithmetic_term[minus_pos:]
      sign = '-'

    #Dont except numbers with more than for digits
    if(len(exp1)> 4 or len(exp2)> 4 ):
      return "Error: Numbers cannot be more than four digits."

    #find the bigger term
    if(len(exp1) >= len(exp2)):
      big_term = exp1
      small_term = exp2
    else: 
      big_term = exp2
      small_term = exp1
    
    #Exclude terms which contain non-number characters
    if(big_term.isdigit() == False or small_term.isdigit() == False):
      return "Error: Numbers must only contain digits."

    arranged_term = exp1 + '\n' + sign + exp2

    arranged_problems.append(arranged_term)
    
    return arranged_problems