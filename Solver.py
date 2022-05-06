import re
algebra_equation = input("Enter algebric equation").replace(" ","")
x = re.split(r'(\D)', algebra_equation)
out = []

for i in x:
  if i == "":
    pass
  else:
    out.append(i)
    
equals = "".join(out[out.index("=")+1:])
equation = out[:out.index("=")]

print("\n\n")
algebra_rules = {"+":"-",
                 "-":"+",
                 "*":"/",
                 "/":"*"}

op = {'+': lambda x, y: x + y,
      '-': lambda x, y: x - y,
      '*': lambda x, y: x * y,
      '/': lambda x, y: x / y}
      
def solve():
  stack_output = equals
  for i in equation:
    if i in algebra_rules:
      print(" ".join(equation)+" = "+str(stack_output))
      lr = str(equation[equation.index(i)+1])
      rule = str(algebra_rules[i])
      
      spacer = " ".join(out).index("=")-(equation.index(i)+1)-3
      print(" "*(equation.index(i)+1)+rule+" "+lr+" "*spacer+" "+rule+lr+"\n")
      
      stack_output = op[str(rule)](int(stack_output),int(lr))
      
      del equation[equation.index(i)]
      del equation[equation.index(lr)]
      del out[out.index(i)]
      del out[out.index(lr)]      
     
  if "x" in equation and len(equation) == 1:
    print("".join(equation)+" = "+str(stack_output))
    
solve()
