%define major 2
%define libname %mklibname sexy %major
%define develname %mklibname sexy -d

Summary: Collection of widgets for GTK+
Name: libsexy
Version: 0.1.11
Release: 13
Source0: http://releases.chipx86.com/libsexy/libsexy/%{name}-%{version}.tar.bz2
License: LGPL
Group: System/Libraries
Url: http://www.chipx86.com/wiki/Libsexy
BuildRequires: gtk+2-devel
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
Provides: %{mklibname sexy 2 -d} = %version
Obsoletes: %{mklibname sexy 2 -d}
%if "%{_lib}" != "lib"
Provides: %{name}-devel = %version
%endif

%description -n %develname
This is a collection of widgets for GTK+ 2.x.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

# cleanups
rm -f %{buildroot}%_libdir/*.*a

%files -n %libname
%_libdir/*.so.%{major}*

%files -n %develname
%doc ChangeLog AUTHORS NEWS
%_datadir/gtk-doc/html/libsexy
%_includedir/*
%_libdir/*.so
%_libdir/pkgconfig/*
