## archinstall/lib/installer.py

gen_fstab = SysCommand(f'genfstab {flags} -f {self.target} {self.target}').output()
# prevents boot hangs when doing host-to-target(h2t) installs instead of from ISO/USB. Good for quick dev or travel.

## Add a def that determines if running from ISO or installed system
## In case of the latter, check subdeps used by archinstall.

## archinstall/lib/pacman/__init__.py

f'pacstrap -C /etc/pacman.conf -K {self.target} {" ".join(packages)} --noconfirm --needed',
# prevents re-installs from meta-packages / overlaps

## General
## In modified menu I added 2-3 things

## Seperate EFI option in guided (works only for grub single disk best-effort in my fork) or traditional /boot/efi 

## Based on this and Bootloader choice:
## Prompt for /boot size (useful if user wants to test out several kernels/UKI larger images)

