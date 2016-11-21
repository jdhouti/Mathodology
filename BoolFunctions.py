# Julien Dhouti
# Started: November 02, 2016

def is_true(b):
    """Returns True if given bool is True, returns False if otherwise."""
    if b:
        return True

    else:
        return False

def bool_not(b):
    """Returns True if given bool is False, returns False if otherwise."""
    """This function is identical to the not function."""
    if b:
        return False

    else:
        return True

def bool_true(b):
    """Returns True regardless of given bool."""
    return True

def bool_false(b):
    """Returns False regardless of given bool."""
    return False

def bool_and(b1, b2):
    """Returns True if both given bools are True, returns False if otherwise."""
    if b1 == True and b2 == True:
        return True

    else:
        return False

def bool_nand(b1, b2):
    """Returns the opposite of bool_and."""
    return bool_not(bool_and(b1, b2))

def bool_or(b1, b2):
    """ Returns the True if either of the given bools are True, retuns false if otherwise."""
    if b1 == False and b2 == False:     # skips to the chase
        return False

    else:
        return True

def bool_xor(b1, b2):
    """If booleans are identical, returns False. Returns True if otherwise."""
    if b1 == b2:
        return False

    else:
        return True

# this function is the same as:
#         not bool_xor(b1, b2)
def bool_equiv(b1, b2):
    """If booleans are identical, returns True, returns False if otherwise."""
    if b1 == b2:
        return True

    else:
        return False
