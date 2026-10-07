Name:           oosha512
Version:        0.1.0
Release:        1%{?dist}
Summary:        High-capacity SHA-512 cryptographic digest generator with binary output mode.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/oosha512
Source0:        oosha512-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
oosha512 is a sovereign, capability-bounded SHA512 HASHER written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/oosha512
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/oosha512-uninstall

%files
/usr/bin/oosha512
/usr/bin/oosha512-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
