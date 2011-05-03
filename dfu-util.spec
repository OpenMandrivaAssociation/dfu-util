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
