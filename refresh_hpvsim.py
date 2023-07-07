#/usr/bin/env python
'''
Remove and redownload the data
'''

import sciris as sc
import hpvsim as hpv
T = sc.timer()

print('Removing data...')
hpv.data.remove_data()

print('Redownloading data...')
hpv.data.quick_download(init=True)

T.toc('Done')