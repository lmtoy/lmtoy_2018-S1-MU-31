#! /usr/bin/env python
#

import os
import sys

from lmtoy import runs

project="2018-S1-MU-31"

#        obsnums per source (make it negative if not added to the final combination)
on = {}

on["B59"] =  [ 92634, 92825,]

# on["OH2"] = [ 92829, 92827, 92823, 92821, 92636, 92632, 92630]


#        common parameters per source on the first dryrun (run1a, run2a)
pars1 = {}

pars1["B59"] = "vlsr=185 dv=40 dw=80"
# pars1["OH2"] = ""

#        common parameters per source on subsequent runs (run1b, run2b)
pars2 = {}

pars2["B59"] = "pix_list=-0,1,4,5,12,13"
#pars2["OH2"] = ""


if __name__ == '__main__':    
    runs.mk_runs(project, on, pars1, pars2, sys.argv)
