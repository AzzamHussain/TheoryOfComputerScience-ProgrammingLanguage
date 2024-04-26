import re

class Identifiers:
    def tokenize_identifiers(self, text):
        tokens = []
        identifier_pattern = re.compile(r'int[_a-zA-Z][_a-zA-Z0-9]{0,18}(\s*=\s*[-+]?\d+)?')

        for match in identifier_pattern.finditer(text):
            tokens.append(('IDENTIFIER', match.group()))

        return tokens