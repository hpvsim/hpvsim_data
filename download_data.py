#/usr/bin/env python
'''
Download the data
'''

import sciris as sc
import hpvsim as hpv

# Set folder
thisdir = sc.thispath()
filesdir = thisdir / 'files'
hpv.data.downloaders.set_filesdir(filesdir)

# Check that things match
md = sc.loadjson(thisdir / 'metadata.json')
mdver = md['version']
hpvver = hpv.data.downloaders.data_version
assert mdver == hpvver, f'Versions do not match! Metadata = {mdver}, HPVsim = {hpvver}'

# Download new data
hpv.data.get_data()

print('Done; run make_zip next')