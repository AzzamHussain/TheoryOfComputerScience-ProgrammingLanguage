import re

class Data_Type:
    def tokenize(self, text):
        tokens = []
        integer_pattern = re.compile(r'[-+]?\d+')

        for match in integer_pattern.finditer(text):
            tokens.append(('INTEGER', int(match.group())))

        return tokens