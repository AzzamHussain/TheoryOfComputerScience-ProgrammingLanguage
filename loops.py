
class TraverseLoop:
    def __init__(self, initialization, condition1, condition2, counter, body_statements):
        self.initialization = initialization
        self.condition1 = condition1
        self.condition2 = condition2
        self.counter = counter
        self.body_statements = body_statements

    def execute(self):
        exec(self.initialization)
        while eval(self.condition1) and eval(self.condition2):
            for statement in self.body_statements:
                exec(statement)
            exec(self.counter)

class UntilLoop:
    def __init__(self, data_type, var_name, value, condition, body_statements, counter_statement):
        self.data_type = data_type
        self.var_name = var_name
        self.value = value
        self.condition = condition
        self.body_statements = body_statements
        self.counter_statement = counter_statement

    def execute(self):
        # exec(f"{self.data_type} {self.var_name} = {self.value}")
        # exec(f"{self.data_type}({self.var_name}) = {self.value}")
        exec(f"{self.var_name} = int({self.value})")

        while not eval(self.condition):
            for statement in self.body_statements:
                exec(statement)
            exec(self.counter_statement)
