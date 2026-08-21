Name:           pcdata
Version:        1.1
Release:        1%{?dist}
Summary:        Display detailed hardware information, similar to CPU-Z

License:        GPL-3.0-only
URL:            https://github.com/JediFonseca/pcdata
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       dmidecode
Requires:       lm_sensors
Requires:       util-linux
Requires:       xrandr
Requires:       upower
Requires:       pciutils
Requires:       procps-ng
Requires:       iproute
Requires:       usbutils

%description
pcdata is a shell script that displays detailed CPU, RAM, and general
system information directly in the terminal, similar to what CPU-Z
provides on Windows. It also offers a realtime monitoring mode for
several CPU, GPU and RAM informations.

%prep
%autosetup

%build
# Nothing to build, this is a shell script.

%install
install -Dm755 pcdata-fedora %{buildroot}%{_bindir}/pcdata

%files
%{_bindir}/pcdata
%license LICENSE
%doc README.md

%changelog
* Thu Aug 20 2026 Jedi Fonseca <jedifn7@gmail.com> - 1.1-1
- Added GPU information section (--gpu flag), with NVIDIA, AMD, and Intel support
- Added combined realtime monitoring section (--now flag) for CPU, RAM, and GPU
- Added Tailscale IP detection (shown only when Tailscale is installed and active)
- Switched local IP detection to a more reliable method based on the default route
- Added procps-ng, iproute, and usbutils as new dependencies

* Wed Aug 19 2026 Jedi Fonseca <jedifn7@gmail.com> - 1.0-1
- Initial release
