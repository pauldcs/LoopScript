from srcs.LPS import lex, execute, preprocess
import sys
import re

def preprocess(code):
    const_regex = re.compile(r'const\s+(\w+)\s+(.+);')
    constants = {}
    for match in const_regex.finditer(code):
        name, value = match.groups()
        constants[name] = value
        code = code.replace(match.group(0), '')
    for name, value in constants.items():
        code = code.replace(f'${name}', value)
    lines = code.split("\n")
    lines = [line.split("#")[0].strip() for line in lines]
    return "\n".join(lines).strip()

def main(infile):
    try:
        with open(infile, "r") as f:
            code = preprocess(f.read())
            execute(lex(code))
            #print(code)
    except Exception as e:
        print(f"Error: {e}")
        return 1

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("error: no input files")
        sys.exit(1)
    main(sys.argv[1])