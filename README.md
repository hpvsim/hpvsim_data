# HPVsim data

Separate repository for storing HPVsim data from public sources. Only used by HPVsim; not to be used directly.

The files included are https://population.un.org/wpp/Download/Files/1_Indicators%20(Standard)/CSV_FILES/WPP2022 from the UN, and `wbgapi.data.DataFrame('SP.DYN.CBRT.IN')` from the World Bank.

This repo uses GitLFS to avoid the issues with storing large data files on GitHub.

To update the data:

1. Run `get_data.py` in HPVsim's `data` folder (NB: this script might be moved into this repo in future).
2. Move the `.obj` files into the `files` subfolder here.
3. Run `make_zip`
4. Commit the updated zip file and push.
5. The new data will now be automatically used for all new HPVsim installs.
6. To refresh an existing HPVsim installation, the easiest approach is to run `hpv.data.remove_data()`. It will then automatically re-download the next time HPVsim is imported.