from srcs.LoopScript import lex, parse
from srcs.execute import traverse

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
	main("test.s")