import re
from random import randint, uniform

TT_MOVE     = 'TT_MOVE'
TT_CLICK    = 'TT_CLICK'
TT_TYPE     = 'TT_TYPE'
TT_LOOP     = 'TT_LOOP'
TT_LOOP_END = 'TT_LOOP_END'
TT_RTEXT    = 'TT_RTEXT'
TT_RSTR     = 'TT_RSTR'

def choose_random_int(a: int, b: int) -> int:
    return randint(a, b)

def choose_random_float(a: float, b: float) -> float:
    return uniform(a, b)

click_regex = re.compile(
    r"click\s+(left|right|double)",
    re.IGNORECASE)
loop_regex = re.compile(
	r"""
		loop\s+
		\(
		(?P<min>\d+),\s+
		(?P<max>\d+)\)
	""", re.VERBOSE)
rtext_regex = re.compile(
    r"""rtext\s+\(
        (?P<min>\d+),\s+
        (?P<max>\d+)\)
    """,
    re.IGNORECASE | re.VERBOSE)
rstr_regex = re.compile(
    r"""rstr\s+\(
        (?P<min>\d+),\s+
        (?P<max>\d+)\)
    """,
    re.IGNORECASE | re.VERBOSE)
end_regex = re.compile(
    r"end",
    re.IGNORECASE)
move_regex = re.compile(
    r"""
        move\s+
        \(
        (?P<min_x>\d+),\s+
        (?P<min_y>\d+)\)\s+
        \(
        (?P<max_x>\d+),\s+
        (?P<max_y>\d+)\)\s+
        (?P<duration>[\d.]+),\s+
        (?P<wait>[\d.]+)
    """, re.VERBOSE)
type_regex = re.compile(
	r"""
		type\s+
		"
		(?P<str>.*?)
		"
	""",re.VERBOSE | re.DOTALL | re.MULTILINE)

def lex(code):
    tokens = []
    commands = code.split(";")
    cmd_number = 1
    for cmd in commands[:-1]:
        cmd = cmd.strip()
        loop_match = loop_regex.search(cmd)
        end_match = end_regex.search(cmd)
        move_match = move_regex.search(cmd)
        click_match = click_regex.search(cmd)
        type_match = type_regex.search(cmd)
        rtext_match = rtext_regex.search(cmd)
        rstr_match = rstr_regex.search(cmd)

        if loop_match:
            min_count = int(loop_match.group("min"))
            max_count = int(loop_match.group("max"))
            tokens.append((TT_LOOP, (min_count, max_count)))
        elif end_match:
            tokens.append((TT_LOOP_END, None))
        elif move_match:
            min_x = int(move_match.group("min_x"))
            min_y = int(move_match.group("min_y"))
            max_x = int(move_match.group("max_x"))
            max_y = int(move_match.group("max_y"))
            duration = float(move_match.group("duration"))
            wait = float(move_match.group("wait"))
            tokens.append(
                (TT_MOVE, (
                    (min_x, min_y),
                    (max_x, max_y),
                    duration, 
                    wait)))
        elif click_match:
            button = click_match.group(1)
            tokens.append((TT_CLICK, button))
        elif type_match:
            str = type_match.group("str")
            tokens.append((TT_TYPE, str))
        elif rtext_match:
            min_count = int(rtext_match.group("min"))
            max_count = int(rtext_match.group("max"))
            tokens.append((TT_RTEXT, (min_count, max_count)))
        elif rstr_match:
            min_count = int(rstr_match.group("min"))
            max_count = int(rstr_match.group("max"))
            tokens.append((TT_RSTR, (min_count, max_count)))
        else:
            print(f"loop_script: lex error on command {cmd_number}: '{cmd}'")
        cmd_number += 1
    return tokens

class ASTNode:
    def __init__(self):
        self.children = []

    def __repr__(self):
        return f"node {self.children}"

class LoopNode(ASTNode):
    def __init__(self, count):
        super().__init__()
        self.count = count

    def __repr__(self):
        return f"loop {self.count}"

class EndNode(ASTNode):
    def __init__(self):
        super().__init__()

    def __repr__(self):
        return f"end"

class MoveNode(ASTNode):
    def __init__(self, x, y, duration, wait):
        super().__init__()
        self.x = x
        self.y = y
        self.duration = duration
        self.wait = wait

    def __repr__(self):
        return f"move {self.x}, {self.y}, {self.duration}, {self.wait}"

class ClickNode(ASTNode):
    def __init__(self, button):
        super().__init__()
        self.button = button

    def __repr__(self):
        return f"click ({self.button})"

class TypeNode(ASTNode):
    def __init__(self, str):
        super().__init__()
        self.str = str

    def __repr__(self):
        return f"type '{self.str}'"

class RTextNode(ASTNode):
    def __init__(self, arg):
        super().__init__()
        self.arg = arg

    def __repr__(self):
        return f"rtext {self.arg}"

class RStrNode(ASTNode):
    def __init__(self, arg):
        super().__init__()
        self.arg = arg

    def __repr__(self):
        return f"rstr {self.arg}"

class RTextNode(ASTNode):
    def __init__(self, arg):
        super().__init__()
        self.arg = arg

    def __repr__(self):
        return f"rtext {self.arg}"

class RStrNode(ASTNode):
    def __init__(self, arg):
        super().__init__()
        self.arg = arg

    def __repr__(self):
        return f"rstr {self.arg}"

def parse(tokens):
    stack = []
    root = None
    for token in tokens:
        token_type, value = token
        if token_type == TT_LOOP:
            node = LoopNode(value)
            if root is None:
                root = node
            if stack:
                stack[-1].children.append(node)
            stack.append(node)
        elif token_type == TT_LOOP_END:
            node = EndNode()
            if stack:
                stack[-1].children.append(node)
            stack.pop()
        elif token_type == TT_MOVE:
            node = MoveNode(*value)
            if stack:
                stack[-1].children.append(node)
            else:
                root = node
        elif token_type == TT_CLICK:
            node = ClickNode(value)
            if stack:
                stack[-1].children.append(node)
            else:
                root = node
        elif token_type == TT_TYPE:
            node = TypeNode(value)
            if stack:
                stack[-1].children.append(node)
            else:
                root = node
        elif token_type == TT_RTEXT:
            rtext_node = RTextNode(value)
            stack[-1].children.append(rtext_node)
        elif token_type == TT_RSTR:
            rstr_node = RStrNode(value)
            stack[-1].children.append(rstr_node)
        else:
            print(f"loop_script: Failed to parse token {token}")
            return None
    return root

def traverse(node, indent=0):
    print("    " * indent + "└── " + str(node))
    for child in node.children:
        traverse(child, indent=indent+1)

def execute(node):
    for child in node.children:
        if isinstance(child, LoopNode):
            print("LOOP")
            for i in range(child.count):
                execute(child)
        elif isinstance(child, EndNode):
            return
        elif isinstance(child, MoveNode):
            print("MOVE")
            # move_mouse(
            #     child.min_x,
            #     child.min_y,
            #     child.max_x,
            #     child.max_y,
            #     child.duration, child.wait)
        elif isinstance(child, ClickNode):
            print("CLICK")
            # click_mouse(child.button)
        elif isinstance(child, TypeNode):
            print("TYPE")
            # type_string(child.str)
        elif isinstance(child, RTextNode):
            print("RTEXT")
            # rtext(child.arg)
        elif isinstance(child, RStrNode):
            print("RSTR")
            # rstr(child.arg)
        else:
            print(f"loop_script: Unknown node type: {child}")