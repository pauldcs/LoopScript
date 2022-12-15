import argparse
import sys

from srcs.script_interpreter import preprocess
from srcs.script_interpreter import parse_commands

def main(script_file):
	try:
		with open(script_file, "r") as f:
			raw = f.read()
			script = preprocess(raw)
			lines = script.split(";")
			lines = [line.strip() for line in lines]
			parse_commands(lines)
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
	parser.add_argument(
		"-v", "--verbose",
		action="store_true",
		help="print verbose output"
	)
	args = parser.parse_args()
	main(args.script_file)