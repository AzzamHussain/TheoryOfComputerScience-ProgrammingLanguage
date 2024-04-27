from Data_Type import Data_Type
from var import Identifiers
from conditional_statement import ConditionalStatementsLexer
from loops import TraverseLoop, UntilLoop

def main():
    # Sample input code
    input_code = "int x = +123; int y = -456;"

    # Create lexer instance for data type
    datatype = Data_Type()

    # Tokenize the input code for data type
    tokens_data_type = datatype.tokenize(input_code)

    ################### IDENTIFIERS #######################

    # Sample input code for identifiers
    input_codeV = "int x = +123; int y = -456;"

    # Create lexer instance for identifiers
    identifier = Identifiers()

    # Tokenize the identifiers in the input code
    tokens_identifiers = identifier.tokenize_identifiers(input_codeV)

    ################### CONDITIONAL STATEMENTS #######################

    # Sample input code for conditional statements
    input_codeC = "if (x > 0) { print('x is positive'); } else if (x == 0) { print('x is zero'); } else { print('x is negative'); }"

    # Create lexer instance for conditional statements
    lexer = ConditionalStatementsLexer()

    # Tokenize the input code for conditional statements
    tokens_conditional = lexer.tokenize(input_codeC)

    ################### LOOPS #######################

    # Sample Traverse loop
    traverse_loop = TraverseLoop(
        initialization="i = 0",
        condition1="i < 5",
        condition2="i >= 0",
        counter="i += 1",
        body_statements=["print(i)"]
    )
    traverse_loop.execute()

    # Sample Until loop
    until_loop = UntilLoop(
        data_type="int",
        var_name="x",
        value="0",
        condition="x == 5",
        body_statements=["print(x)"],
        counter_statement="x += 1"
    )
    until_loop.execute()

    # Print the tokens
    print("Data Type Tokens:", tokens_data_type)
    print("Identifier Tokens:", tokens_identifiers)
    print("Conditional Statement Tokens:", tokens_conditional)

if __name__ == "__main__":
    main()
