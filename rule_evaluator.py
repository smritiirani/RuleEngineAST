Logic to Evaluate Rules


def evaluate_node(node, user_data):
    if node.type == 'operand':
        attribute, operator, value = parse_operand(node.value)
        return compare(user_data[attribute], operator, value)
    elif node.type == 'operator':
        left_result = evaluate_node(node.left, user_data)
        right_result = evaluate_node(node.right, user_data)
        if node.value == 'AND':
            return left_result and right_result
        elif node.value == 'OR':
            return left_result or right_result

def parse_operand(operand_string):
    # Parse strings like "age > 30" into components
    for operator in ['>', '<', '=', '!=']:
        if operator in operand_string:
            attribute, value = operand_string.split(operator)
            return attribute.strip(), operator, value.strip()

def compare(left, operator, right):
    if operator == '>':
        return left > int(right)
    elif operator == '<':
        return left < int(right)
    elif operator == '=':
        return left == right
    elif operator == '!=':
        return left != right

def evaluate_rule(ast, user_data):
    return evaluate_node(ast, user_data)
