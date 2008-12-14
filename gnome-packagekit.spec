Summary:	GNOME PackageKit Client
Name:		gnome-packagekit
Version:	0.3.12
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://www.packagekit.org/releases/%{name}-%{version}.tar.gz
# Source0-md5:	97545c284c74c974ee0a259af9eaf461
URL:		http://www.packagekit.org/
BuildRequires:	GConf2-devel
BuildRequires:	PackageKit-devel >= 0.3.4
BuildRequires:	PolicyKit-gnome-devel >= 0.8
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	dbus-devel >= 1.2.0
BuildRequires:	dbus-glib-devel >= 0.74
BuildRequires:	gettext-devel
BuildRequires:	gnome-doc-utils
BuildRequires:	gtk+2-devel >= 2:2.12.8
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libglade2-devel >= 1:2.6.2
BuildRequires:	libnotify-devel >= 0.4.4
BuildRequires:	libsexy-devel >= 0.1.11
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	unique-devel >= 0.9.4
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk+2
Requires(post,preun):	GConf2
Requires:	PackageKit >= 0.3.1
Requires:	PolicyKit-gnome >= 0.8
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides session applications for the PackageKit API.
There are several utilities designed for installing, updating and
removing packages.

%prep
%setup -q

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-scrollkeeper \
	--disable-schemas-install

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome --with-omf

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install gnome-packagekit.schemas
%update_icon_cache hicolor
%update_desktop_database

%preun
%gconf_schema_uninstall gnome-packagekit.schemas

%postun
%update_icon_cache hicolor
%update_desktop_database_postun

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog COPYING NEWS README
%attr(755,root,root) %{_bindir}/gpk-application
%attr(755,root,root) %{_bindir}/gpk-backend-status
%attr(755,root,root) %{_bindir}/gpk-install-catalog
%attr(755,root,root) %{_bindir}/gpk-install-local-file
%attr(755,root,root) %{_bindir}/gpk-install-mime-type
%attr(755,root,root) %{_bindir}/gpk-install-package-name
%attr(755,root,root) %{_bindir}/gpk-install-provide-file
%attr(755,root,root) %{_bindir}/gpk-log
%attr(755,root,root) %{_bindir}/gpk-prefs
%attr(755,root,root) %{_bindir}/gpk-repo
%attr(755,root,root) %{_bindir}/gpk-update-icon
%attr(755,root,root) %{_bindir}/gpk-update-viewer
%{_datadir}/gnome-packagekit
%{_sysconfdir}/gconf/schemas/gnome-packagekit.schemas
%{_datadir}/gnome/autostart/gpk-update-icon.desktop
%{_iconsdir}/hicolor/*/*/*
%{_desktopdir}/gpk-application.desktop
%{_desktopdir}/gpk-install-catalog.desktop
%{_desktopdir}/gpk-install-file.desktop
%{_desktopdir}/gpk-log.desktop
%{_desktopdir}/gpk-prefs.desktop
%{_desktopdir}/gpk-repo.desktop
%{_desktopdir}/gpk-update-viewer.desktop
%{_mandir}/man1/gpk-install-local-file.1*
%{_mandir}/man1/gpk-install-mime-type.1*
%{_mandir}/man1/gpk-install-package-name.1*
%{_mandir}/man1/gpk-install-provide-file.1*
%{_mandir}/man1/gpk-prefs.1*
%{_mandir}/man1/gpk-repo.1*
%{_mandir}/man1/gpk-update-icon.1*
%{_mandir}/man1/gpk-update-viewer.1*
