
from clingo.symbol import Number
from clingo.control import Control

class ExampleApp:
    @staticmethod
    def divisors(a):
        a = a.number
        for i in range(1, a+1):
            if a % i == 0:
                yield Number ( i )
    def run ( self ):
        ctl = Control ()
        ctl . load ( "example.lp" )
        ctl . ground ([( "base" , [])] , context = self )
        ctl . solve (on_model = print)
if __name__ == "__main__" :
    ExampleApp (). run ()
