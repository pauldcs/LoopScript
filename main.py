from srcs.LoopScript import lex
from srcs.LoopScript import parse
import argparse
import sys

def preprocess(text):
    lines = text.split("\n")
    lines = [line.split("#")[0].strip() for line in lines]
    return "\n".join(lines)

def traverse(node, indent=0):
    print("    " * indent + "└── " + str(node))
    for child in node.children:
        traverse(child, indent=indent+1)

def main(script_file):
	try:
		with open(script_file, "r") as f:
			raw = f.read()
			script = preprocess(raw)
			tokens = lex(script.strip())
			ast = parse(tokens)
			traverse(ast)
	except IOError as e:
		print(f"An error occurred while reading '{script_file}': {e}")
		sys.exit(1)

if __name__ == "__main__":
	parser = argparse.ArgumentParser( 
		description="Run a script written in the GUI automation scripting language"
	)
	parser.add_argument(
		"script_file",
		help="the script file to run"
	)
	args = parser.parse_args()
	main(args.script_file)