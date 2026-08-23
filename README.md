# PCData

PCData is a simple Bash script that displays detailed system and hardware information directly in the terminal, inspired by the style and organization of tools such as CPU-Z and GPU-Z.

It provides general system information as well as detailed information about the CPU, RAM, and GPU. It also includes realtime information such as CPU usage, temperature, clock speed, RAM usage, GPU usage, temperature, clock speed, and power draw when supported by the hardware and installed software.

The project is a hobby/personal project focused on being simple, readable, and easy to maintain.

## Installation

Run the following command in a terminal:

```bash
wget -qO- "https://raw.githubusercontent.com/JediFonseca/pcdata/refs/heads/main/pcdata-install" | sudo bash
```

The installer will:

1. Detect the Linux distribution.
2. Install the required dependencies.
3. Download `pcdata` and `pcdata-manager` to `/usr/bin`.
4. Give both scripts execution permissions.

### Distribution support

PCData currently supports Debian/Ubuntu-based, Arch-based and Fedora-based systems.

## Usage

Run `pcdata` without any arguments to display general system information:

```bash
pcdata
```

### Available options

```bash
pcdata --help
```

Displays usage information and the required dependencies.

```bash
pcdata --cpu
```

Displays detailed CPU information, including realtime CPU data.

```bash
pcdata --ram
```

Displays detailed RAM information, including information for each memory slot.

```bash
pcdata --gpu
```
*Dual GPU is currently unsupported.*

Displays detailed GPU information and realtime GPU data.

```bash
pcdata --now
```

Displays realtime CPU, RAM, swap, and GPU information together.

```bash
pcdata --update
```

Updates PCData to the latest available version.

```bash
pcdata --uninstall
```

Completely uninstalls PCData.

### Exiting realtime modes

The `--cpu`, `--ram`, `--gpu`, and `--now` modes continuously update the displayed information.

Press:

```bash
CTRL+C
```

to exit.
