import re

TT_MOVE     = 'TT_MOVE'
TT_CLICK    = 'TT_CLICK'
TT_TYPE     = 'TT_TYPE'
TT_LOOP     = 'TT_LOOP'
TT_LOOP_END = 'TT_LOOP_END'

loop_regex = re.compile(
	r"""
		loop\s+
		(?P<count>\d+)
	""", re.VERBOSE)

end_regex = re.compile(r"end", re.IGNORECASE)
move_regex = re.compile(
	r"""
		move\s+
		\(
		(?P<min_x>\d+),\s+
		(?P<min_y>\d+)\)\s+
		\(
		(?P<max_x>\d+),\s+
		(?P<max_y>\d+)\)\s+
		\(
		(?P<duration>[\d.]+),\s+
		(?P<wait>[\d.]+)\)
	""", re.VERBOSE)

click_regex = re.compile(r"click\s+(left|right|double)", re.IGNORECASE)
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
        if loop_match:
            tokens.append((TT_LOOP, int(loop_match.group("count"))))
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
                    min_x,
                    min_y,
                    max_x,
                    max_y,
                    duration,
                    wait)))
        elif click_match:
            button = click_match.group(1)
            tokens.append((TT_CLICK, button))
        elif type_match:
            str = type_match.group("str")
            tokens.append((TT_TYPE, str))
        else:
            print(f"Error on command {cmd_number}: '{cmd}'")
            return None
        cmd_number += 1
    return tokens

class ASTNode:
    def __init__(self):
        self.children = []

    def __repr__(self):
        return f"node ({self.children})"

class LoopNode(ASTNode):
    def __init__(self, count):
        super().__init__()
        self.count = count

    def __repr__(self):
        return f"loop ({self.count})"

class EndNode(ASTNode):
    def __init__(self):
        super().__init__()

    def __repr__(self):
        return f"end"

class MoveNode(ASTNode):
    def __init__(self, min_x, min_y, max_x, max_y, duration, wait):
        super().__init__()
        self.min_x = min_x
        self.min_y = min_y
        self.max_x = max_x
        self.max_y = max_y
        self.duration = duration
        self.wait = wait

    def __repr__(self):
        return f"move ({self.min_x}, {self.min_y}, {self.max_x}, {self.max_y}, {self.duration}, {self.wait})"

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
        return f"type ('{self.str}')"

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
        else:
            return None
    return root