from gi.repository import GLib
import os
import sys
import subprocess
import json

#display server, either 'wayland' or 'x11'
display_server = os.getenv('XDG_SESSION_TYPE')

#default gom-app config folder
config_folder = os.path.join(GLib.get_user_config_dir(), 'gom-app/')
#folder for saved application profiles
profiles_folder = os.path.join(config_folder, 'profiles/')

#config file containing gpu information
gpu_info = os.path.join(config_folder, 'gpu_info.json')
#command to update the .json file with collected gpu information
upd = 'pkexec lshw -C display -json > ' + gpu_info
f_upd = 'flatpak-spawn --host ' + upd

class Config:
    def update_gpu_info(self):
        if os.getenv('FLATPAK_ID'):
            subprocess.run(f_upd, shell=True)
        else:
            subprocess.run(upd, shell=True)
        print('Updated gpu information.')

    def load_info(self):
        with open(gpu_info) as f:
            info = json.load(f)
            print(info)
        print('Loaded gpu information.')

    def initialize(self):
        #Verify gom-app folder existance
        if os.path.exists(config_folder) == False:
            try:
                os.makedirs(config_folder)
                print('Created config directory "%s".' % config_folder)
            except OsError as error:
                print('Could not create the config directory "%s".' % config_folder)
        #Verify gom-app/profiles existance
        if os.path.exists(profiles_folder) == False:
            try:
                os.makedirs(profiles_folder)
                print('Created config directory "%s".' % profiles_folder)
            except OsError as error:
                print('Could not create the config directory "%s".' % profiles_folder)
        #Verify gpu_info.json existance, updating information
        if os.path.exists(gpu_info) == False:
            self.update_gpu_info()

        print('Checking for config files.')
