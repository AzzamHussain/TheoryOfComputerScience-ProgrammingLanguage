from Data_Type import Data_Type
from var import Identifiers

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

    # Print the tokens
    print("Data Type Tokens:", tokens_data_type)
    print("Identifier Tokens:", tokens_identifiers)

if __name__ == "__main__":
    main()
