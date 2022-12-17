from srcs.LPS import lex, parse, traverse
import sys

def preprocess(text):
    lines = text.split("\n")
    lines = [line.split("#")[0].strip() for line in lines]
    return "\n".join(lines)

def main(infile):
	try:
		with open(infile, "r") as f:
			code = preprocess(f.read())
			ast = parse(lex(code))
			traverse(ast)
	except Exception as e:
		print(f"An error occurred: {e}")
		return 1

if __name__ == "__main__":
	if len(sys.argv) < 2:
		print("error: no input files")
		sys.exit(1)
	main(sys.argv[1])