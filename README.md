# c6

Workflow to extract 2D marker motion from video recordings using DeepLabCut. I broke down the process into three stages. Step 1 is easy to do on your desktop/laptop. Here it is assumed that you'll transfer the whole project folder to the cluster computing node.

STEP 1
Project setup and manual labeling. This should be easy to run on any desktop/laptop computer. Take the command line shell to the folder where you have the source videos and then run: 
>jupyter notebook path to where you placed the scripts/step_1_start_project_and_manually_label_frames.ipynb

Once you're done, copy the project to your cluster by entering this command in the shell of YOUR computer (not the cluster), replacing dobri2 with your own user name:
>scp -r my_project_folder dobri2@graham.computecanada.ca:~/

STEP 2
Train the neural net. This is the most time-consuming part. It should take a day at least on a computecanada node or multiple days on your own computer. (I haven't evaluated its performance wrt training time and different machines thoroughly. It was at least 10x faster on Graham relative to my laptop.) In graham.computecanada.ca, send the training as a job with:
>sbatch step_2_train.sh

Important parameters inside. You need to edit this script to hard-code the project folder path by changing the address in 'cd ~/stepclap-2021-09-20/'. To control the duration of the training, you either set the corresponding SBATCH tag in the .sh file, or you leave this for very long (days if you want), and set the 'maxiters' argument in the .py script. In the example that I worked with, two short videos with similar motion inside, I found that after 200k or 300k iterations the loss started to plateau. This needs to be explored though. How much improvement will you get when working with complex datasets with variable backgrounds if you let the training do the default 1M iterations?

STEP 3
Analyze and automatically label the full videos:
>sbatch step_3_analyze_and_label.sh

This is not super time-consuming but it seems to require a good amount of memory. Similar to the previous, pay attention to the details inside the script, such as the project folder '~/stepclap-2021-09-20/'

You can monitor both steps 2 and 3 to some extent by checking how long they've been running with:
>squeue --user dobri2

and their periodicially updated output, if any. If the script inside the job is producing any output (what you would normally see during execution in the shell), it will be dumped in a text file that starts with gra (for Graham) and ends with .out. You can quickly check its content with:
>cat gra....out

Once step 3 is complete, you should have the intersting files in the 'videos' folder. Copy it to your computer with something like the following, issued from the shell of your computer (not the cluster). Important! The slash matters. With the slash, scp copies INSIDE the given folder. Without the slash, scp REPLACES the given folder.
>scp -r dobri2@graham.computecanada.ca:~/stepclap-CC-2021-09-20/videos my_project_folder/

That's it, this stage of the journey is complete. The outcome of this looks something like the figures and data files in the 'sample videos' folder. Also check the videos with added markers in https://mcmasteru365-my.sharepoint.com/:f:/g/personal/dotovd_mcmaster_ca/Eh4XyfwWXUxEq2_nF9Y7dxIB0_9anhG4n0PS01VOtZl-Og?e=a6PDgv.

Now you need to pull the timeseries data from the data files and analyze them as you would analyze mocap recordings.

===

Some notes on installation, usage, and hardware.

There's a big increase in difficulty from installing for CPU to installing for GPU usage. The latter requires a lot of prerequisites and the computer system to be all aligned and mutually consistent and this turns out to be a huge pain. I found it hardest to install for GUI on my Ubuntu laptop, then my Windows laptop, and the easiest was on Graham which is also linux-based but didn't create as many issues. Note that it's practically pointless to run the training on CPU only; each participant will take days. You need to find a system that has a decent NVIDIA GPU and that you can play with in order to have the toolbox communicate with the GPU. 

If you'll be using Compute Canada's resources, browse the wiki for advices and best practices, it's not too much to read. https://docs.computecanada.ca/wiki. For example, where to store your raw data and scripts, https://docs.computecanada.ca/wiki/Storage_and_file_management? I tried using the 'projects' space but I got weird errors there so I moved the working project to the home folder at ~/.

Another, smallish, difficulty was to have GUI working on Ubuntu. There's an apparent incompatibility in some of the prerequisites but there's a workaround it. The GUI is needed for labeling the frames. If you don't plan to do labeling on a linux-based computer, then ignore this.

If you just need to install the deeplabcut module in your python environment then you don't need to clone the rep. If you want to practice by running the examples, start by cloning the repository, git clone https://github.com/DeepLabCut/DeepLabCut.git, and then look inside their 'examples' folder.

To get this set of scripts on your machine, it's easy to download the zip file or clone this repo over ssh:
>git clone git@github.com:TrainorLab/c6

To do that, you will need to authenticate with an ssh key, or use a client. For the ssh, check https://docs.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent

