# GPU Offloading Manager
An application for linux using GTK4 for managing application profiles under hybrid graphics (laptops/computers with multiple  GPUs).

## Objective
Linux based systems have always had issues and lack of support regarding computers with multiple video cards.
In the recent years however, manufacturers managed to improve quite a bit in the driver department, implementing several lacking features that improved offloading capabilities.
One of the few things that still did not improve is *application profile selection* - launching a program using a more/less capable GPU automatically/manually.
**GPU Offloading Manager aims to implement an _user interface to configure and launch programs automatically under hybrid systems._**

#### TODO:
- [ ] UI Design

- [ ] Code Implementation

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
