Name:           pcdata
Version:        1.0
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

%description
pcdata is a shell script that displays detailed CPU, RAM, and general
system information directly in the terminal, similar to what CPU-Z
provides on Windows. It also offers a realtime monitoring mode for
CPU temperature, clock speed, and multiplier.

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
* Wed Aug 19 2026 Jedi Fonseca <jedifn7@gmail.com> - 1.0-1
- Initial release
