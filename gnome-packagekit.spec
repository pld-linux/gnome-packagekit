# TODO: is polkit-gnome still required?
#
# Conditional build:
%bcond_without	systemd	# rely on systemd for session tracking instead of ConsoleKit
#
Summary:	GNOME PackageKit Client
Summary(pl.UTF-8):	Klient PackageKit dla GNOME
Name:		gnome-packagekit
Version:	43.0
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	https://download.gnome.org/sources/gnome-packagekit/43/%{name}-%{version}.tar.xz
# Source0-md5:	cc7fa625c449df6f75bda2abab95ea0d
Patch0:		systemd-fallback.patch
URL:		https://gitlab.gnome.org/GNOME/gnome-packagekit
BuildRequires:	AppStream
BuildRequires:	PackageKit-devel >= 0.9.1
BuildRequires:	dbus-devel >= 1.2.0
BuildRequires:	dbus-glib-devel >= 0.74
BuildRequires:	docbook-dtd41-sgml
BuildRequires:	docbook-utils
BuildRequires:	gettext-tools >= 0.19.7
BuildRequires:	glib2-devel >= 1:2.56.0
BuildRequires:	gtk+3-devel >= 3.24
BuildRequires:	libxslt-progs
BuildRequires:	meson >= 0.46.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	polkit-devel
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 2.042
%{?with_systemd:BuildRequires:  systemd-devel}
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xz
BuildRequires:	yelp-tools
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Requires(post,preun):	glib2 >= 1:2.56.0
Requires:	PackageKit >= 0.9.1
Requires:	glib2 >= 1:2.56.0
Requires:	gtk+3 >= 3.24
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
%patch -P0 -p1 -b .orig

%build
%meson \
	%{!?with_systemd:-Dsystemd=false}

%meson_build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

%py_postclean

%find_lang %{name} --with-gnome

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
%doc AUTHORS COMMITMENT MAINTAINERS README.md
%attr(755,root,root) %{_bindir}/gpk-application
%attr(755,root,root) %{_bindir}/gpk-log
%attr(755,root,root) %{_bindir}/gpk-prefs
%attr(755,root,root) %{_bindir}/gpk-update-viewer
%{_datadir}/GConf/gsettings/org.gnome.packagekit.gschema.migrate
%{_datadir}/glib-2.0/schemas/org.gnome.packagekit.gschema.xml
%{_datadir}/gnome-packagekit
%{_datadir}/metainfo/org.gnome.PackageUpdater.metainfo.xml
%{_datadir}/metainfo/org.gnome.Packages.metainfo.xml
%{_desktopdir}/gpk-log.desktop
%{_desktopdir}/gpk-prefs.desktop
%{_desktopdir}/org.gnome.PackageUpdater.desktop
%{_desktopdir}/org.gnome.Packages.desktop
%{_iconsdir}/hicolor/scalable/apps/gpk-*.svg
%{_iconsdir}/hicolor/scalable/mimetypes/application-x-catalog.svg
%{_iconsdir}/hicolor/scalable/mimetypes/application-x-package-list.svg
%{_mandir}/man1/gpk-application.1*
%{_mandir}/man1/gpk-log.1*
%{_mandir}/man1/gpk-prefs.1*
%{_mandir}/man1/gpk-update-viewer.1*
