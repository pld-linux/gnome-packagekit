#
# Conditional build:
%bcond_without	systemd	# rely on systemd for session tracking instead of ConsoleKit
#
Summary:	GNOME PackageKit Client
Summary(pl.UTF-8):	Klient PackageKit dla GNOME
Name:		gnome-packagekit
Version:	3.24.0
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-packagekit/3.24/%{name}-%{version}.tar.xz
# Source0-md5:	fb460341360b91977eeba35c8e38d3ba
Patch0:		systemd-fallback.patch
URL:		http://www.packagekit.org/
BuildRequires:	PackageKit-devel >= 0.9.1
BuildRequires:	appstream-glib-devel
BuildRequires:	autoconf >= 2.65
BuildRequires:	automake >= 1.11
BuildRequires:	dbus-devel >= 1.2.0
BuildRequires:	dbus-glib-devel >= 0.74
BuildRequires:	docbook-dtd41-sgml
BuildRequires:	docbook-utils
BuildRequires:	fontconfig-devel
BuildRequires:	gettext-tools >= 0.19.7
BuildRequires:	glib2-devel >= 1:2.32.0
BuildRequires:	gnome-common
BuildRequires:	gtk+3-devel >= 3.15.3
BuildRequires:	gtk-doc >= 1.9
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libcanberra-devel >= 0.10
BuildRequires:	libcanberra-gtk3-devel >= 0.10
BuildRequires:	libnotify-devel >= 0.7.0
BuildRequires:	libtool >= 2:2
BuildRequires:	libxslt-progs
BuildRequires:	pkgconfig
BuildRequires:	polkit-devel
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
Requires(post,preun):	glib2 >= 1:2.32.0
Requires:	PackageKit >= 0.9.1
Requires:	glib2 >= 1:2.32.0
Requires:	gtk+3 >= 3.15.3
Requires:	polkit-gnome >= 0.92
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides session applications for the PackageKit API.
There are several utilities designed for installing, updating and
removing packages.

%description -l pl.UTF-8
Ten pakiet dostarcza aplikacje sesji dla API PackageKit. Zawiera kilka
narzędzi stworzonych do instalacji, aktualizacji i usuwania pakietów.

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
%attr(755,root,root) %{_bindir}/gpk-log
%attr(755,root,root) %{_bindir}/gpk-prefs
%attr(755,root,root) %{_bindir}/gpk-update-viewer
%{_datadir}/GConf/gsettings/org.gnome.packagekit.gschema.migrate
%{_datadir}/glib-2.0/schemas/org.gnome.packagekit.gschema.xml
%{_datadir}/gnome-packagekit
%{_datadir}/metainfo/org.gnome.PackageUpdater.appdata.xml
%{_datadir}/metainfo/org.gnome.Packages.appdata.xml
%{_iconsdir}/hicolor/*x*/apps/gpk-*.png
# terminating "*" is a workaround for rpm glob failing to glob dirs with symlinks dead at build time
%{_iconsdir}/hicolor/*x*/mimetypes/application-x-catalog.png*
%{_iconsdir}/hicolor/*x*/mimetypes/application-x-package-list.png*
%{_iconsdir}/hicolor/scalable/apps/gpk-*.svg
%{_iconsdir}/hicolor/scalable/mimetypes/application-x-catalog.svg
%{_iconsdir}/hicolor/scalable/mimetypes/application-x-package-list.svg
%{_desktopdir}/gpk-install-local-file.desktop
%{_desktopdir}/gpk-log.desktop
%{_desktopdir}/gpk-prefs.desktop
%{_desktopdir}/org.gnome.PackageUpdater.desktop
%{_desktopdir}/org.gnome.Packages.desktop
%{_mandir}/man1/gpk-application.1*
%{_mandir}/man1/gpk-log.1*
%{_mandir}/man1/gpk-prefs.1*
%{_mandir}/man1/gpk-update-viewer.1*
