from Data_Type import Data_Type
#import Data_Type

def main():
    # Sample input code
    input_code = "int x = +123; int y = -456;"

    # Create lexer instance
    datatype = Data_Type()

    # Tokenize the input code
    tokens = datatype.tokenize(input_code)

    # Print the tokens
    print(tokens)

if __name__ == "__main__":
    main()
