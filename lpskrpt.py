from srcs.skrpt import lex, parse, traverse, execute
import sys

print("""\
.__                __                   __                   
|  | ______  _____|  | ________________/  |_   ______ ___.__.
|  | \____ \/  ___/  |/ /\_  __ \____ \   __\  \____ <   |  |
|  |_|  |_> >___ \|    <  |  | \/  |_> >  |    |  |_> >___  |
|____/   __/____  >__|_ \ |__|  |   __/|__| /\ |   __// ____|
     |__|       \/     \/       |__|        \/ |__|   \/""")

def preprocess(text):
    lines = text.split("\n")
    lines = [line.split("#")[0].strip() for line in lines]
    return "\n".join(lines)

def main(infile):
	try:
		with open(infile, "r") as f:
			code = preprocess(f.read())
			ast = parse(lex(code))
			print(".")
			traverse(ast)
			#execute(ast)
	except Exception as e:
		print(f"An error occurred: {e}")
		return 1

if __name__ == "__main__":
	if len(sys.argv) < 2:
		print("error: no input files")
		sys.exit(1)
	main(sys.argv[1])