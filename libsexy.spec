%define major	2
%define libname	%mklibname sexy %{major}
%define devname	%mklibname sexy -d

Summary:	Collection of widgets for GTK+
Name:		libsexy
Version:	0.1.11
Release:	29
License:	LGPLv2
Group:		System/Libraries
Url:		https://www.chipx86.com/wiki/Libsexy
Source0:	http://releases.chipx86.com/libsexy/libsexy/%{name}-%{version}.tar.bz2
Patch0:		%{name}-%{version}-url-label.patch
Patch1:		%{name}-icon-name.patch
Patch2:		gtk2-single-include.patch
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

%build
export LIBS=$(pkg-config --libs gmodule-2.0)
%configure --disable-static
%make_build

%install
%make_install

%files -n %{libname}
%{_libdir}/libsexy.so.%{major}*

%files -n %{devname}
%doc ChangeLog AUTHORS NEWS
%{_datadir}/gtk-doc/html/libsexy
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
