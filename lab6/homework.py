def check_length(elements):
    if len(elements) != 3:
        raise ValueError(
            "Błędne wejście - powinny być trzy elementy oddzielone odstępami: 'liczba op liczba', zamiast liczby może być x (wynik ostatniego działania).")


def check_operand(x, operand):
    if operand == 'x':
        return x

    try:
        operand = float(operand)
    except ValueError:
        raise ValueError("Pierwszy i trzeci element to muszą być liczby lub x (oznacza wynik ostatniego działania).")

    return operand


def check_operator_and_process(operator, left_operand, right_operand):
    if operator == '+':
        return left_operand + right_operand
    elif operator == '-':
        return left_operand - right_operand
    elif operator == '*':
        return left_operand * right_operand
    elif operator == '/':
        return left_operand / right_operand
    else:
        raise ValueError("Środkowy element nie jest symbolem operacji.")


def calculate(x, expression):
    try:
        elements = expression.split()
        check_length(elements)
        left_operand, operator, right_operand = elements
        left_operand = check_operand(x, left_operand)
        right_operand = check_operand(x, right_operand)
        result = check_operator_and_process(operator, left_operand, right_operand)
    except ZeroDivisionError:
        raise ZeroDivisionError("Dzielenie przez 0")
    except ValueError as e:
        raise ValueError(str(e))

    return result


def calculator():
    x = 0.0
    while True:
        try:
            user_input = input(">>> ")
            if user_input.lower() == "exit":
                print("Do widzenia")
                break
            x = calculate(x, user_input)
            print(x)
        except ZeroDivisionError as zde:
            print(zde)
        except ValueError as ve:
            print(ve)


if __name__ == "__main__":
    calculator()
