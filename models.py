SQLAlchemy Models

from config import db

class Rule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rule_string = db.Column(db.String, nullable=False)
    ast_json = db.Column(db.JSON, nullable=False)

def save_rule(rule_string, ast_json):
    rule = Rule(rule_string=rule_string, ast_json=ast_json)
    db.session.add(rule)
    db.session.commit()
