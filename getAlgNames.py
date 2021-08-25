#/usr/bin/env python

from mantid.api import AlgorithmFactory, AlgorithmManager

algs = AlgorithmFactory.getRegisteredAlgorithms(True)

algnames = []
algsummary = []

for algname, version in algs.items():
    alg = AlgorithmManager.create(algname, version)
    #
    algnames.append(algname)
    algsummary.append(alg.summary())

with open("alglist.csv", "w") as f:
    txtstr = "CurrentName\tSummary\n"
    for n, s in zip(algnames, algsummary):
        txtstr += f"{n}\t{s}\n"
    f.write(txtstr)
