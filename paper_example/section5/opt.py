
import sys
from clingo.symbol import Number, SymbolType
from clingo.application import Application, clingo_main


class OptExampleApp(Application):

    program_name = 'opt-example'
    version = '1.0'

    def __init__(self):
        self._bound = None

    def _on_model(self, model):
        self._bound = 0
        for atom in model.symbols(atoms=True):
            if atom.match('_minimize', 2) and atom.arguments[0].type \
                is SymbolType.Number:
                self._bound += atom.arguments[0].number

    def main(self, ctl, files):
        if not files:
            files = ['-']
        for f in files:
            ctl.load(f)
        ctl.add('bound', ['b'],
                ':- #sum{V,I : _minimize (V,I)} >= b.')
        ctl.ground([('base', [])])

        while ctl.solve(on_model=self._on_model).satisfiable:
            print('Found new bound : {} '.format(self._bound))
            ctl.ground([('bound', [Number(self._bound)])])

        if self._bound is not None:
            print('Optimum found')

clingo_main(OptExampleApp(), sys.argv[1:])    
