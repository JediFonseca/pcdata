## ⚠️ Personal Project

PCData was built for my own personal use. The repository is public and anyone is welcome to use, fork, or modify it freely. That said, since this is a hobby project maintained in my spare time, I may not always be able to provide support to third parties. I'll help if I can, but there are no guarantees. Issues and pull requests may go unanswered. Use it as-is, at your own risk.

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

---

```bash
pcdata --cpu
```

Displays detailed CPU information, including realtime CPU data.

---

```bash
pcdata --ram
```

Displays detailed RAM information, including information for each memory slot.

---

```bash
pcdata --gpu
```

Displays detailed GPU information and realtime GPU data.

*Dual GPU is currently unsupported.*

---

```bash
pcdata --now
```

Displays realtime CPU, RAM, swap, and GPU information together.

---

```bash
pcdata --update
```

Updates PCData to the latest available version.

---

```bash
pcdata --uninstall
```

Completely uninstalls PCData.

## Prints

<img width="824" height="767" alt="Captura de tela de 2026-08-21 02-15-34" src="https://github.com/user-attachments/assets/39a9f61c-7e52-4a12-990d-a8cb7638d84e" />
<img width="710" height="657" alt="Captura de tela de 2026-08-21 02-15-53" src="https://github.com/user-attachments/assets/69a15911-4cb3-45fc-b1f9-bca70822da56" />
<img width="710" height="753" alt="Captura de tela de 2026-08-21 02-16-05" src="https://github.com/user-attachments/assets/de0c7f9a-d6b2-46d1-8069-c594b85bbdbd" />
<img width="735" height="407" alt="Captura de tela de 2026-08-21 02-16-20" src="https://github.com/user-attachments/assets/4c390775-e7c1-43d2-95d4-5890c7aae676" />
<img width="611" height="443" alt="Captura de tela de 2026-08-21 02-16-35" src="https://github.com/user-attachments/assets/c376da7b-05cf-4f34-82a8-770ced958bd5" />
