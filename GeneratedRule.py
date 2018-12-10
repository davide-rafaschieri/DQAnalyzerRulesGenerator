class GeneratedRule:

    def __init__(self, column_name, pattern_value, pattern_num_cases, pattern_percent, rule_name, rule_description, rule_pattern, rule_expression):
        self.column_name = column_name
        self.pattern_value = pattern_value
        self.pattern_num_cases = pattern_num_cases
        self.pattern_percent = pattern_percent
        self.rule_name = rule_name
        self.rule_description = rule_description
        self.rule_pattern = rule_pattern
        self.rule_expression = rule_expression

    def __eq__(self, other):
        return self.rule_expression == other.rule_expression

    def __hash__(self):
        return hash(('expression', self.rule_expression))
