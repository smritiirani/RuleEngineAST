Logic to Combine Multiple ASTs

def combine_rules(rules):
    asts = [create_rule(rule) for rule in rules]
    while len(asts) > 1:
        left = asts.pop(0)
        right = asts.pop(0)
        combined = Node(node_type='operator', left=left, right=right, value='AND')
        asts.append(combined)
    return asts[0]
