from gi.repository import GLib
import os
import sys
import subprocess
import json
from .notify import *

class Config:
    #display server, either 'wayland' or 'x11'
    display_server = os.getenv('XDG_SESSION_TYPE')

    #default gom-app config folder
    config_folder = os.path.join(GLib.get_user_config_dir(), 'gom-app/')
    #folder for saved application profiles
    profiles_folder = os.path.join(config_folder, 'profiles/')

    #config file containing gpu information
    gpu_info = os.path.join(config_folder, 'gpu_info.json')
    #command to update the .json file with collected gpu information
    #pkexec
    upd = 'lshw -quiet -C display -json > ' + gpu_info
    f_upd = 'flatpak-spawn --host ' + upd

    #Gpu information - integrated
    integrated_info = {'Vendor_i', 'Product_i', 'Description_i', 'Driver_i', 'Bus_i'}

    #Gpu information - discrete
    discrete_info = {'Vendor_d', 'Product_d', 'Description_d', 'Driver_d', 'Bus_d'}

    def update_gpu_info(self):
        if os.getenv('FLATPAK_ID'):
            subprocess.run(self.f_upd, shell=True)
        else:
            subprocess.run(self.upd, shell=True)

        Notify.send_notification('Updated gpu information.')

    def load_info(self):
        with open(self.gpu_info) as f:
            info = json.load(f)
            for i in info:
                print('######################################')
                print(i['vendor'])
                print(i['product'])
                print(i['description'])
                print(i['configuration']['driver'])
                print(i['handle'])

        print('Loaded gpu information.')

    def initialize(self):
        #Verify gom-app folder existance
        if os.path.exists(self.config_folder) == False:
            try:
                os.makedirs(self.config_folder)
                print('Created config directory "%s".' % self.config_folder)
            except OsError as error:
                Notify.send_notification('Could not create the config directory "%s".' % self.config_folder)
        #Verify gom-app/profiles existance
        if os.path.exists(self.profiles_folder) == False:
            try:
                os.makedirs(self.profiles_folder)
                print('Created config directory "%s".' % self.profiles_folder)
            except OsError as error:
                Notify.send_notification('Could not create the config directory "%s".' % self.profiles_folder)
        #Verify gpu_info.json existance, updating information
        if os.path.exists(self.gpu_info) == False:
            self.update_gpu_info()

        print('Checking for config files.')
        self.load_info()


