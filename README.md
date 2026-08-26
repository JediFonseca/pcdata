## ⚠️ Personal Project

PCData was built for my own personal use. The repository is public and anyone is welcome to use, fork, or modify it freely. That said, since this is a hobby project maintained in my spare time, I may not always be able to provide support to third parties. I'll help if I can, but there are no guarantees. Issues and pull requests may go unanswered. Use it as-is, at your own risk.

**Dual GPU is currently unsupported.**

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

Run `pcdata` on a terminal:

```bash
pcdata
```

## Prints

<img width="824" height="767" alt="Captura de tela de 2026-08-21 02-15-34" src="https://github.com/user-attachments/assets/0a1cb77c-6939-48fc-9252-6082e64d52dd" />

<img width="710" height="657" alt="Captura de tela de 2026-08-21 02-15-53" src="https://github.com/user-attachments/assets/1fb5eea8-9e4b-42b2-a3f6-381d93087c5b" />

<img width="710" height="753" alt="Captura de tela de 2026-08-21 02-16-05" src="https://github.com/user-attachments/assets/e4029885-c820-4c15-8cea-99e684d4fa62" />

<img width="735" height="407" alt="Captura de tela de 2026-08-21 02-16-20" src="https://github.com/user-attachments/assets/28c21315-33b1-45b0-a0c4-f922fd0bc915" />

<img width="611" height="443" alt="Captura de tela de 2026-08-21 02-16-35" src="https://github.com/user-attachments/assets/cf817b99-207d-41ad-816e-975c2c7f141b" />
