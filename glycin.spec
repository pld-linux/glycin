#
# Conditional build:
%bcond_without	apidocs	 # API documentation

Summary:	Sandboxed and extendable image rendering
Summary(pl.UTF-8):	Rozszerzalne renderowanie obrazów w piaskownicy
Name:		glycin
Version:	2.0.0
Release:	1
License:	MPL v2.0 or LGPL v2.1+
Group:		Libraries
Source0:	https://download.gnome.org/sources/glycin/2.0/%{name}-%{version}.tar.xz
# Source0-md5:	f25308bac987c808b85d99dd582ca91f
# cargo vendor-filterer --platform='*-unknown-linux-*' --tier=2
Source1:	%{name}-%{version}-vendor.tar.xz
# Source1-md5:	da6b5ef1b59bc8067ede802d26cef4b4
URL:		https://gitlab.gnome.org/GNOME/glycin
BuildRequires:	cairo-devel >= 1.17.0
BuildRequires:	cargo
BuildRequires:	fontconfig-devel >= 1:2.13.0
%{?with_apidocs:BuildRequires:	gi-docgen}
BuildRequires:	glib2-devel >= 1:2.60
BuildRequires:	gobject-introspection-devel
BuildRequires:	gtk4-devel >= 4.16.0
BuildRequires:	lcms2-devel >= 2.14
BuildRequires:	libheif-devel >= 1.17.0
BuildRequires:	libjxl-devel >= 0.11.0
BuildRequires:	librsvg-devel >= 2.52.0
BuildRequires:	libseccomp-devel >= 2.5.0
BuildRequires:	meson >= 1.2
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 2.042
BuildRequires:	rust >= 1.85
BuildRequires:	tar >= 1:1.22
BuildRequires:	vala
BuildRequires:	xz
Requires:	fontconfig-libs >= 1:2.13.0
Requires:	glib2 >= 1:2.60
Requires:	lcms2 >= 2.14
Requires:	libseccomp >= 2.5.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

%package -n vala-glycin
Summary:	Vala API for glycin library
Summary(pl.UTF-8):	API języka Vala do biblioteki glycin
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	vala
BuildArch:	noarch

%description -n vala-glycin
Vala API for glycin library.

%description -n vala-glycin -l pl.UTF-8
API języka Vala do biblioteki glycin.

%package apidocs
Summary:	API documentation for glycin library
Summary(pl.UTF-8):	Dokumentacja API biblioteki glycin
Group:		Documentation
BuildArch:	noarch

%description apidocs
API documentation for glycin library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki glycin.

%package gtk4
Summary:	Sandboxed and extendable image decoding for GTK 4
Summary(pl.UTF-8):	Rozszerzalne renderowanie obrazów w piaskownicy dla GTK 4
Group:		Libraries
Requires:	gtk4 >= 4.16.0

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
Requires:	gtk4-devel >= 4.16.0

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

%package -n vala-glycin-gtk4
Summary:	Vala API for glycin-gtk4 library
Summary(pl.UTF-8):	API języka Vala do biblioteki glycin-gtk4
Group:		Development/Libraries
Requires:	%{name}-gtk4-devel = %{version}-%{release}
Requires:	vala-glycin = %{version}-%{release}
BuildArch:	noarch

%description -n vala-glycin-gtk4
Vala API for glycin library.

%description -n vala-glycin-gtk4 -l pl.UTF-8
API języka Vala do biblioteki glycin.

%package gtk4-apidocs
Summary:	API documentation for glycin-gtk4 library
Summary(pl.UTF-8):	Dokumentacja API biblioteki glycin-gtk4
Group:		Documentation
BuildArch:	noarch

%description gtk4-apidocs
API documentation for glycin-gtk4 library.

%description gtk4-apidocs -l pl.UTF-8
Dokumentacja API biblioteki glycin-gtk4.

%package loaders
Summary:	Sandboxed image rendering
Summary(pl.UTF-8):	Renderowanie obrazów w piaskownicy
Group:		Applications/Graphics
Requires:	cairo >= 1.17.0
Requires:	gtk4 >= 4.12.0
Requires:	libheif >= 1.17.0
Requires:	libjxl >= 0.11.0
Requires:	librsvg >= 2.52.0

%description loaders
Glycin allows to decode images into gdk::Textures and to extract image
metadata. The decoding happens in sandboxed modular image loaders.

%description loaders -l pl.UTF-8
Glycin pozwala dekodować obrazy do obiektów gdk::Texture oraz
wydobywać metadane z obrazów. Dekodowanie dzieje się w modułach
wczytujących działających w piaskownicy.

%package thumbnailer
Summary:	Thumbnailer based on glycin-loaders
Summary(pl.UTF-8):	Program do miniaturek obrazków oparty na glycin-loaders
Group:		Applications/Graphics
Requires:	%{name}-loaders = %{version}-%{release}

%description thumbnailer
Thumbnailer based on glycin-loaders.

%description thumbnailer -l pl.UTF-8
Program do miniaturek obrazków oparty na glycin-loaders.

%prep
%setup -q -a1

%{__sed} -i -e "/^cargo_options/ a '--verbose', '--target', '%{rust_target}'," \
	-e "s,/ rust_target /,/ '%rust_target' / rust_target /," glycin-loaders/meson.build libglycin/meson.build

%{__sed} -i -e "/'build',/ a '--verbose', '--target', '%{rust_target}'," \
	-e "s,/ rust_target /,/ '%rust_target' / rust_target /," glycin-thumbnailer/meson.build

# use our offline registry
export CARGO_HOME="$(pwd)/.cargo"

mkdir -p "$CARGO_HOME"
cat >.cargo/config.toml <<EOF
[source.crates-io]
replace-with = 'vendored-sources'

[source.vendored-sources]
directory = '$PWD/vendor'
EOF

%build
export CARGO_HOME="$(pwd)/.cargo"
export PKG_CONFIG_ALLOW_CROSS=1
export RUSTFLAGS="%{rpmrustflags}"
%meson \
	%{?with_apidocs:-Dcapi_docs=true} \
	-Dloaders=glycin-heif,glycin-image-rs,glycin-jpeg2000,glycin-jxl,glycin-raw,glycin-svg

# There are some strange hacks with empty stub libraries for meson overwritten by rust libs.
# Because of some mistaken dependency processing gir build fails after linking to empty stubs
# instead of real libraries...
# Workaround: ensure libs are overwritten by rust copies before further processing for gir.
#meson_build libglycin/libglycin-copy-library

#meson_build libglycin/libglycin-gtk4-copy-library

%meson_build

%install
rm -rf $RPM_BUILD_ROOT

export CARGO_HOME="$(pwd)/.cargo"
export PKG_CONFIG_ALLOW_CROSS=1
%meson_install

%if %{with apidocs}
install -d $RPM_BUILD_ROOT%{_gidocdir}
%{__mv} $RPM_BUILD_ROOT%{_docdir}/libglycin*-2 $RPM_BUILD_ROOT%{_gidocdir}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	gtk4 -p /sbin/ldconfig
%postun	gtk4 -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc NEWS LICENSE README.md
%attr(755,root,root) %{_libdir}/libglycin-2.so.0
%{_libdir}/girepository-1.0/Gly-2.typelib

%files devel
%defattr(644,root,root,755)
%{_libdir}/libglycin-2.so
%{_includedir}/glycin-2
%{_datadir}/gir-1.0/Gly-2.gir
%{_pkgconfigdir}/glycin-2.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libglycin-2.a

%files -n vala-glycin
%defattr(644,root,root,755)
%{_datadir}/vala/vapi/glycin-2.deps
%{_datadir}/vala/vapi/glycin-2.vapi

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_gidocdir}/libglycin-2
%endif

%files gtk4
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libglycin-gtk4-2.so.0
%{_libdir}/girepository-1.0/GlyGtk4-2.typelib

%files gtk4-devel
%defattr(644,root,root,755)
%{_libdir}/libglycin-gtk4-2.so
%{_includedir}/glycin-gtk4-2
%{_datadir}/gir-1.0/GlyGtk4-2.gir
%{_pkgconfigdir}/glycin-gtk4-2.pc

%files gtk4-static
%defattr(644,root,root,755)
%{_libdir}/libglycin-gtk4-2.a

%files -n vala-glycin-gtk4
%defattr(644,root,root,755)
%{_datadir}/vala/vapi/glycin-gtk4-2.deps
%{_datadir}/vala/vapi/glycin-gtk4-2.vapi

%if %{with apidocs}
%files gtk4-apidocs
%defattr(644,root,root,755)
%{_gidocdir}/libglycin-gtk4-2
%endif

%files loaders
%defattr(644,root,root,755)
%doc NEWS LICENSE README.md
%dir %{_libexecdir}/glycin-loaders
%dir %{_libexecdir}/glycin-loaders/2+
%attr(755,root,root) %{_libexecdir}/glycin-loaders/2+/glycin-heif
%attr(755,root,root) %{_libexecdir}/glycin-loaders/2+/glycin-image-rs
%attr(755,root,root) %{_libexecdir}/glycin-loaders/2+/glycin-jpeg2000
%attr(755,root,root) %{_libexecdir}/glycin-loaders/2+/glycin-jxl
%attr(755,root,root) %{_libexecdir}/glycin-loaders/2+/glycin-raw
%attr(755,root,root) %{_libexecdir}/glycin-loaders/2+/glycin-svg
%dir %{_datadir}/glycin-loaders
%dir %{_datadir}/glycin-loaders/2+
%dir %{_datadir}/glycin-loaders/2+/conf.d
%{_datadir}/glycin-loaders/2+/conf.d/glycin-heif.conf
%{_datadir}/glycin-loaders/2+/conf.d/glycin-image-rs.conf
%{_datadir}/glycin-loaders/2+/conf.d/glycin-jpeg2000.conf
%{_datadir}/glycin-loaders/2+/conf.d/glycin-jxl.conf
%{_datadir}/glycin-loaders/2+/conf.d/glycin-raw.conf
%{_datadir}/glycin-loaders/2+/conf.d/glycin-svg.conf

%files thumbnailer
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/glycin-thumbnailer
%{_datadir}/thumbnailers/glycin-heif.thumbnailer
%{_datadir}/thumbnailers/glycin-image-rs.thumbnailer
%{_datadir}/thumbnailers/glycin-jpeg2000.thumbnailer
%{_datadir}/thumbnailers/glycin-jxl.thumbnailer
%{_datadir}/thumbnailers/glycin-raw.thumbnailer
%{_datadir}/thumbnailers/glycin-svg.thumbnailer
