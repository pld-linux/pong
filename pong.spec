Summary:	A library for creating configuration dialogs
Summary(pl):	Biblioteka do tworzenia dialogów konfiguracyjnych
Name:		pong
Version:	1.0.2
Release:	0.2
License:	GPL
Group:		X11/Libraries
Source0:	http://ftp.5z.com/pub/pong/%{name}-%{version}.tar.gz
URL:		http://www.gnome.org/
BuildRequires:	GConf >= 0.6.0
BuildRequires:	bonobo >= 0.36
BuildRequires:	gdk-pixbuf >= 0.7.0
BuildRequires:	gob >= 1.0.7
BuildRequires:	libglade
BuildRequires:	libxml
BuildRequires:	oaf >= 0.6.0
BuildRequires:	sed
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
PonG is a library and a GUI tool for creating GNOME dialog boxes from
an XML description. The XML describes the widgets and the gconf keys
to use, and PonG takes care of the rest. It can optionally use
libglade and/or bonobo for the widgets as well.

%package devel
Summary:	pong
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}

%description devel
Pong developement files.

%package static
Summary:	A library for creating configuration dialogs
Summary(pl):	Biblioteka do tworzenia dialogów konfiguracyjnych
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static pong library.

%description static -l pl
Statyczna biblioteka pong.

%package edit
Summary:	A library for creating configuration dialogs
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}

%description edit

%prep
%setup -q

%build
sed -e s/AM_GNOME_GETTEXT/AM_GNU_GETTEXT/ configure.in > configure.in.tmp
mv -f configure.in.tmp configure.in
#%{__libtoolize}
#xml-i18n-toolize --copy --force
#aclocal -I intl
#autoconf
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root} %{_bindir}/pong-tool*
%{_libdir}/*.so.*
%{_datadir}/idl/pong-interface.idl
%{_datadir}/locale/*/*/*
%{_datadir}/gnome/help/*
%{_datadir}/omf/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root} %{_bindir}/pong-gconf-schema-export*
%{_libdir}/*.so
%{_libdir}/*.la
%{_libdir}/*.sh
%{_aclocaldir}/*.m4
%{_includedir}/pong-1/*/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a

%files edit
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pong-edit-1
%attr(755,root,root) %{_bindir}/pong-edit
%{_applnkdir}/Development/pong-edit.desktop
%{_datadir}/pong-1/pong-edit.glade
