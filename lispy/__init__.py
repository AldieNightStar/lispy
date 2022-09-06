from lispy.lexparse import lex as _lex, parse as _parse

def parse(src):
    return _parse(_lex(src))