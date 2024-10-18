# RuleEngineAST
A rule engine is a system that applies business logic or decision-making rules to data input to automate decision processes. Using an Abstract Syntax Tree (AST) in a rule engine provides a flexible way to represent and evaluate these rules dynamically
Project Overview
This project implements a Rule Engine that uses an Abstract Syntax Tree (AST) to dynamically represent and evaluate business rules. The Rule Engine allows for the creation, combination, and evaluation of rules based on user-defined conditions such as age, department, income, experience, etc. The rules are parsed into an AST structure, allowing for flexibility in managing complex rules and optimizing evaluation.

Features
Create Rules: Parse rule strings into ASTs for easier management and evaluation.
Combine Rules: Merge multiple rules into a single AST to reduce redundant evaluations and enhance performance.
Evaluate Rules: Evaluate user attributes against predefined rules to determine eligibility.
Dynamic Modifications: Modify rules dynamically by adding or removing conditions, changing operators, etc.
Error Handling: Detect and report invalid rule strings or user data formats.
Extensibility: Built with a modular design to allow easy extension for advanced rule types or new features.
Technologies
Backend: Python (Flask)
Data Storage: PostgreSQL (with SQLAlchemy ORM)
AST Representation: Custom Node-based class structure
API: RESTful API for rule management and evaluation
Testing: Unit tests using unittest
Architecture
This project is structured as a 3-tier application:

Frontend: Simple UI or Postman to test API.
API Layer: Provides endpoints to create, combine, and evaluate rules.
Backend Logic: The core logic of rule parsing, AST generation, and evaluation.
Database: Stores rules in a relational database with metadata.

