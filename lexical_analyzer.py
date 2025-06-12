import nltk
import re
nltk.download('punkt')

f = open('InputProgForPythonCode.c', 'r')
program = f.read()
count = 0

Identifiers_Output = []
Keywords_Output = []
Symbols_Output = []
Operators_Output = []
Numerals_Output = []
Headers_Output = []

def remove_Spaces(program):
    scanned_Program = []
    for line in program:  # Changed 'prog' to 'program'
        if (line.strip() != ''):
            scanned_Program.append(line.strip())
    return scanned_Program

def remove_Comments(program):
    program_Multi_Comments_Removed = re.sub("/\*[^*]*\*+(?:[^/*][^*]*\*+)*/", "", program)
    program_Single_Comments_Removed = re.sub("//.*", "", program_Multi_Comments_Removed)
    return program_Single_Comments_Removed

RE_Keywords = r"\b(auto|break|case|char|const|continue|default|do|double|else|enum|extern|float|for|goto|if|int|long|register|return|short|signed|sizeof|static|struct|switch|typedef|union|unsigned|void|volatile|while|string|class|struc|include)\b"
RE_Operators = r"(\+)|(-)|(=)|(\*)|(/)|(%)|(--)|(<=)|(>=)"
RE_Numerals = r"^\d+$"  # Adjust as needed for more complex numerals
RE_Special_Characters = r"[\[@&~!#$\^\|{}\]:;<>?,\.']|\(\)|\(|\)|{}|\[\]|\""
RE_Identifiers = r"^[a-zA-Z_][a-zA-Z0-9_]*"
RE_Headers = r"([a-zA-Z]+\.[h])"

program_Comments_removed = remove_Comments(program)
prog = program_Comments_removed.split('\n')
scanned_Prog = remove_Spaces(prog)

scanned_Program = '\n'.join([str(elem) for elem in scanned_Prog])
scanned_Program_lines = scanned_Program.split('\n')
Source_Code = [line for line in scanned_Program_lines]

for line in Source_Code:
    count += 1
    if line.startswith("#include"):
        tokens = nltk.wordpunct_tokenize(line)
    else:
        tokens = nltk.wordpunct_tokenize(line)
    for token in tokens:
        if re.findall(RE_Keywords, token):
            Keywords_Output.append(token)
        elif re.findall(RE_Headers, token):
            Headers_Output.append(token)
        elif re.findall(RE_Operators, token):
            Operators_Output.append(token)
        elif re.findall(RE_Numerals, token):
            Numerals_Output.append(token)
        elif re.findall(RE_Special_Characters, token):
            Symbols_Output.append(token)
        elif re.findall(RE_Identifiers, token):
            Identifiers_Output.append(token)

print("This Program is run by Newton Tiwari - 1244")
print("There Are", len(Keywords_Output), "Keywords:", Keywords_Output)
print("\n")
print("There Are", len(Identifiers_Output), "Identifiers:", Identifiers_Output)
print("\n")
print("There Are", len(Headers_Output), "Header Files:", Headers_Output)
print("\n")
print("There Are", len(Symbols_Output), "Symbols:", Symbols_Output)
print("\n")
print("There Are", len(Numerals_Output), "Numerals:", Numerals_Output)
print("\n")
