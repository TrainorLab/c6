# c6

Workflow to extract marker motion in 2D from video recordings using DeepLabCut.

First, some notes on installation, usage, and hardware.

There's a big increase in difficulty from installing for CPU to installing for GPU usage. The latter requires a lot of prerequisites and the computer system to be all aligned and mutually consistent and this turns out to be a huge pain. I found it hardest to install for GUI on my Ubuntu laptop, then my Windows laptop, and the easiest was on Graham which is also linux-based but didn't create as many issues. Note that it's practically pointless to run the training on CPU only; each participant will take days. You need to find a system that has a decent NVIDIA GPU and that you can play with in order to have the toolbox communicate with the GPU. 

If you'll be using Compute Canada's resources, browse its wiki, for advices and best practices, it's not that much. https://docs.computecanada.ca/wiki. For example, where to store your raw data and scripts, https://docs.computecanada.ca/wiki/Storage_and_file_management.

Another, smallish, difficulty was to have GUI working on Ubuntu. There's an apparent incompatibility in some of the prerequisites but there's a workaround it. The GUI is needed for labeling the frames. If you don't plan to do labeling on a linux-based computer, then ignore this.

If you just need to install the deeplabcut module in your python environment then you don't need to clone the rep. If you want to practice by running the examples, start by cloning the repository, git clone https://github.com/DeepLabCut/DeepLabCut.git, and then look inside their 'examples' folder.

The actual workflow. I've broken down the process into three stages. Step 1 is easy to do on your desktop/laptop. Then you'll need to transfer the whole project folder to the cluster computing node.

STEP 1
Project setup and manual labeling. This should be easy to run on any desktop/laptop computer. Take the command line shell to the folder where you have the source videos and then run: 
> jupyter notebook <path to where you placed the scripts>/step_1_start_project_and_manually_label_frames.ipynb

Once you're done, copy the project to your cluster:
> scp -r project_folder dobri2@graham.computecanada.ca:~/project/def-ljt/dobri2/

STEP 2
Train the neural net. This is the most time-consuming part. It should take a day at least on a computecanada node or multiple days on your own computer. (I haven't evaluated its performance wrt training time and different machines thoroughly. It was at least 10x faster on Graham relative to my laptop.) In graham.computecanada.ca, send the training as a job with:
> sbatch step_2_train.sh
Important parameters inside, such as how long to run the training. You need to edit this script to hard-code the project folder path by changing the address in:
cd ~/project/def-ljt/dobri2/dodo_sample2/stepclap-2021-09-20/

STEP 3
Analyze and automatically label the full videos:
> sbatch step_3_analyze_and_label.sh
This is not super time-consuming but it seems to require a good amount of memory. Similar to the previous, pay attention to the details inside the script, such as the project folder:
cd ~/project/def-ljt/dobri2/dodo_sample2/stepclap-2021-09-20/
