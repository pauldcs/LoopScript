import re

click_regex = re.compile(
    r"CLICK[\s\t\n]+"
    r"\((?P<minX>\d+),[\s\t\n]+(?P<minY>\d+)\)[\s\t\n]+"
    r"\((?P<maxX>\d+),[\s\t\n]+(?P<maxY>\d+)\)[\s\t\n]+"
    r"\((?P<duration>[\d.]+),[\s\t\n]+(?P<wait>[\d.]+)\)"
)
type_regex = re.compile(
    r"WRITE[\s\t\n]+\"(?P<str>.*)\""
)
type_rtext_regex = re.compile(
    r"WRITE_RTEXT[\s\t\n]+(?P<n_words>\d+)"
)
type_rstr_regex = re.compile(
    r"WRITE_RSTR[\s\t\n]+(?P<n_chars>\d+)"
)
wait_regex = re.compile(
    r"WAIT[\s\t\n]+(?P<n_secs>\d+)"
)

def preprocess(text):
    lines = text.split("\n")
    lines = [line.split("#")[0].strip() for line in lines]
    return "\n".join(lines)


def parse_command(command):
	click_match = click_regex.search(command)
	if click_match:
		operands = click_match.groupdict()
		print(operands)
		return

	write_match = type_regex.search(command)
	if write_match:
		operands = write_match.groupdict()
		print(operands)
		return

	write_rtext_match = type_rtext_regex.search(command)
	if write_rtext_match:
		operands = write_rtext_match.groupdict()
		print(operands)
		return

	write_rstr_match = type_rstr_regex.search(command)
	if write_rstr_match:
		operands = write_rstr_match.groupdict()
		print(operands)
		return
		
	wait_match = wait_regex.search(command)
	if wait_match:
		operands = wait_match.groupdict()
		print(operands)
		return
	
	else:
		print(f"Error: invalid command '{command}'")

def parse_commands(commands):
	for command in commands:
		parse_command(command)
