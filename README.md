# PC Data

Simple shell script to show software and hardware information on Linux.

## How to install (On Fedora 44 via COPR)

1. Add the *copr* repository to your system:

```
sudo dnf copr enable jedifonseca/pcdata
```

2. Install *pcdata*

```
sudo dnf install pcdata
```

All the dependencies *pcdata* needs will be installed with it.

**List of dependencies: (Based on Fedora 44)**
- dmidecode
- util-linux
- lm_sensors
- pciutils
- upower
- xrandr

*On other distros, for now, you'll have to comment the "safety_checks" line, at the end of the file,
and run "./pcdata-fedora" directly. Be sure to have all the dependencies installed.*

## How to use

For the basic/general system information:

```
pcdata
```

For information about the CPU:

```
pcdata --cpu
```

For information about the RAM modules:

```
pcdata --ram
```

For information about the GPU:

```
pcdata --gpu
```

For all the realtime information about the CPU, GPU and RAM:

```
pcdata --now
```

For the *help* section:

```
pcdata --help
```

## Prints

<img width="824" height="767" alt="Captura de tela de 2026-08-21 02-15-34" src="https://github.com/user-attachments/assets/aed3ab22-7774-4e0f-8c83-45d108d9f058" />

<img width="710" height="657" alt="Captura de tela de 2026-08-21 02-15-53" src="https://github.com/user-attachments/assets/26d6b32e-8af4-47f0-899f-e202be487676" />

<img width="710" height="753" alt="Captura de tela de 2026-08-21 02-16-05" src="https://github.com/user-attachments/assets/253a45bf-ec06-45e6-a7fd-5271b24fa003" />

<img width="735" height="407" alt="Captura de tela de 2026-08-21 02-16-20" src="https://github.com/user-attachments/assets/ff92312c-9bff-4ee0-98ae-2388a719a559" />

<img width="611" height="443" alt="Captura de tela de 2026-08-21 02-16-35" src="https://github.com/user-attachments/assets/75c19d01-a445-4049-837d-87caa05783e5" />
