# HPVsim data

Separate repository for storing HPVsim data from public sources. Only used by HPVsim; not to be used directly.

The files included are https://population.un.org/wpp/Download/Files/1_Indicators%20(Standard)/CSV_FILES/WPP2022 from the UN, and `wbgapi.data.DataFrame('SP.DYN.CBRT.IN')` from the World Bank.

This repo uses GitLFS to avoid the issues with storing large data files on GitHub.

To update the data:

1. Update the metadata in `metadata.json` -- **you must increment the version number**.
2. **Update the version number in `hpvsim/data/downloaders.py` to match.**
3. If needed, delete existing files in the `files` folder.
4. Run `download_data.py`.
5. Run `make_zip.py`.
6. Commit the new zip file and push.
7. The new data will now be automatically used for all new HPVsim installs.
8. Run `refresh_hpvsim.py`. This will run `hpv.data.remove_data()`, and then redownload the data.
9. Release the new version of HPVsim with the new data version.