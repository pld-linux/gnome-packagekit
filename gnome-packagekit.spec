#
# Conditional build:
%bcond_without	systemd # rely on systemd for session tracking instead of ConsoleKit
#
Summary:	GNOME PackageKit Client
Summary(pl.UTF-8):	Klient PackageKit dla GNOME
Name:		gnome-packagekit
Version:	3.6.1
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-packagekit/3.6/%{name}-%{version}.tar.xz
# Source0-md5:	a4467f482ffb77ae9b2650d25970583f
Patch0:		systemd-fallback.patch
URL:		http://www.packagekit.org/
BuildRequires:	PackageKit-devel >= 0.8.0
BuildRequires:	autoconf >= 2.65
BuildRequires:	automake >= 1.11
BuildRequires:	dbus-devel >= 1.2.0
BuildRequires:	dbus-glib-devel >= 0.74
BuildRequires:	docbook-dtd41-sgml
BuildRequires:	docbook-utils
BuildRequires:	fontconfig-devel
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.32.0
BuildRequires:	gnome-common
BuildRequires:	gnome-doc-utils
BuildRequires:	gtk+3-devel >= 3.0.0
BuildRequires:	gtk-doc >= 1.9
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libcanberra-devel >= 0.10
BuildRequires:	libcanberra-gtk3-devel >= 0.10
BuildRequires:	libnotify-devel >= 0.7.0
BuildRequires:	libtool
BuildRequires:	libxslt-progs
BuildRequires:	pkgconfig
BuildRequires:	polkit-devel
BuildRequires:	python
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.311
%{?with_systemd:BuildRequires:  systemd-devel}
BuildRequires:	udev-glib-devel
BuildRequires:	upower-devel >= 0.9.0
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	yelp-tools
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Requires(post,preun):	glib2 >= 1:2.26.0
Requires:	PackageKit >= 0.8.0
Requires:	polkit-gnome >= 0.92
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides session applications for the PackageKit API.
There are several utilities designed for installing, updating and
removing packages.

%description -l pl.UTF-8
Ten pakiet dostarcza aplikacje sesji dla API PackageKit. Zawiera kilka
narzędzi stworzonych do instalacji, aktualizacji i usuwania pakietów.

%package -n python-gnome-packagekit
Summary:	Widgets to use PackageKit in GTK+ applications
Summary(pl.UTF-8):	Widgety do użycia PackageKit w aplikacjach GTK+
Group:		Libraries/Python
Requires:	gnome-packagekit = %{version}-%{release}
Requires:	python-packagekit
Requires:	python-pygtk-gtk

%description -n python-gnome-packagekit
This module provides widgets to use PackageKit in GTK+ applications.

%description -n python-gnome-packagekit -l pl.UTF-8
Ten moduł dostarcza widgety do użycia PackageKit w aplikacjach GTK+.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	%{__enable_disable systemd systemd} \
	--disable-schemas-compile

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%py_postclean

%find_lang %{name} --with-gnome --with-omf

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor
%update_desktop_database
%glib_compile_schemas

%postun
%update_icon_cache hicolor
%update_desktop_database_postun
%glib_compile_schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog COPYING NEWS README
%attr(755,root,root) %{_bindir}/gpk-application
%attr(755,root,root) %{_bindir}/gpk-dbus-service
%attr(755,root,root) %{_bindir}/gpk-distro-upgrade
%attr(755,root,root) %{_bindir}/gpk-install-catalog
%attr(755,root,root) %{_bindir}/gpk-install-local-file
%attr(755,root,root) %{_bindir}/gpk-install-mime-type
%attr(755,root,root) %{_bindir}/gpk-install-package-name
%attr(755,root,root) %{_bindir}/gpk-install-provide-file
%attr(755,root,root) %{_bindir}/gpk-log
%attr(755,root,root) %{_bindir}/gpk-prefs
%attr(755,root,root) %{_bindir}/gpk-service-pack
%attr(755,root,root) %{_bindir}/gpk-update-viewer
%{_datadir}/GConf/gsettings/org.gnome.packagekit.gschema.migrate
%{_datadir}/dbus-1/services/org.freedesktop.PackageKit.service
%{_datadir}/glib-2.0/schemas/org.gnome.packagekit.gschema.xml
%{_datadir}/gnome-packagekit
%{_iconsdir}/hicolor/*/*/*
%{_desktopdir}/gpk-application.desktop
%{_desktopdir}/gpk-dbus-service.desktop
%{_desktopdir}/gpk-distro-upgrade.desktop
%{_desktopdir}/gpk-install-catalog.desktop
%{_desktopdir}/gpk-install-local-file.desktop
%{_desktopdir}/gpk-log.desktop
%{_desktopdir}/gpk-prefs.desktop
%{_desktopdir}/gpk-service-pack.desktop
%{_desktopdir}/gpk-update-viewer.desktop
%{_mandir}/man1/gpk-application.1*
%{_mandir}/man1/gpk-backend-status.1*
%{_mandir}/man1/gpk-install-local-file.1*
%{_mandir}/man1/gpk-install-mime-type.1*
%{_mandir}/man1/gpk-install-package-name.1*
%{_mandir}/man1/gpk-install-provide-file.1*
%{_mandir}/man1/gpk-prefs.1*
%{_mandir}/man1/gpk-repo.1*
%{_mandir}/man1/gpk-update-icon.1*
%{_mandir}/man1/gpk-update-viewer.1*

%files -n python-gnome-packagekit
%defattr(644,root,root,755)
%{py_sitescriptdir}/packagekit/*.py[co]
