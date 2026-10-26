# The LTO configure workaround rewrites this ancient libtool script into a
# command that starts with -e, so the shared library is never produced.
%global _disable_lto 1

%define major	2
%define libname	%mklibname sexy %{major}
%define devname	%mklibname sexy -d

Summary:	Collection of widgets for GTK+
Name:		libsexy
Version:	0.1.11
Release:	31
License:	LGPLv2
Group:		System/Libraries
Url:		https://www.chipx86.com/wiki/Libsexy
Source0:	http://releases.chipx86.com/libsexy/libsexy/%{name}-%{version}.tar.bz2
Patch0:		%{name}-%{version}-url-label.patch
Patch1:		%{name}-icon-name.patch
Patch2:		gtk2-single-include.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool-base
BuildRequires:	slibtool
BuildRequires:	make
BuildRequires:	gtk-doc
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(libxml-2.0)

%description
This is a collection of widgets for GTK+ 2.x.

%package -n %{libname}
Summary:	Collection of widgets for GTK+
Group:		System/Libraries

%description -n %{libname}
This is a collection of widgets for GTK+ 2.x.

%package -n %{devname}
Summary:	Collection of widgets for GTK+
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
%if "%{_lib}" != "lib"
Provides:	%{name}-devel = %{EVRD}
%endif

%description -n %{devname}
This is a collection of widgets for GTK+ 2.x.

%prep
%autosetup -p1
# The upstream pc file hardcodes ${exec_prefix}/lib, which is the 32-bit
# directory. pkg-config then adds -L/usr/lib and the link becomes elf32-i386.
sed -i 's|^libdir=.*|libdir=@libdir@|' libsexy.pc.in

%build
export LIBS=$(pkg-config --libs gmodule-2.0)
%configure --disable-static
%make_build LIBTOOL=slibtool-shared

%install
%make_install LIBTOOL=slibtool-shared

%files -n %{libname}
%{_libdir}/libsexy.so.%{major}*

%files -n %{devname}
%doc ChangeLog AUTHORS NEWS
%{_datadir}/gtk-doc/html/libsexy
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
