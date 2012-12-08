%define major 2
%define libname %mklibname sexy %major
%define develname %mklibname sexy -d

Summary: Collection of widgets for GTK+
Name: libsexy
Version: 0.1.11
Release: 14
Source0: http://releases.chipx86.com/libsexy/libsexy/%{name}-%{version}.tar.bz2
Patch0: %{name}-%{version}-url-label.patch
Patch1: %{name}-icon-name.patch
Patch2: gtk2-single-include.patch
License: LGPL
Group: System/Libraries
Url: http://www.chipx86.com/wiki/Libsexy
BuildRequires: gtk+2-devel
BuildRequires: glib2-devel
BuildRequires: gtk-doc

%description
This is a collection of widgets for GTK+ 2.x.

%package -n %libname
Group:System/Libraries
Summary: Collection of widgets for GTK+
#gw watch for major number changes
Requires: %mklibname enchant 1

%description -n %libname
This is a collection of widgets for GTK+ 2.x.

%package -n %develname
Group:Development/C
Summary: Collection of widgets for GTK+
Requires: %libname = %version
Provides: %{mklibname sexy 2 -d} = %{EVRD}
Obsoletes: %{mklibname sexy 2 -d}
%if "%{_lib}" != "lib"
Provides: %{name}-devel = %{EVRD}
%endif

%description -n %develname
This is a collection of widgets for GTK+ 2.x.

%prep
%setup -q
%patch0 -p1 -b .url-label
%patch1 -p1 -b .icon-name
%patch2 -p1 -b .gtk-single-include

%build
export LIBS=`pkg-config --libs gmodule-2.0`
%configure2_5x --disable-static
%make

%install
%makeinstall_std

%files -n %libname
%_libdir/*.so.%{major}*

%files -n %develname
%doc ChangeLog AUTHORS NEWS
%_datadir/gtk-doc/html/libsexy
%_includedir/*
%_libdir/*.so
%_libdir/pkgconfig/*


%changelog
* Tue Jan 31 2012 Oden Eriksson <oeriksson@mandriva.com> 0.1.11-13
+ Revision: 770067
- fix build
- sync with the fedora patches
- various cleanups

* Mon Sep 19 2011 Götz Waschk <waschk@mandriva.org> 0.1.11-12
+ Revision: 700316
- rebuild

* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 0.1.11-11
+ Revision: 661525
- mass rebuild

* Sun Nov 28 2010 Oden Eriksson <oeriksson@mandriva.com> 0.1.11-10mdv2011.0
+ Revision: 602605
- rebuild

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 0.1.11-9mdv2010.1
+ Revision: 520904
- rebuilt for 2010.1

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.1.11-8mdv2010.0
+ Revision: 425720
- rebuild

* Sun Nov 09 2008 Oden Eriksson <oeriksson@mandriva.com> 0.1.11-7mdv2009.1
+ Revision: 301469
- rebuilt against new libxcb

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 0.1.11-6mdv2009.0
+ Revision: 222985
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Tue Mar 04 2008 Oden Eriksson <oeriksson@mandriva.com> 0.1.11-5mdv2008.1
+ Revision: 178937
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Tue Sep 18 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.1.11-3mdv2008.0
+ Revision: 89848
- rebuild

* Fri Aug 31 2007 Oden Eriksson <oeriksson@mandriva.com> 0.1.11-2mdv2008.0
+ Revision: 76768
- new devel naming


* Sun Apr 01 2007 Götz Waschk <waschk@mandriva.org> 0.1.11-1mdv2007.1
+ Revision: 150155
- new version

* Wed Jan 24 2007 Götz Waschk <waschk@mandriva.org> 0.1.10-2mdv2007.1
+ Revision: 112818
- rebuild
- Import libsexy

* Wed Sep 06 2006 Götz Waschk <waschk@mandriva.org> 0.1.10-1mdv2007.0
- new version

* Wed Sep 06 2006 Götz Waschk <waschk@mandriva.org> 0.1.8-2mdv2007.0
- fix enchant dep

* Sun Mar 19 2006 Götz Waschk <waschk@mandriva.org> 0.1.8-1mdk
- fix URL
- New release 0.1.8

* Thu Mar 16 2006 Götz Waschk <waschk@mandriva.org> 0.1.7-1mdk
- major 2
- source URL
- new version

* Mon Feb 06 2006 Götz Waschk <waschk@mandriva.org> 0.1.6-1mdk
- update file list
- fix buildrequires
- New release 0.1.6

* Mon Jan 23 2006 Götz Waschk <waschk@mandriva.org> 0.1.5-1mdk
- New release 0.1.5
- use mkrel

* Fri Nov 25 2005 Götz Waschk <waschk@mandriva.org> 0.1.4-2mdk
- fix buildrequires

* Thu Nov 24 2005 Götz Waschk <waschk@mandriva.org> 0.1.4-1mdk
- initial package

