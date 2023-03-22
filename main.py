import operator

ops = {"+": operator.add, "-": operator.sub}


def arithmetic_arranger(problems):
  #Error check
  if len(problems) > 4:
    print("Error: Too many problems.")

  firstline = ""
  secondline = ""
  dashline = ""
  totalline = ""

  f = 0
  for n in problems:
    fnum = n.split()[0]
    operator = n.split()[1]
    snum = n.split()[2]

    #Error check
    if operator != "+" and operator != "-":
      print("Error: Operator must be '+' or '-'.")
    if len(fnum) > 4 or len(snum) > 4:
      print("Error: Numbers cannot be more than four digits.")
    if not fnum.isnumeric() or not snum.isnumeric():
      print("Error: Numbers must only contain digits.")

    total = ops[operator](int(fnum), int(snum))

    maxlen = max(len(fnum), len(snum)) + 2
    firstline = firstline + fnum.rjust(maxlen) + (4 * " ")
    secondline = secondline + operator + snum.rjust(maxlen - 1) + (4 * " ")
    dashline = dashline + "-" * (maxlen) + (4 * " ")
    totalline = totalline + str(total).rjust(maxlen) + (" " * 4)

    f += 1
    if f == len(problems):
      print(firstline)
      print(secondline)
      print(dashline)
      print(totalline + "\n")


arithmetic_arranger(["256 + 15", "8 - 63", "327 - 96", "5668 + 789"])
