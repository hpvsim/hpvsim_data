'''
Find where data versions have changed
'''

import sciris as sc

T = sc.timer()

# Define the versions here
keep_match = True
v1 = '1.1'
v2 = '1.2'

# Load the two files
datadir = sc.thispath() / '..'
f1 = datadir / f'hpvsim_data_v{v1}.zip'
f2 = datadir / f'hpvsim_data_v{v2}.zip'

d1 = sc.loadzip(f1)
d2 = sc.loadzip(f2)

# Make comparison
comps = sc.autolist()
fkeys = sorted(list(set(d1.keys()) | set(d2.keys())))
for fkey in fkeys:
    if fkey != 'metadata.json':
        print(f'Working on {fkey}...')
        ckeys = sorted(list(set(d1[fkey].keys()) | set(d2[fkey].keys())))
        for ckey in ckeys:
            print(f'  Working on {ckey}...')
            try:
                df1 = d1[fkey][ckey]
                df2 = d2[fkey][ckey]
            except:
                comps += dict(file=fkey, country=ckey, column=None, match=None, v1=None, v2=None)
            if not hasattr(df1, 'columns'):
                match = (df1 == df2).all()
                if match:
                    v1,v2 = None, None
                else:
                    v1 = df1.sum()
                    v2 = df2.sum()
                if keep_match or not match:
                    comps +=  dict(file=fkey, country=ckey, column=None, match=match, v1=v1, v2=v2)
            else:
                for col in df1.columns:
                    c1 = df1[col]
                    c2 = df2[col]
                    match = (c1 == c1).values.all()
                    if match:
                        v1,v2 = None, None
                    else:
                        v1 = c1.sum()
                        v2 = c2.sum()
                    if keep_match or not match:
                        comps += dict(file=fkey, country=ckey, column=col, match=match, v1=v1, v2=v2)

df = sc.dataframe(comps)
df.to_excel(f'comparison_v{v1}_v{v2}.xlsx')

T.toc('Done')