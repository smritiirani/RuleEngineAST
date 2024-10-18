app.py - Flask API Application
pyhon


from flask import Flask, request, jsonify
from ast import create_rule
from rule_evaluator import evaluate_rule
from rule_combiner import combine_rules

app = Flask(__name__)

@app.route('/create_rule', methods=['POST'])
def create_rule_endpoint():
    data = request.get_json()
    rule_string = data['rule_string']
    ast = create_rule(rule_string)
    return jsonify(ast)

@app.route('/combine_rules', methods=['POST'])
def combine_rules_endpoint():
    data = request.get_json()
    rules = data['rules']
    combined_ast = combine_rules(rules)
    return jsonify(combined_ast)

@app.route('/evaluate_rule', methods=['POST'])
def evaluate_rule_endpoint():
    data = request.get_json()
    ast = data['ast']
    user_data = data['user_data']
    result = evaluate_rule(ast, user_data)
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
