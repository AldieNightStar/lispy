def lex(src):
    arr = []
    sb = []
    def _submit():
        if len(sb) > 0:
            arr.append("".join(sb))
            sb.clear()
    esc = False
    commentMode = False
    for c in src:
        if commentMode:
            if c == "\n": commentMode=False; continue
            continue
        if esc:
            esc = False
            print("Escaped", c)
            sb.append(c)
            continue
        if c in " \t\n\r":
            _submit()
            continue
        if c == "\\":
            esc = True
            continue
        if c in "()[]{}<>":
            _submit()
            arr.append(c)
            continue
        if c == "#":
            commentMode = True
            continue
        sb.append(c)
    _submit()
    return arr

def _try_parse_cmd(tok, it):
    if tok != "(": return
    arr = []
    for subtok in it:
        if subtok == ")": break
        # Try parse inner cmd's
        cmd = _try_parse_cmd(subtok, it)
        if cmd: arr.append(cmd); continue
        # Add everything in
        arr.append(subtok)
    return arr

def parse(toks):
    def _parse(it):
        arr = []
        for tok in it:
            # Try parse found cmds
            cmd = _try_parse_cmd(tok, it)
            if cmd: arr.append(cmd); continue
        return arr
    return _parse(iter(toks))
