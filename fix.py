# http://code.activestate.com/recipes/384122-infix-operators/
class prefix:
    def __init__(self, function):
        self.function = function
    def __ror__(self, other):
        return infix(
            lambda x, self=self, other=other: self.function(other, x)
        )
    def __or__(self, other):
        return self.function(other)

class infix:
    def __init__(self, function):
        self.function = function
    def __ror__(self, other):
        return infix(
            lambda x, self=self, other=other: self.function(other, x)
        )
    def __or__(self, other):
        return self.function(other)