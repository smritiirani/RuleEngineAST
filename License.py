

---

9. **tests/** - Unit Tests for Rule Engine

**tests/test_rule_engine.py**

```python
import unittest
from ast import create_rule
from rule_evaluator import evaluate_rule

class TestRuleEngine(unittest.TestCase):
    def test_create_rule(self):
        rule = "age > 30 AND department = 'Sales'"
        ast = create_rule(rule)
        self.assertIsNotNone(ast)
    
    def test_evaluate_rule(self):
        rule = "age > 30 AND department = 'Sales'"
        ast = create_rule(rule)
        user_data = {"age": 35, "department": "Sales"}
        result = evaluate_rule(ast, user_data)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
