import re

class ConditionalStatementsLexer:
    def tokenize(self, text):
        tokens = []
        keywords = ["if", "else if", "else", "(", ")", "{", "}", ">", "<", ">=", "<=", "!=", "==", "%"]

        # Regular expression pattern to match keywords
        pattern = "|".join(re.escape(kw) for kw in keywords)
        keyword_pattern = re.compile(pattern)

        # Tokenize the text
        for match in keyword_pattern.finditer(text):
            tokens.append(('KEYWORD', match.group()))

        return tokens
