class TyrepunctureException(Exception):
        def __init__(self,arg):
            self.msg = arg
str="puncture"
if str=="puncture":
    raise TyrepunctureException("sorry you cannot move")
