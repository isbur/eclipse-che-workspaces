from functools import partial
# http://code.activestate.com/recipes/384122-infix-operators/
class prefix:

    def __init__(self, function):
        self.operator_function = function

    def __or__(self, righthand_operand):
        return self.operator_function(righthand_operand)


class infix:

    def __init__(self, operator_function):
        self.operator_function = operator_function

    def __rtruediv__(self, lefthand_operand):
        return infix(
            partial(
                self.operator_function_thin_wrapper, lefthand_operand=lefthand_operand
            )
        )

    def __truediv__(self, righthand_operand):
        return self.operator_function(
            righthand_operand=righthand_operand
        )

    def operator_function_thin_wrapper( 
        self, 
        lefthand_operand, 
        righthand_operand
    ):
        return self.operator_function(
            lefthand_operand, 
            righthand_operand
        )