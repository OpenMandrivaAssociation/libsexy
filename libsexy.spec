%define name libsexy
%define version 0.1.11
%define major 2
%define libname %mklibname sexy %major
%define develname %mklibname sexy -d

Summary: Collection of widgets for GTK+
Name: %{name}
Version: %{version}
Release: %mkrel 12
Source0: http://releases.chipx86.com/libsexy/libsexy/%{name}-%{version}.tar.bz2
License: LGPL
Group: System/Libraries
Url: http://www.chipx86.com/wiki/Libsexy
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
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
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post -n %libname -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %libname -p /sbin/ldconfig
%endif

%files -n %libname
%defattr(-,root,root)
%_libdir/*.so.%{major}*

%files -n %develname
%defattr(-,root,root)
%doc ChangeLog AUTHORS NEWS
%_datadir/gtk-doc/html/libsexy
%_includedir/*
%_libdir/*.so
%_libdir/*.a
%attr(644,root,root) %_libdir/*.la
%_libdir/pkgconfig/*
