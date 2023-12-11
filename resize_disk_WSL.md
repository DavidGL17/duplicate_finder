# Resize disk WSL

Sources :

-   https://superuser.com/questions/1606213/how-do-i-get-back-unused-disk-space-from-ubuntu-on-wsl2

## New technique

In cmd or powershell, shutdown the wsl with `wsl --shutdown`, then list with `wsl -l -v` and ensure the state is stopped. Then run `wsl --manage <distro> --set-sparse true` by replacing the `<distro>` with the name under the Name column.

## Old technique

To run this one you cannot have run the new technique before. If you did, run `wsl --manage <distro> --set-sparse false` to revert the changes (with the wsl shutdown).

Same as before, shutdown and list

```powershell
wsl --shutdown
wsl -l -v
```

Then go to `C:/Users/<user>/AppData/Local/Packages/CanonicalGroupLimited.Ubuntu22.04LTS_79rhkp1fndgsc\LocalState`, there should be a file named `ext4.vhdx`. Now in the powershell, run `diskpart`, which will open a new terminal. In that new window, run

```powershell
select vdisk file="C:\WSL-Distros\…\ext4.vhdx" # replace with the path to the vhdx file
attach vdisk readonly
compact vdisk # takes a long time
detach vdisk
exit
```
