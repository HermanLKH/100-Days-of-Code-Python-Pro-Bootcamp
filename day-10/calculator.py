from art import logo

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
	"+": add,
	"-": subtract,
	"*": multiply,
	"/": divide
}

def calculator():
  should_continue = True

  num1 = float(input("What's the first number? "))

  for symbol in operations:
    print(symbol)

  while should_continue:
    operation_symbol = input("Pick an operation: ")

    num2 = float(input("What's the next number? "))

    answer = operations[operation_symbol](num1, num2)

    print(f"{num1} {operation_symbol} {num2} = {answer}")

    calculator_option = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation, or type 'e' to exit: ")

    if calculator_option == "y":
      num1 = answer
    elif calculator_option == "n":
      calculator()
    else:
      should_continue = False

print(logo)
calculator()