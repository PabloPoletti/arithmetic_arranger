def arithmetic_arranger(problems, show_answers=False):
    # Check if there are too many problems
    if len(problems) > 5:
        return "Error: Too many problems."

    # Initialize lists for each row of the formatted problems
    first_row = []
    second_row = []
    dashes = []
    answers = []

    # Loop through each problem and split it into parts
    for problem in problems:
        parts = problem.split()

        # Check if the operator is valid
        if parts[1] not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."

        # Check if the operands are valid
        if not parts[0].isdigit() or not parts[2].isdigit():
            return "Error: Numbers must only contain digits."

        # Check if the operands have too many digits
        if len(parts[0]) > 4 or len(parts[2]) > 4:
            return "Error: Numbers cannot be more than four digits."

        # Convert the operands to integers
        operand1 = int(parts[0])
        operand2 = int(parts[2])

        # Calculate the answer
        if parts[1] == "+":
            answer = operand1 + operand2
        else:
            answer = operand1 - operand2

        # Convert the operands and answer to strings
        operand1_str = str(operand1)
        operand2_str = str(operand2)
        answer_str = str(answer)

        # Determine the maximum length of the operands and answer
        max_length = max(len(operand1_str), len(operand2_str), len(answer_str))

        # Add padding to the left of each operand and answer
        operand1_formatted = operand1_str.rjust(max_length + 2)
        operand2_formatted = parts[1] + operand2_str.rjust(max_length + 1)
        answer_formatted = answer_str.rjust(max_length + 2)

        # Add each row to the list of rows
        first_row.append(operand1_formatted)
        second_row.append(operand2_formatted)
        dashes.append("-" * (max_length + 2))
        answers.append(answer_formatted)

    # Combine the rows into a single string, separated by four spaces
    arranged_problems = "    ".join(first_row) + "\n" + "    ".join(second_row) + "\n" + "    ".join(dashes)

    # If show_answers is True, add the answers to the string
    if show_answers:
        arranged_problems += "\n" + "    ".join(answers)

    return arranged_problems