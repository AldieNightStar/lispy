# Simple lisp parser for python

# Usage
```py
from lispy import parse

# Parse text source of the lisp file
# Returns list of commands where each sublist is a command as well
#    [command arg1 arg2 arg3 [subcommand arg1 arg2 ...]]
arr = parse(src)
```