class Mat:
    def __init__(*vecs):
        """
        Takes one or more input vectors as arguments and initializes the `self.rows`
        attribute with the provided values.

        """
        self.rows = vecs

    def __add__(self): ...
