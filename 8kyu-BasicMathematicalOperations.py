# Your task is to create a function that does four basic mathematical operations.
# The function should take three arguments - operation(string/char), value1(number), value2(number).
# The function should return result of numbers after applying the chosen operation.

def basic_op(operator, value1, value2):
    # your code here
    if operator == "+":
        result = value1 + value2
    elif operator == "-":
        result = value1 - value2
    elif operator == "*":
        result = value1 * value2
    elif operator == "/":
        if value2 != 0:
            result = value1 / value2
        else:
            raise ValueError("Não é possível dividir por zero")
    else:
        raise ValueError("Operador desconhecido")
    return result