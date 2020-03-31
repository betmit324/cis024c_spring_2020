import argparse
import sys
import add
import subtract

def calculator(operator,operands,verbosity):

    n1,n2 = operands.split(',')
    n1 = int(n1)
    n2 = int(n2)

    if operator == "+":
        result = add.add(n1,n2)
    elif operator == "-":
        result = subtract.subtract(n1,n2)
        
    if verbosity:
    	print("Operator:",operator,end="***")
    	print("Operands:",operands,end="***")

    print("Result:", result)

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    #parser.add_argument("--verbosity", help="increase output verbosity")
    #parser.add_argument("--verbosity", help="increase output verbosity",action="store_true" )
    parser.add_argument("--operator",   default="+", help="operator. supported values are + and -")
    parser.add_argument("--operands",   default="2,3",help="operands. enter comma separated list of operands")
    parser.add_argument("-v","--verbosity", help="increase output verbosity",action="store_true" )
    args = parser.parse_args()

    print("Verbosity flag is:",args.verbosity, type(args.verbosity))
    
    operator = args.operator
    operands = args.operands

    calculator(operator,operands,args.verbosity)
