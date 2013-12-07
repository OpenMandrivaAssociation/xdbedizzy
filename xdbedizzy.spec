Name:		xdbedizzy
Version:	1.1.0
Release:	5
Summary:	Demo of DBE creating a double buffered spinning scene
Group:		Development/X11
Source:		http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License:	MIT
BuildRoot:	%{_tmppath}/%{name}-root

BuildRequires:	x11-util-macros	>= 1.1.5
BuildRequires:	libxext-devel	>= 1.0.3

%description
Xdbedizzy is a demo of DBE creating a double buffered spinning scene.

%prep
%setup -q -n %{name}-%{version}

%build
%configure	--x-includes=%{_includedir}\
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
%{_mandir}/man1/xdbedizzy.1*


%changelog
* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 1.1.0-2mdv2011.0
+ Revision: 671291
- mass rebuild

* Tue Nov 02 2010 Thierry Vignaud <tv@mandriva.org> 1.1.0-1mdv2011.0
+ Revision: 592585
- new release

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.2-4mdv2010.1
+ Revision: 524405
- rebuilt for 2010.1

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.0.2-3mdv2009.0
+ Revision: 226025
- rebuild

* Mon Jan 21 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.0.2-2mdv2008.1
+ Revision: 155931
- Updated BuildRequires and resubmit package.

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Aug 31 2007 Adam Williamson <awilliamson@mandriva.org> 1.0.2-1mdv2008.0
+ Revision: 76442
- fix manpage name
- rebuild for 2008
- minor spec clean
- new release 1.0.2

  + Thierry Vignaud <tv@mandriva.org>
    - do not hardcode lzma extension!!!


* Wed May 31 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-31 18:32:34 (31796)
- rebuild to fix cooker uploading

* Mon May 29 2006 Andreas Hasenack <andreas@mandriva.com>
+ 2006-05-29 14:36:37 (31646)
- renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

* Thu May 04 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-04 21:25:17 (26918)
- increment release

* Thu Apr 27 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-04-27 04:02:05 (26704)
- Adding X.org 7.0 to the repository

