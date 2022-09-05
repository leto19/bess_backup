#Bess Backup

Have YOU ever experienced data loss due to HPC (SHARC/Bessemer) automatic deletion policy?
For those not in the know, every now and again files older than 60 days are deleted forever (!!!) from 
your fastdata directory (usally `/fastdata/[username]`). You can generate a list of files which are set to be deleted with this command:
```
lfs find -ctime +60 /fastdata/[username]
```
Up until now there wasn't an easy way to backup these files in an automatic way...

This is why I've written a python script  `bess_backup.py` which will automatically find those files and folders which are due to be deleted and copy them to a backup folder within your `/fastdata/` folder. 

To run it simply start an interactive session, place the script file anywhere in your home directory and run
```
python3 bess_backup.py
```
I've also provided a [SLURM](https://docs.hpc.shef.ac.uk/en/latest/hpc/scheduler/index.html#job-submission-control-on-bessemer) script which will queue a job to run to start `bess_backup.py`.

To run this simply place `slurm_bess_backup.sh` in the same folder as `bess_backup.py` and run:
```
sbatch slurm_bess_backup.sh
```
(Note that this will only work for Bessemer as SHARC uses a different workload manager) 

Let me know if you try it out (and if you have any problems).
