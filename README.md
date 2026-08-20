# PC Data

Simple shell script to show software and hardware information on Linux.

<img width="739" height="557" alt="Captura_de_tela_20260412_143357" src="https://github.com/user-attachments/assets/92577e06-b153-4ee3-bf3a-d7b265d368e7" />

<img width="635" height="647" alt="Captura_de_tela_20260412_144024" src="https://github.com/user-attachments/assets/eae7f204-df7f-4d0a-917a-417ac03d05c3" />

<img width="610" height="690" alt="Captura_de_tela_20260412_144058" src="https://github.com/user-attachments/assets/423475dc-5eeb-49bd-b4fe-12d1fbab5443" />

# PC Data

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

For the *help* section:

```
pcdata --help
```
