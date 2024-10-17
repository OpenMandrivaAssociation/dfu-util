Summary:	Tool to reflash firmware by usb
License:	GPLv2+
Group:		Development/Other
Name:		dfu-util
Version:	0.11
Release:	1
Source0:	https://sourceforge.net/projects/dfu-util/files/dfu-util-%{version}.tar.gz
Url:		https://wiki.openmoko.org/wiki/Dfu-util

BuildRequires: pkgconfig(libusb-1.0)

%description
Dfu-util is a tool to reflash the firmware of compliant usb device.
DFU is intended to download and upload firmware to/from devices
connected over USB.

%prep
%autosetup -p1

%build
%configure 
%make_build

%install
%make_install

%files 
%defattr(-,root,root)
%{_bindir}/dfu-util
%{_bindir}/dfu-prefix
%{_bindir}/dfu-suffix
%{_mandir}/man1/*


%changelog
* Tue May 03 2011 Michael Scherer <misc@mandriva.org> 0.2-0.20102407.2mdv2011.0
+ Revision: 664834
- mass rebuild

  + Per Øyvind Karlsen <peroyvind@mandriva.org>
    - update to latest code from git (899d6dadadfca07f0290da519f1769e5d0193721)
    - apply some cosmetics

* Wed Apr 08 2009 Michael Scherer <misc@mandriva.org> 0-0.svn4965.1mdv2009.1
+ Revision: 365206
- add another missing buildrequires
- add missing BuildRequires
- import dfu-util


