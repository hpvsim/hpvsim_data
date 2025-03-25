#!/usr/bin/env python
'''
Download the data
'''

import sciris as sc
import hpvsim.data.downloaders as hdd

# Options
force  = True
tidy   = True
serial = False

# Set folder
thisdir = sc.thispath()
filesdir = thisdir / 'files'
hdd.set_filesdir(filesdir)

# Check that things match
md = sc.loadjson(thisdir / 'metadata.json')
mdver = md['version']
hpvver = hdd.data_version
if sc.compareversions(mdver, hpvver) != 0:
    errormsg = f'The typical workflow is to update the HPVsim data version {hpvver} first, then update the metadata version {mdver}. Please update to match, then rerun.'
    raise ValueError(errormsg)
else:
    hdd.download_data(force=force, tidy=tidy, serial=serial) # Download new data
    print('Done; run make_zip.py next')