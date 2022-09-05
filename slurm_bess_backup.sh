#!/bin/bash
#SBATCH --nodes=1
#SBATCH --mem=32000
#SBATCH --time=128:00:00
#SBATCH --output=bess-backup-%j.out
#load the modules
module load Anaconda3/5.3.0



# run the script
srun --export=ALL python3 bess_backup.py
