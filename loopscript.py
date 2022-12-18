from srcs.LPS import lex, execute, preprocess
import sys

# print("""
# ██       ██████   ██████  ██████  ███████  ██████ ██████  ██ ██████  ████████ 
# ██      ██    ██ ██    ██ ██   ██ ██      ██      ██   ██ ██ ██   ██    ██    
# ██      ██    ██ ██    ██ ██████  ███████ ██      ██████  ██ ██████     ██    
# ██      ██    ██ ██    ██ ██           ██ ██      ██   ██ ██ ██         ██    
# ███████  ██████   ██████  ██      ███████  ██████ ██   ██ ██ ██         ██
# """)

def main(infile):
    try:
        with open(infile, "r") as f:
            code = preprocess(f.read())
            tokens = lex(code)
            execute(tokens)
    except Exception as e:
        print(f"Error: {e}")
        return 1

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("error: no input files")
        sys.exit(1)
    main(sys.argv[1])