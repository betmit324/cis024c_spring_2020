
import add
import subtract

def calculator():
    operator = input("Enter the operator (+/-):")
    operands = input("Enter the operands (comma separated): ")

    n1,n2 = operands.split(',')
    n1 = int(n1)
    n2 = int(n2)

    if operator == "+":
        result = add.add(n1,n2)
    elif operator == "-":
        result = subtract.subtract(n1,n2)
        
    print("Operator:",operator)
    print("Operands:",operands)
    print("Result:", result)

if __name__ == "__main__":
    calculator()


