## archinstall/lib/installer.py

gen_fstab = SysCommand(f'genfstab {flags} -f {self.target} {self.target}').output()
## prevents boot hangs when doing host-to-target(h2t) installs instead of from ISO/USB. Good for quick dev or travel (speaking of experience bricked my install in South of France had no USB but 2 disks)

## Add a def that determines if running from ISO or installed system
## In case of the latter, check subdeps used by archinstall.
## Otherwise user will get errors during install because he's missing X or Y that is present in ISO but not on typical host installed HOST

## Prevent host pollution
## So for example when running from a host we want to set console kb locale but not change it globally just for the session
## The same for mirrorlist: no touching if it's from a host we can simply use as is 

## archinstall/lib/pacman/__init__.py

f'pacstrap -C /etc/pacman.conf -K {self.target} {" ".join(packages)} --noconfirm --needed',
# prevents re-installs from meta-packages / overlaps

## archinstall/lib/hardware.py

# I think you should also pre-load hw detection here as on slow hardware seems to take a bit of time to open the profile/hardware TUI section.

# Add nvidia-prime if hybrid graphics detected (Intel/AMD iGPU + Nvidia dGPU) # Very common cases in many laptops
NvidiaPrime = 'nvidia-prime'

if self.is_nvidia() and (SysInfo.has_intel_graphics() or SysInfo.has_amd_graphics()):
  packages.append(GfxPackage.NvidiaPrime)

# Also added: For VMs allowing to run GTK/Adw apps under QEMU/VB (cool fix IMO ;)
## Software render fallback
VulkanSwrast = 'vulkan-swrast'

# Divided group into 2 VM groups:  
# Altho I have only ever tested in QEMU but I'm guessing anything that works well for QEMU is probably good to have on VB/VMware 
# Could be useful for guest-utils pkgs or clipboard share but obviously that'd be more pkgs... Not minimal change.

# archinstall/lib/mirrors.py

#### Super important
## I added a fallback from archlinux.org/mirrors/status to local list
## Cannot remember when but it was down for 24-48h the other time and well nobody could use your code: stuck on loading mirrors...
## While the mirrorlist exists on disk
## Made a small menu to select mirrors manually if timeout say 15 seconds
## Region > Re-order them in a list first selected = highest prio > Filter https only

## General
## In modified menu I added 2-3 things
## Seperate EFI option in guided (works only for grub single disk best-effort in my fork) or traditional /boot/efi 
## Based on this and Bootloader choice:
## Prompt for /boot size (useful if user wants to test out several kernels/UKI larger images)

## Add a small status icon to the main README in github so that users can see if CI is failing
