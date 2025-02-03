# TODO: introspection, vapi, capi_docs (there are some meson issues with fake library stubs)
Summary:	Sandboxed and extendable image rendering
Summary(pl.UTF-8):	Rozszerzalne renderowanie obrazów w piaskownicy
Name:		glycin
Version:	1.1.4
Release:	0.1
License:	MPL v2.0 or LGPL v2.1+
Group:		Libraries
Source0:	https://download.gnome.org/sources/glycin/1.1/%{name}-%{version}.tar.xz
# Source0-md5:	4faccd31dbe4c2b223784ef20918fb74
URL:		https://gitlab.gnome.org/sophie-h/glycin
BuildRequires:	cairo-devel >= 1.17.0
BuildRequires:	cargo
BuildRequires:	glib2-devel >= 1:2.60
BuildRequires:	gdk-pixbuf2-devel >= 2.0
BuildRequires:	gtk4-devel >= 4.12.0
BuildRequires:	lcms2-devel >= 2.14
BuildRequires:	libheif-devel >= 1.14.2
BuildRequires:	libjxl-devel >= 0.8.2
BuildRequires:	libseccomp-devel >= 2.5.0
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	meson >= 1.2
BuildRequires:	ninja >= 1.5
BuildRequires:	pango-devel
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 2.038
BuildRequires:	rust >= 1.77
Requires:	glib2 >= 1:2.60
Requires:	lcms2 >= 2.14
Requires:	libseccomp >= 2.5.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_debugsource_packages	0

%description
Glycin allows to decode images into gdk::Textures and to extract image
metadata. The decoding happens in sandboxed modular image loaders.

%description -l pl.UTF-8
Glycin pozwala dekodować obrazy do obiektów gdk::Texture oraz
wydobywać metadane z obrazów. Dekodowanie dzieje się w modułach
wczytujących działających w piaskownicy.

%package devel
Summary:	Header file for glycin library
Summary(pl.UTF-8):	Plik nagłówkowy biblioteki glycin
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 1:2.60
Requires:	lcms2-devel >= 2.14
Requires:	libseccomp-devel >= 2.5.0

%description devel
Header file for glycin library.

%description devel -l pl.UTF-8
Plik nagłówkowy biblioteki glycin.

%package static
Summary:	Static glycin library
Summary(pl.UTF-8):	Statyczna biblioteka glycin
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static glycin library.

%description static -l pl.UTF-8
Statyczna biblioteka glycin.

%package gtk4
Summary:	Sandboxed and extendable image decoding for GTK 4
Summary(pl.UTF-8):	Rozszerzalne renderowanie obrazów w piaskownicy dla GTK 4
Group:		Libraries
Requires:	gtk4 >= 4.12.0

%description gtk4
Sandboxed and extendable image decoding for GTK 4.

%description gtk4 -l pl.UTF-8
Rozszerzalne renderowanie obrazów w piaskownicy dla GTK 4.

%package gtk4-devel
Summary:	Header file for glycin-gtk4 library
Summary(pl.UTF-8):	Plik nagłówkowy biblioteki glycin-gtk4
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-gtk4 = %{version}-%{release}
Requires:	gtk4-devel >= 4.12.0

%description gtk4-devel
Header file for glycin-gtk4 library.

%description gtk4-devel -l pl.UTF-8
Plik nagłówkowy biblioteki glycin-gtk4.

%package gtk4-static
Summary:	Static glycin-gtk4 library
Summary(pl.UTF-8):	Statyczna biblioteka glycin-gtk4
Group:		Development/Libraries
Requires:	%{name}-gtk4-devel = %{version}-%{release}

%description gtk4-static
Static glycin-gtk4 library.

%description gtk4-static -l pl.UTF-8
Statyczna biblioteka glycin-gtk4.

%package loaders
Summary:	Sandboxed image rendering
Summary(pl.UTF-8):	Renderowanie obrazów w piaskownicy
Group:		Applications/Graphics
Requires:	cairo >= 1.17.0
Requires:	gtk4 >= 4.12.0
Requires:	libheif >= 1.14.2
Requires:	libjxl >= 0.8.2

%description loaders
Glycin allows to decode images into gdk::Textures and to extract image
metadata. The decoding happens in sandboxed modular image loaders.

%description loaders -l pl.UTF-8
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
%meson build \
	-Dintrospection=false \
	-Dvapi=false

%meson_build

%install
rm -rf $RPM_BUILD_ROOT

%ifarch x32
export PKG_CONFIG_ALLOW_CROSS=1
%endif
%meson_install

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	gtk4 -p /sbin/ldconfig
%postun	gtk4 -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc NEWS LICENSE README.md
%attr(755,root,root) %{_libdir}/libglycin-1.so.0

%files devel
%defattr(644,root,root,755)
%{_libdir}/libglycin-1.so
%{_includedir}/glycin-1
%{_pkgconfigdir}/glycin-1.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libglycin-1.a

%files gtk4
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libglycin-gtk4-1.so.0
%{_pkgconfigdir}/glycin-gtk4-1.pc

%files gtk4-devel
%defattr(644,root,root,755)
%{_libdir}/libglycin-gtk4-1.so
%{_includedir}/glycin-gtk4-1

%files gtk4-static
%defattr(644,root,root,755)
%{_libdir}/libglycin-gtk4-1.a

%files loaders
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
