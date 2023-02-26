# GPU Offloading Manager
A linux application to configure applications and hybrid graphics on linux

### **GPU Offloading Manager aims to implement an _user interface to configure and launch programs automatically under hybrid systems._**

### Objective
Linux based systems have always had issues and lack of support regarding computers with multiple video cards.
In the recent years however, manufacturers managed to improve quite a bit in the driver department, implementing several lacking features that improved offloading capabilities.
One of the few things that still did not improve is *application profile selection* - launching a program using a more/less capable GPU automatically/manually.

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
    - [ ] Tar.gz file
    - [ ] Flatpak support
    - [ ] Snap support

### Extra notes
- This application is NOT a driver/switcher utility (like prime-select or others). What is does is simply allow the user to select the default graphic card for installed applications under systems with hydrid graphics.
- The application expects your system to already have your drivers configured. Follow your distribution documentation before using Gpu Offloading Manager.

<sub>Reminder: This project is mostly a hobby, and as such, no updates/features are a given. I'll try my best to update the project and make sure that it works, but no compromises.</sub>
