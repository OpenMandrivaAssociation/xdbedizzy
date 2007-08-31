Name:		xdbedizzy
Version:	1.0.2
Release:	%mkrel 1
Summary:	Demo of DBE creating a double buffered spinning scene
Group:		Development/X11
Source:		http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License:	MIT
BuildRoot:	%{_tmppath}/%{name}-root

BuildRequires:	x11-util-macros >= 1.0.1
BuildRequires:	libxext-devel >= 1.0.0

%description
Xdbedizzy is a demo of DBE creating a double buffered spinning scene.

%prep
%setup -q -n %{name}-%{version}

%build
%configure2_5x	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/xdbedizzy
%{_mandir}/man1/xdbedizzy.1x*

