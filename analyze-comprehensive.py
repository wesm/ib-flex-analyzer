import glob
import os

from ibflex.statement import FlexStatement, rollup_statements

paths = glob.glob(os.path.expanduser('~/Dropbox/ib_flex_reports/*.xml'))

statements = [FlexStatement(path) for path in paths]

mtm = rollup_statements(statements)
realized = rollup_statements(statements, 'realized')


fees = statements[0].fees
for _s in statements[1:]:
    fees = fees.add(_s.fees, fill_value=0)

totals = mtm.sum(0).add(fees, fill_value=0)
totals.Total += fees.sum()
