#!/usr/bin/env python
import pandas as pd
import statsmodels
import sys
import statsmodels.formula.api as smf

fname = sys.argv[1]
cols  = "date      AAPL      MSFT       XOM       Mkt     SMB     HML       Rf".split()
syms  = ['AAPL','MSFT','XOM']
data  = pd.read_excel(fname, sheetname='Data')[cols].dropna(how='any')
for col in syms+['Mkt']:
    data[col+('_Rf' if col=='Mkt' else '_excess')] = data[col] - data['Rf']

#1 factor
for sym in syms:
    mod_1f = smf.ols(formula=sym+'_excess ~ Mkt_Rf', data=data)
    res_1f = mod_1f.fit()
    print(res_1f.summary(title="1-Factor OLS Regression Results for {}".format(sym)))
    print("")
    print("")


#3factor
for sym in syms:
    mod_3f = smf.ols(formula=sym+'_excess ~ Mkt_Rf + SMB + HML', data=data)
    res_3f = mod_3f.fit()
    print(res_3f.summary(title="3-Factor OLS Regression Results for {}".format(sym)))
    print("")
    print("")
