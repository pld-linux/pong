Summary:	A library for creating configuration dialogs
Summary(pl.UTF-8):	Biblioteka do tworzenia dialogów konfiguracyjnych
Name:		pong
Version:	1.0.2
Release:	1
License:	GPL
Group:		X11/Libraries
Source0:	http://ftp.5z.com/pub/pong/%{name}-%{version}.tar.gz
# Source0-md5:	6d794f21b5e6d09eb438f432725cb3d4
URL:		http://www.gnome.org/
BuildRequires:	GConf-devel >= 0.6.0
BuildRequires:	automake
BuildRequires:	bonobo-devel >= 0.36
BuildRequires:	gdk-pixbuf-gnome-devel >= 0.7.0
BuildRequires:	gob >= 1.0.7
BuildRequires:	libglade-gnome-devel
BuildRequires:	libxml-devel
BuildRequires:	oaf-devel >= 0.6.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PonG is a library and a GUI tool for creating GNOME dialog boxes from
an XML description. The XML describes the widgets and the gconf keys
to use, and PonG takes care of the rest. It can optionally use
libglade and/or bonobo for the widgets as well.

%description -l pl.UTF-8
PonG to biblioteka i narzędzie z graficznym interfejsem służące do
tworzenia okienek dialogowych GNOME z opisu w XML. XML opisuje widgety
i klucze gconf jakie mają być używane, a PonG zajmuje się całą resztą.
Opcjonalnie może używać także libglade i/lub bonobo do widgetów.

%package devel
Summary:	PonG header files
Summary(pl.UTF-8):	Pliki nagłówkowe PonG
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
PonG developement files.

%description devel -l pl.UTF-8
Pliki nagłówkowe PonG.

%package static
Summary:	Static PonG library
Summary(pl.UTF-8):	Statyczna biblioteka PonG
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static PonG library.

%description static -l pl.UTF-8
Statyczna biblioteka PonG.

%package edit
Summary:	Dialog box editor
Summary(pl.UTF-8):	Edytor okien dialogowych
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description edit
Dialog box editor.

%description edit -l pl.UTF-8
Edytor okien dialogowych.

%prep
%setup -q

%build
sed -e s/AM_GNOME_GETTEXT/AM_GNU_GETTEXT/ configure.in > configure.in.tmp
mv -f configure.in.tmp configure.in
#%%{__libtoolize}
#xml-i18n-toolize --copy --force
#%{__aclocal} -I intl
#%{__autoconf}
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_aclocaldir},%{_applnkdir}/Development}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install pong-edit/pong-edit.desktop $RPM_BUILD_ROOT%{_applnkdir}/Development

%find_lang %{name} --with-gnome

mv pong-tool/ChangeLog ChangeLog.pong-tool
mv pong/ChangeLog ChangeLog.pong

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog* NEWS README TODO
%attr(755,root,root) %{_bindir}/pong-tool*
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%{_datadir}/idl/pong-interface.idl
%{_datadir}/omf/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pong-gconf-schema-export*
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%attr(755,root,root) %{_libdir}/*.sh
%{_aclocaldir}/*.m4
%{_includedir}/pong-1

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files edit
%defattr(644,root,root,755)
%doc pong-edit/ChangeLog
%attr(755,root,root) %{_bindir}/pong-edit*
%{_applnkdir}/Development/pong-edit.desktop
%dir %{_datadir}/pong-1
%{_datadir}/pong-1/*.glade
