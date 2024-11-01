
class Vec:
    """
    Allows multiple values to be stored as a single object, with the `vs` parameter
    accepting a variable number of arguments.

    """
    def __init__(*vs):
        self.vs = vs
