Summary:	GNOME PackageKit Client
Name:		gnome-packagekit
Version:	0.1.9
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://people.freedesktop.org/~hughsient/releases/%{name}-%{version}.tar.gz
# Source0-md5:	531969d7299aeb1c9a19453481541c60
URL:		http://www.packagekit.org/
BuildRequires:	GConf2-devel
BuildRequires:	PackageKit-devel >= 0.1.8
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	dbus-devel >= 1.1.4
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
Requires(post,preun):	GConf2
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

%preun
%gconf_schema_uninstall gnome-packagekit.schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog COPYING NEWS README
%attr(755,root,root) %{_bindir}/pk-application
%attr(755,root,root) %{_bindir}/pk-backend-status
%attr(755,root,root) %{_bindir}/pk-install-file
%attr(755,root,root) %{_bindir}/pk-install-package
%attr(755,root,root) %{_bindir}/pk-prefs
%attr(755,root,root) %{_bindir}/pk-repo
%attr(755,root,root) %{_bindir}/pk-transaction-viewer
%attr(755,root,root) %{_bindir}/pk-update-icon
%attr(755,root,root) %{_bindir}/pk-update-viewer
%{_datadir}/gnome-packagekit
%{_sysconfdir}/gconf/schemas/gnome-packagekit.schemas
%{_datadir}/gnome/autostart/pk-update-icon.desktop
%{_desktopdir}/pk-application.desktop
%{_desktopdir}/pk-install-file.desktop
%{_desktopdir}/pk-prefs.desktop
%{_desktopdir}/pk-repo.desktop
%{_desktopdir}/pk-transaction-viewer.desktop
%{_desktopdir}/pk-update-viewer.desktop
