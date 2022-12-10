# GPU Offloading Manager
An application for linux using GTK4 for managing application profiles under hybrid graphics (laptops/computer with multiple  GPUs).

##Why would I want this?
Linux based systems have always had issues and lack of support regarding computers with multiple video cards.
In the recent years however, GPU manufacturers managed to improve quite a bit in the driver department, implementing several lacking features that improved the GPU offloading situation.
One of the few things that still did not improve is *application profile selection* - launching a program using a more/less capable GPU automatically/manually.
**GPU Offloading Manager aims to implement an _user interface to  configure and launch programs automatically using a determined GPU under hybrid systems._ **

####TODO:
- [ ] UI Implementation
    - [X] GTK Window
    - [X] Primary Menu
        - [ ] Preferences Submenu
            - [ ] Application Preferences
            - [ ] Integrated GPU Preferences
            - [ ] Discrete GPU Preferences
        - [ ] Keyboard Shortcuts Submenu
        - [ ] Help Submenu
        - [ ] About Submenu
    - [ ] Interactive Panels
        - [X] Basic Display Information Panel
        - [ ] Application Profiles Panel
        - [ ] Running Applications (using GOM)
    
- [ ] Code Implementation for all of the above
    
- [ ] Driver support
	- [ ] Open-source
		- [ ] Nouveau
		- [ ] Amdgpu
	- [ ] Proprietary
		- [ ] Nvidia
		- [ ] Amdgpu-Pro
		
- [ ] Packaging
    - [ ] Compiling Instructions
    - [ ] Tar.gz
    - [ ] Flatpak through Flathub
    - [ ] (perhaps?) AppImage

<sub>Reminder: This project is mostly a hobby, and as such, no updates/features are a given. I'll try my best to update the project and make sure that it works, but no compromises.</sub>
