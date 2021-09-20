import deeplabcut
import os
# from pathlib import Path # ?

# DON'T forget to take the command line to the right location, the project folder.

# Useful to keep a path to the project folder.
# You can hard-code this if necessary.
path_config_folder = os.getcwd()
print(path_config_folder)
path_config_file = os.path.join(path_config_folder,'config.yaml')

videofile_path = [
    os.path.join(path_config_folder,'videos','VID_20210917_133448.mp4'),
    os.path.join(path_config_folder,'videos','VID_20210917_133508.mp4')]
print(videofile_path)

deeplabcut.analyze_videos(path_config_file,videofile_path)
deeplabcut.create_labeled_video(path_config_file,videofile_path)
deeplabcut.plot_trajectories(path_config_file,videofile_path)
