class Calculator:
  def __init__(self, a, b, operation):
    self.a = float(a)
    self.b = float(b)
    self.operation = operation.lower()

  def calculate(self):
    if self.operation == 'add':
        return self.a + self.b
    elif self.operation == 'subtract':
        return self.a - self.b
    elif self.operation == 'multiply':
        return self.a * self.b
    elif self.operation == 'divide':
        if self.b != 0:
            return self.a / self.b
        else:
            return "Error: Division by zero"
    else:
        return "Invalid Operation"

  calc = Calculator(10.5, 15.5, 'add')
  print("Result: ",calc.calculate())
