import deeplabcut
import os
# from pathlib import Path # ?

# DON'T forget to take the command line to the right location, the project folder.

# Useful to keep a path to the project folder.
# You can hard-code this if necessary.
path_config_folder = os.getcwd()
print(path_config_folder)
path_config_file = os.path.join(path_config_folder,'config.yaml')

deeplabcut.create_training_dataset(path_config_file,windows2linux=True)
deeplabcut.train_network(path_config_file, shuffle=1, saveiters=50000, displayiters=10000, maxiters=50000) # maxiters=50000 or even less for shorter, demo purposes.
