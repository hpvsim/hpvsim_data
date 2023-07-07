#/usr/bin/env python
'''
Download the data
'''

import sciris as sc
import hpvsim.data.downloaders as hdd

# Set folder
thisdir = sc.thispath()
filesdir = thisdir / 'files'
hdd.set_filesdir(filesdir)

# Check that things match
md = sc.loadjson(thisdir / 'metadata.json')
mdver = md['version']
hpvver = hdd.data_version
assert sc.compareversions(mdver, hpvver) == 1, f'Metadata version {mdver} should be greater than HPVsim version {hpvver}'

# Download new data
hdd.get_data()

print('Done; run make_zip.py next')