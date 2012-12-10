%define	gitdate	20102407

Summary:	Tool to reflash firmware by usb
Name:		dfu-util
Version:	0.2
Release:	%mkrel 0.%{gitdate}.2
Source0:	%{name}-%{version}.tar.xz
License:	GPLv2+
Group:		Development/Other
Url:		http://wiki.openmoko.org/wiki/Dfu-util
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	libusb-devel

%description
Dfu-util is a tool to reflash the firmware of compliant usb device.

%prep
%setup -q

%build
%configure 
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(-,root,root)
%{_bindir}/dfu-util
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


