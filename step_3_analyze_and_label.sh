#!/bin/bash
#SBATCH --job-name=dlc_analyze_videos
#SBATCH --account=def-ljt   # adjust this to match the accounting group you are using to submit jobs
#SBATCH --gres=gpu:1        # request GPU "generic resource"
#SBATCH --mem=16000M        # memory per node
#SBATCH --time=0-00:30      # time (DD-HH:MM)
#SBATCH --mail-user=dotovd@mcmaster.ca # adjust this to match your email address
#SBATCH --mail-type=ALL
#SBATCH --output=%N-%j.out  # %N for node name, %j for jobID

module load cuda cudnn 
source ~/DLC/bin/activate
cd ~/stepclap-CC-2021-09-20/
python ~/c6/step_3_analyze_and_label.py
