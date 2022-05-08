
import sys
from clingo.symbol import Number
from clingo.application import Application, clingo_main


class ExampleApp(Application):
    program_name = "example"
    version = "1.0"
    
    @staticmethod
    def divisors(a):
        a = a.number
        for i in range(1, a+1):
            if a % i == 0:
                yield Number ( i )
    
    def main(self, ctl, files):
        for path in files: 
            ctl.load(path)
        if not files:
            ctl.load ( " -" )
        ctl.ground([( "base" , [])] , context = self )
        ctl.solve()

if __name__ == "__main__" :
    clingo_main (ExampleApp(),sys.argv[1:])
