# see m4/${libname}.m4 />= for required version of particular library
%define		libbfio_ver		20201125
%define		libcdata_ver		20220115
%define		libcerror_ver		20120425
%define		libcfile_ver		20160409
%define		libclocale_ver		20120425
%define		libcnotify_ver		20120425
%define		libcpath_ver		20180716
%define		libcsplit_ver		20120701
%define		libcthreads_ver		20160404
%define		libfcache_ver		20191109
%define		libfdata_ver		20201129
%define		libfvalue_ver		20200711
%define		libuna_ver		20210801
Summary:	Python 2 bindings for libvslvm library
Summary(pl.UTF-8):	Wiązania Pythona 2 do biblioteki libvslvm
Name:		python-pyvslvm
Version:	20221025
Release:	1
License:	LGPL v3+
Group:		Libraries/Python
#Source0Download: https://github.com/libyal/libvslvm/releases
Source0:	https://github.com/libyal/libvslvm/releases/download/%{version}/libvslvm-experimental-%{version}.tar.gz
# Source0-md5:	d57ca4f0c1c5dff437c29e73f28ca289
URL:		https://github.com/libyal/libvslvm/
BuildRequires:	autoconf >= 2.71
BuildRequires:	automake >= 1.6
BuildRequires:	gettext-tools >= 0.21
BuildRequires:	libbfio-devel >= %{libbfio_ver}
BuildRequires:	libcdata-devel >= %{libcdata_ver}
BuildRequires:	libcerror-devel >= %{libcerror_ver}
BuildRequires:	libcfile-devel >= %{libcfile_ver}
BuildRequires:	libclocale-devel >= %{libclocale_ver}
BuildRequires:	libcnotify-devel >= %{libcnotify_ver}
BuildRequires:	libcpath-devel >= %{libcpath_ver}
BuildRequires:	libcsplit-devel >= %{libcsplit_ver}
BuildRequires:	libcthreads-devel >= %{libcthreads_ver}
BuildRequires:	libfcache-devel >= %{libfcache_ver}
BuildRequires:	libfdata-devel >= %{libfdata_ver}
BuildRequires:	libfvalue-devel >= %{libfvalue_ver}
BuildRequires:	libfuse-devel >= 2.6
BuildRequires:	libuna-devel >= %{libuna_ver}
BuildRequires:	libtool >= 2:2
%{?with_python2:BuildRequires:	python-devel >= 1:2.5}
%{?with_python3:BuildRequires:	python3-devel >= 1:3.2}
Requires:	libbfio >= %{libbfio_ver}
Requires:	libcerror >= %{libcerror_ver}
Requires:	libvslvm >= %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python 2 bindings for libvslvm library.

%description -l pl.UTF-8
Wiązania Pythona 2 do biblioteki libvslvm.

%prep
%setup -q -n libvslvm-%{version}

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-python2 \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# keep only python2 module
%{__rm} $RPM_BUILD_ROOT%{_bindir}/vslvm*
%{__rm} -r $RPM_BUILD_ROOT%{_includedir}/libvslvm*
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libvslvm.*
%{__rm} $RPM_BUILD_ROOT%{_pkgconfigdir}/libvslvm.pc
%{__rm} -r $RPM_BUILD_ROOT%{_mandir}/man[13]

%{__rm} $RPM_BUILD_ROOT%{py_sitedir}/pyvslvm.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{py_sitedir}/pyvslvm.so
