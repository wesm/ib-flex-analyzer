import glob
import os

from ibflex.statement import FlexStatement, rollup_statements

paths = glob.glob(os.path.expanduser('~/Dropbox/ib_flex_reports/*.xml'))

statements = [FlexStatement(path) for path in paths]

mtm = rollup_statements(statements)
realized = rollup_statements(statements, 'realized')
