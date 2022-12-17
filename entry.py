from srcs.LPS import lex, execute, preprocess
import sys

def main(infile):
	try:
		with open(infile, "r") as f:
			code = preprocess(f.read())
			lexed = lex(code)
			for i in lexed:
				print(i)
			execute(lexed)
	except Exception as e:
		print(f"Error: {e}")
		return 1

if __name__ == "__main__":
	if len(sys.argv) < 2:
		print("error: no input files")
		sys.exit(1)
	main(sys.argv[1])