Summary:	Sandboxed image rendering
Summary(pl.UTF-8):	Renderowanie obrazów w piaskownicy
Name:		glycin-loaders
Version:	1.0.1
Release:	1
License:	MPL v2.0 or LGPL v2.1+
Group:		Applications
Source0:	https://download.gnome.org/sources/glycin-loaders/1.0/%{name}-%{version}.tar.xz
# Source0-md5:	b4d7ad77a91f498385d21e16df81dea9
URL:		https://gitlab.gnome.org/sophie-h/glycin
BuildRequires:	cairo-devel >= 1.17.0
BuildRequires:	cargo
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	gdk-pixbuf2-devel >= 2.0
BuildRequires:	gtk4-devel >= 4.12.0
BuildRequires:	libheif-devel >= 1.14.2
BuildRequires:	libjxl-devel >= 0.8.2
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	meson >= 0.57
BuildRequires:	ninja >= 1.5
BuildRequires:	pango-devel
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	rust >= 1.75
Requires:	cairo >= 1.17.0
Requires:	gtk4 >= 4.12.0
Requires:	libheif >= 1.14.2
Requires:	libjxl >= 0.8.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_debugsource_packages	0

%description
Glycin allows to decode images into gdk::Textures and to extract image
metadata. The decoding happens in sandboxed modular image loaders.

%description -l pl.UTF-8
Glycin pozwala dekodować obrazy do obiektów gdk::Texture oraz
wydobywać metadane z obrazów. Dekodowanie dzieje się w modułach
wczytujących działających w piaskownicy.

%prep
%setup -q

%ifarch x32
%{__sed} -i -e "/^cargo_options/ a '--target', 'x86_64-unknown-linux-gnux32'," \
	-e "s,/ rust_target /,/ 'x86_64-unknown-linux-gnux32' / rust_target /," loaders/meson.build
%endif

%build
%ifarch x32
export PKG_CONFIG_ALLOW_CROSS=1
%endif
%meson build

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ifarch x32
export PKG_CONFIG_ALLOW_CROSS=1
%endif
%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS LICENSE README.md
%dir %{_libexecdir}/glycin-loaders
%dir %{_libexecdir}/glycin-loaders/1+
%attr(755,root,root) %{_libexecdir}/glycin-loaders/1+/glycin-heif
%attr(755,root,root) %{_libexecdir}/glycin-loaders/1+/glycin-image-rs
%attr(755,root,root) %{_libexecdir}/glycin-loaders/1+/glycin-jxl
%attr(755,root,root) %{_libexecdir}/glycin-loaders/1+/glycin-svg
%dir %{_datadir}/glycin-loaders
%dir %{_datadir}/glycin-loaders/1+
%dir %{_datadir}/glycin-loaders/1+/conf.d
%{_datadir}/glycin-loaders/1+/conf.d/glycin-heif.conf
%{_datadir}/glycin-loaders/1+/conf.d/glycin-image-rs.conf
%{_datadir}/glycin-loaders/1+/conf.d/glycin-jxl.conf
%{_datadir}/glycin-loaders/1+/conf.d/glycin-svg.conf
