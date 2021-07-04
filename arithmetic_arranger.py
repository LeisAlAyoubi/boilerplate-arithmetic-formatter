def arithmetic_arranger(arithmetic_list, return_answer=False):

  arranged_problems = []

  #check if list doesnt contain more than 5 arithmetic problems
  if len(arithmetic_list) > 5:
    return "Error: Too many problems."

  
  first_term = ""
  second_term = ""
  dashes = ""
  solution = "" 
  
  for arithmetic_term in arithmetic_list:

    #print(arithmetic_term)
    #check if arithmetic expression has + or - signs
    if(("+" not in arithmetic_term) and ("-" not in arithmetic_term)):
      return "Error: Operator must be '+' or '-'."
    
    #find arithmetic operator and slice string to arithmetic terms
    plus_pos = arithmetic_term.find('+')
    minus_pos = arithmetic_term.find('-')

    if plus_pos != -1:
      exp1 = arithmetic_term[:plus_pos]
      exp2 = arithmetic_term[plus_pos+1:]
      exp1 = exp1.strip()
      exp2 = exp2.strip()
      sign = '+'

      #Exclude terms which contain non-number characters
      if(exp1.isdigit() == False) or (exp2.isdigit() == False):
        return "Error: Numbers must only contain digits."

      problem_solution = int(exp1) + int(exp2)

    elif minus_pos != -1:
      exp1 = arithmetic_term[:minus_pos]
      exp2 = arithmetic_term[minus_pos+1:]
      exp1 = exp1.strip()
      exp2 = exp2.strip()
      sign = '-'
      sign = sign.strip()

      #Exclude terms which contain non-number characters
      if(exp1.isdigit() == False) or (exp2.isdigit() == False):
        return "Error: Numbers must only contain digits."

      problem_solution = int(exp1) - int(exp2)

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

    if(arithmetic_term != arithmetic_list[len(arithmetic_list)-1]):
      first_term += " " * (2 + len(str(big_term)) - len(str(exp1))) + exp1 + "    "
      second_term +=sign + " " * (1 + len(str(big_term)) - len(str(exp2)))+ exp2 + "    "
      dashes +="-" * len(big_term) + "--" + "    "
    else:
      first_term += " " * (2 + len(str(big_term)) - len(str(exp1))) + exp1
      second_term += sign + " " * (1 + len(str(big_term)) - len(str(exp2)))+ exp2
      dashes += "-" * len(big_term) + "--"

    if(return_answer == True):
      if(arithmetic_term != arithmetic_list[len(arithmetic_list)-1]):
        solution += " " * ( 2+ len(str(big_term)) - len(str(problem_solution))) + str(problem_solution) + "    "
        arranged_problems =first_term + "\n" +  second_term + "\n" + dashes + "\n" +solution
      else:
        solution += " " * ( 2+ len(str(big_term)) - len(str(problem_solution))) + str(problem_solution)
        arranged_problems =first_term + "\n" +  second_term + "\n" + dashes + "\n" +solution

    else:
      arranged_problems =first_term + "\n" +  second_term + "\n" + dashes
    
  return arranged_problems
