from random import randint, uniform
from srcs.act import move_cursor, click_spot, human_type, generate_random_string
from srcs.text import generate_random_text
import re
import sys
import datetime

TT_MOVE     = 'TT_MOVE'
TT_CLICK    = 'TT_CLICK'
TT_TYPE     = 'TT_TYPE'
TT_DEL      = 'TT_DEL'
TT_LOOP     = 'TT_LOOP'
TT_LOOP_END = 'TT_LOOP_END'
TT_RTEXT    = 'TT_RTEXT'
TT_RSTR     = 'TT_RSTR'


def choose_random_int(a: int, b: int) -> int:
    return randint(a, b)

def choose_random_float(a: float, b: float) -> float:
    return uniform(a, b)

loop_regex = re.compile(
    r"""
        loop\s+
        (?P<count>\d+)
    """, re.VERBOSE)

del_regex = re.compile(
    r"""
        del\s+
        (?P<count>\d+)
    """, re.VERBOSE)

move_regex = re.compile(
    r"""
        mov\s+
        \(
        (?P<min_x>\d+),\s+
        (?P<min_y>\d+)\),\s+
        \(
        (?P<max_x>\d+),\s+
        (?P<max_y>\d+)\),\s+
        (?P<duration>[\d.]+)
    """, re.VERBOSE)

click_regex = re.compile(
    r"click\s+(left|right|double)",
    re.IGNORECASE)

end_regex = re.compile(
    r"end",
    re.IGNORECASE)

click_regex = re.compile(
    r"click\s+(left|right|double)",
    re.IGNORECASE)

rtext_regex = re.compile(
    r"""rtxt\s+\(
        (?P<min>\d+),\s+
        (?P<max>\d+)\)
    """,
    re.IGNORECASE
        | re.VERBOSE)
rstr_regex = re.compile(
    r"""rstr\s+\(
        (?P<min>\d+),\s+
        (?P<max>\d+)\)
    """,
    re.IGNORECASE
        | re.VERBOSE)

type_regex = re.compile(
	r"""
		type\s+
		"(?P<str>.*?)"
	""",re.VERBOSE
            | re.DOTALL
            | re.MULTILINE)

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

def lex(code):
    tokens = []
    unbalanced = 0
    commands = code.split(";")
    cmd_number = 1
    for cmd in commands[:-1]:
        cmd = cmd.strip()
        loop_match  = loop_regex.search(cmd)
        end_match   = end_regex.search(cmd)
        move_match  = move_regex.search(cmd)
        click_match = click_regex.search(cmd)
        type_match  = type_regex.search(cmd)
        del_match   = del_regex.search(cmd)
        rtext_match = rtext_regex.search(cmd)
        rstr_match  = rstr_regex.search(cmd)
        if loop_match:
            unbalanced += 1
            count = int(loop_match.group("count"))
            tokens.append((TT_LOOP, count))
        elif end_match:
            unbalanced -= 1
            tokens.append((TT_LOOP_END, None))
        elif move_match:
            min_x = int(move_match.group("min_x"))
            min_y = int(move_match.group("min_y"))
            max_x = int(move_match.group("max_x"))
            max_y = int(move_match.group("max_y"))
            duration = float(move_match.group("duration"))
            tokens.append(
                (TT_MOVE, (
                    (min_x, min_y),
                    (max_x, max_y),
                    duration)))
        elif click_match:
            button = click_match.group(1)
            tokens.append((TT_CLICK, button))
        elif type_match:
            str = type_match.group("str")
            tokens.append((TT_TYPE, str))
        elif del_match:
            count = del_match.group("count")
            tokens.append((TT_DEL, count))
        elif rtext_match:
            min_count = int(rtext_match.group("min"))
            max_count = int(rtext_match.group("max"))
            tokens.append((TT_RTEXT, choose_random_int(min_count, max_count)))
        elif rstr_match:
            min_count = int(rstr_match.group("min"))
            max_count = int(rstr_match.group("max"))
            tokens.append((TT_RSTR, choose_random_int(min_count, max_count)))
        else:
            print(f"loop_script: lex error on command {cmd_number}: '{cmd}'")
            sys.exit(1)
        cmd_number += 1
    if (unbalanced):
        print(f"loop_script: Error: loops must be delimited by a 'end'")
        sys.exit(1)
    return tokens

def execute(tokens):
    stack = []
    i = 0
    while i < len(tokens):
        token = tokens[i]
        token_type = token[0]
        if token_type == TT_LOOP:
            stack.append((i, token))
            i += 1
        elif token_type == TT_LOOP_END:
            if not stack:
                raise Exception("Unbalanced loop block")
            loop_start_index, loop_start_token = stack.pop()
            loop_count = loop_start_token[1]
            loop_block = tokens[loop_start_index + 1:i]
            for j in range(loop_count):
                execute(loop_block)
            i += 1
        else:
            execute_token(token)
            i += 1
    if stack:
        raise Exception("Unbalanced loop block")

def execute_token(token):
    now = datetime.datetime.now()
    time_str = now.strftime("%H:%M:%S")
    name = sys.argv[1]
    #time_str = ""
    token_type = token[0]
    if token_type == TT_MOVE:
        x, y, duration = token[1]
        print(f"{name}:  {time_str}   move:", x, y, duration)
        # move_cursor((
        #         choose_random_int(x[0], x[1]),
        #         choose_random_int(y[0], y[1])
        #     ),
        #     duration
        # )
    elif token_type == TT_CLICK:
        button = token[1]
        print(f"{name}:  {time_str}  click:", button)
    elif token_type == TT_TYPE:
        str = token[1]
        print(f"{name}:  {time_str}   type:", str)
    elif token_type == TT_DEL:
        count = token[1]
        print(f"{name}:  {time_str}    del:", count)
    elif token_type == TT_RTEXT:
        count = token[1]
        print(f"{name}:  {time_str}   rtxt:", count)
    elif token_type == TT_RSTR:
        count = token[1]
        print(f"{name}:  {time_str}   rstr:", count)
