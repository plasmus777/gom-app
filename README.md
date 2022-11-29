# GPU Offloading Manager
1
An application for gnome using GTK4 that allows the user to control and manage their "discrete gpu" through prime-offloading in a simple way.

Modern linux GPU drivers support prime-offloading, but there is no user interface to interact with them. The objective behind this project is to change that.


TODO:
- [ ] Basic Information Gathering/Display
	- [ ] Check for GPU compatibility/driver support
	- [ ] Display basic GPU info (driver, version, vendor...)
	- [ ] Display current power state (enabled, disabled, power drain)
	- [ ] Display running proccesses on the discrete GPU
	
- [ ] Application/Proccess Management
	- [ ] Configure default launch option for integrated/discrete GPU
	- [ ] (Optional) Configure launch variables (allows using scripts/other methods such as the old bumblebee)
	- [ ] Launch using the integrated GPU
	- [ ] Launch using the discrete GPU
	- [ ] Create/manage profiles in order to automatically select the integrated/discrete GPU upon execution
	- [ ] Export/Import profiles to allow profile saving/sharing
	
- [ ] Driver support
	- [ ] Open-source
		- [ ] Nouveau
		- [ ] Amdgpu
	- [ ] Proprietary
		- [ ] Nvidia
		- [ ] Amdgpu-Pro
		
Reminder: I am making this project mostly as a hobby, and as such, no updates/features are a given. I'll try my best to update the project and make sure that it works, but no compromises.
