ast.py - AST Logic (Node, Rule Parsing)

class Node:
    def __init__(self, node_type, left=None, right=None, value=None):
        self.type = node_type  # 'operator' or 'operand'
        self.left = left       # Left child for operators
        self.right = right     # Right child for operators
        self.value = value     # Value for operand nodes

def create_rule(rule_string):
    # Simplified rule parsing logic
    tokens = rule_string.split()  # This can be enhanced with a proper parser
    stack = []
    
    for token in tokens:
        if token == 'AND' or token == 'OR':
            right = stack.pop()
            left = stack.pop()
            stack.append(Node(node_type='operator', left=left, right=right, value=token))
        else:
            stack.append(Node(node_type='operand', value=token))
    
    return stack.pop()  # The root of the AST

