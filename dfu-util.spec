%define rel 1
%define svn_release 4965

%define release 0.svn%{svn_release}.%rel
# tarball generate with 
# cd /tmp
# svn co https://svn.openmoko.org/trunk/src/host/dfu-util 
# tar -cf dfu-util-r4965.tar.gz  dfu-util

Summary: Tool to reflash firmware by usb
Name: dfu-util
Version: 0
Release: %mkrel %release
Source0: %{name}-r%{svn_release}.tar.gz
Patch:   dfu-util-man_install.patch
License: GPLv2+
Group: Development/Other
Url: http://wiki.openmoko.org/wiki/Dfu-util
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: devel(libusb-0.1) 
BuildRequires: libusb-static-devel glibc-static-devel

%description
Dfu-util is a tool to reflash the firmware of compliant usb device.

%prep
%setup -q -n %{name}
%patch -p0

%build
bash autogen.sh 
%configure 
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(-,root,root)
%_bindir/dfu-util
%_bindir/dfu-util_static
%_mandir/man1/*

