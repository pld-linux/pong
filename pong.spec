Summary:	A library for creating configuration dialogs
Summary(pl):	Biblioteka do tworzenia dialogów konfiguracyjnych
Name:		pong
Version:	1.0.2
Release:	1
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
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
PonG is a library and a GUI tool for creating GNOME dialog boxes from
an XML description. The XML describes the widgets and the gconf keys
to use, and PonG takes care of the rest. It can optionally use
libglade and/or bonobo for the widgets as well.

%description -l pl
PonG to biblioteka i narzêdzie z graficznym interfejsem s³u¿±ce do
tworzenia okienek dialogowych GNOME z opisu w XML. XML opisuje widgety
i klucze gconf jakie maj± byæ u¿ywane, a PonG zajmuje siê ca³± reszt±.
Opcjonalnie mo¿e u¿ywaæ tak¿e libglade i/lub bonobo do widgetów.

%package devel
Summary:	PonG header files
Summary(pl):	Pliki nag³ówkowe PonG
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}

%description devel
PonG developement files.

%description devel -l pl
Pliki nag³ówkowe PonG.

%package static
Summary:	Static PonG library
Summary(pl):	Statyczna biblioteka PonG
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static PonG library.

%description static -l pl
Statyczna biblioteka PonG.

%package edit
Summary:	Dialog box editor
Summary(pl):	Edytor okien dialogowych
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}

%description edit
Dialog box editor.

%description edit -l pl
Edytor okien dialogowych.

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
install -d $RPM_BUILD_ROOT{%{_aclocaldir},%{_applnkdir}/Development}
%{__make} DESTDIR=$RPM_BUILD_ROOT install

mv $RPM_BUILD_ROOT%{_datadir}/aclocal/* $RPM_BUILD_ROOT%{_aclocaldir}
install pong-edit/pong-edit.desktop $RPM_BUILD_ROOT%{_applnkdir}/Development

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc pong-tool/ChangeLog pong/ChangeLog
%attr(755,root,root) %{_bindir}/pong-tool*
%attr(755,root,root) %{_libdir}/*.so.*
%{_datadir}/idl/pong-interface.idl
%{_datadir}/gnome/help/*
%{_datadir}/omf/*

%files devel
%defattr(644,root,root,755)
%doc AUTHORS NEWS README TODO
%attr(755,root,root) %{_bindir}/pong-gconf-schema-export*
%{_libdir}/*.so
%{_libdir}/*.la
%attr(755,root,root) %{_libdir}/*.sh
%{_aclocaldir}/*.m4
%{_includedir}/pong-1

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a

%files edit
%defattr(644,root,root,755)
%doc pong-edit/ChangeLog
%attr(755,root,root) %{_bindir}/pong-edit*
%{_applnkdir}/Development/pong-edit.desktop
%dir %{_datadir}/pong-1
%{_datadir}/pong-1/*.glade
