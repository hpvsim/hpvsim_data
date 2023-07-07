#!/usr/bin/env python
# Regenerate the data file for quick download:
# 1. Remove the existing file
# 2. Add new files recursively but without keeping folder structure

import sciris as sc

ans = input('Did you remember to increment the version? y/[n] ')
if ans != 'y':
    raise ValueError('\nNo? OK, thanks for your honesty. Exiting.')

# Make it easier to run bash commands
def run(command, printinput=True, printoutput=True):
    import subprocess as sp
    if printinput: print(command)
    std = sp.Popen(f'{command}', shell=True, stdout=sp.PIPE, stderr=sp.PIPE)
    stdout, stderr = std.communicate()
    output = stdout.decode()
    try:
        output += stderr.decode()
    except:
        pass
    if printoutput: print(output)
    return output

mdfile = 'metadata.json'
metadata = sc.loadjson(mdfile)
version = metadata['version']

data_file = f'hpvsim_data_v{version}.zip'
run(f'zip {data_file} -R -j {mdfile} files/*') # TODO: update to sc.savezip(), hard because of flags

string = f'''
Please next run:
    git add {data_file}
    git commit -m 'updated data'
    git push

Then remember to update data_version in HPVsim to use the new version: ({version}).
'''
print(string)