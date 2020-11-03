#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : tokyocabinet
Version  : 1.4.48
Release  : 8
URL      : http://fallabs.com/tokyocabinet/tokyocabinet-1.4.48.tar.gz
Source0  : http://fallabs.com/tokyocabinet/tokyocabinet-1.4.48.tar.gz
Summary  : a modern implementation of DBM
Group    : Development/Tools
License  : LGPL-2.1
Requires: tokyocabinet-bin = %{version}-%{release}
Requires: tokyocabinet-data = %{version}-%{release}
Requires: tokyocabinet-lib = %{version}-%{release}
Requires: tokyocabinet-libexec = %{version}-%{release}
Requires: tokyocabinet-license = %{version}-%{release}
Requires: tokyocabinet-man = %{version}-%{release}
BuildRequires : bzip2-dev
BuildRequires : pkgconfig(zlib)

%description
================================================================
Tokyo Cabinet: a modern implementation of DBM
================================================================

%package bin
Summary: bin components for the tokyocabinet package.
Group: Binaries
Requires: tokyocabinet-data = %{version}-%{release}
Requires: tokyocabinet-libexec = %{version}-%{release}
Requires: tokyocabinet-license = %{version}-%{release}

%description bin
bin components for the tokyocabinet package.


%package data
Summary: data components for the tokyocabinet package.
Group: Data

%description data
data components for the tokyocabinet package.


%package dev
Summary: dev components for the tokyocabinet package.
Group: Development
Requires: tokyocabinet-lib = %{version}-%{release}
Requires: tokyocabinet-bin = %{version}-%{release}
Requires: tokyocabinet-data = %{version}-%{release}
Provides: tokyocabinet-devel = %{version}-%{release}
Requires: tokyocabinet = %{version}-%{release}

%description dev
dev components for the tokyocabinet package.


%package lib
Summary: lib components for the tokyocabinet package.
Group: Libraries
Requires: tokyocabinet-data = %{version}-%{release}
Requires: tokyocabinet-libexec = %{version}-%{release}
Requires: tokyocabinet-license = %{version}-%{release}

%description lib
lib components for the tokyocabinet package.


%package libexec
Summary: libexec components for the tokyocabinet package.
Group: Default
Requires: tokyocabinet-license = %{version}-%{release}

%description libexec
libexec components for the tokyocabinet package.


%package license
Summary: license components for the tokyocabinet package.
Group: Default

%description license
license components for the tokyocabinet package.


%package man
Summary: man components for the tokyocabinet package.
Group: Default

%description man
man components for the tokyocabinet package.


%prep
%setup -q -n tokyocabinet-1.4.48
cd %{_builddir}/tokyocabinet-1.4.48

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1604442925
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%configure --disable-static
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1604442925
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/tokyocabinet
cp %{_builddir}/tokyocabinet-1.4.48/COPYING %{buildroot}/usr/share/package-licenses/tokyocabinet/e60c2e780886f95df9c9ee36992b8edabec00bcc
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/tcamgr
/usr/bin/tcamttest
/usr/bin/tcatest
/usr/bin/tcbmgr
/usr/bin/tcbmttest
/usr/bin/tcbtest
/usr/bin/tcfmgr
/usr/bin/tcfmttest
/usr/bin/tcftest
/usr/bin/tchmgr
/usr/bin/tchmttest
/usr/bin/tchtest
/usr/bin/tctmgr
/usr/bin/tctmttest
/usr/bin/tcttest
/usr/bin/tcucodec
/usr/bin/tcumttest
/usr/bin/tcutest

%files data
%defattr(-,root,root,-)
/usr/share/tokyocabinet/COPYING
/usr/share/tokyocabinet/ChangeLog
/usr/share/tokyocabinet/doc/benchmark.pdf
/usr/share/tokyocabinet/doc/common.css
/usr/share/tokyocabinet/doc/icon16.png
/usr/share/tokyocabinet/doc/index.html
/usr/share/tokyocabinet/doc/index.ja.html
/usr/share/tokyocabinet/doc/logo-ja.png
/usr/share/tokyocabinet/doc/logo.png
/usr/share/tokyocabinet/doc/spex-en.html
/usr/share/tokyocabinet/doc/spex-ja.html
/usr/share/tokyocabinet/doc/tokyoproducts.pdf
/usr/share/tokyocabinet/doc/tokyoproducts.ppt
/usr/share/tokyocabinet/tokyocabinet.idl

%files dev
%defattr(-,root,root,-)
/usr/include/tcadb.h
/usr/include/tcbdb.h
/usr/include/tcfdb.h
/usr/include/tchdb.h
/usr/include/tctdb.h
/usr/include/tcutil.h
/usr/lib64/libtokyocabinet.so
/usr/lib64/pkgconfig/tokyocabinet.pc
/usr/share/man/man3/tcadb.3
/usr/share/man/man3/tcbdb.3
/usr/share/man/man3/tcfdb.3
/usr/share/man/man3/tchdb.3
/usr/share/man/man3/tclist.3
/usr/share/man/man3/tcmap.3
/usr/share/man/man3/tcmdb.3
/usr/share/man/man3/tcmpool.3
/usr/share/man/man3/tctdb.3
/usr/share/man/man3/tctree.3
/usr/share/man/man3/tcutil.3
/usr/share/man/man3/tcxstr.3
/usr/share/man/man3/tokyocabinet.3

%files lib
%defattr(-,root,root,-)
/usr/lib64/libtokyocabinet.so.9
/usr/lib64/libtokyocabinet.so.9.11.0

%files libexec
%defattr(-,root,root,-)
/usr/libexec/tcawmgr.cgi

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/tokyocabinet/e60c2e780886f95df9c9ee36992b8edabec00bcc

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/tcamgr.1
/usr/share/man/man1/tcamttest.1
/usr/share/man/man1/tcatest.1
/usr/share/man/man1/tcbmgr.1
/usr/share/man/man1/tcbmttest.1
/usr/share/man/man1/tcbtest.1
/usr/share/man/man1/tcfmgr.1
/usr/share/man/man1/tcfmttest.1
/usr/share/man/man1/tcftest.1
/usr/share/man/man1/tchmgr.1
/usr/share/man/man1/tchmttest.1
/usr/share/man/man1/tchtest.1
/usr/share/man/man1/tctmgr.1
/usr/share/man/man1/tctmttest.1
/usr/share/man/man1/tcttest.1
/usr/share/man/man1/tcucodec.1
/usr/share/man/man1/tcumttest.1
/usr/share/man/man1/tcutest.1
