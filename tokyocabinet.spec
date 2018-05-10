#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : tokyocabinet
Version  : 1.4.48
Release  : 4
URL      : http://fallabs.com/tokyocabinet/tokyocabinet-1.4.48.tar.gz
Source0  : http://fallabs.com/tokyocabinet/tokyocabinet-1.4.48.tar.gz
Summary  : a modern implementation of DBM
Group    : Development/Tools
License  : LGPL-2.1
Requires: tokyocabinet-bin
Requires: tokyocabinet-lib
Requires: tokyocabinet-doc
Requires: tokyocabinet-data
BuildRequires : bzip2-dev
BuildRequires : pkgconfig(zlib)
BuildRequires : zlib-dev

%description
================================================================
Tokyo Cabinet: a modern implementation of DBM
================================================================

%package bin
Summary: bin components for the tokyocabinet package.
Group: Binaries
Requires: tokyocabinet-data

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
Requires: tokyocabinet-lib
Requires: tokyocabinet-bin
Requires: tokyocabinet-data
Provides: tokyocabinet-devel

%description dev
dev components for the tokyocabinet package.


%package doc
Summary: doc components for the tokyocabinet package.
Group: Documentation

%description doc
doc components for the tokyocabinet package.


%package lib
Summary: lib components for the tokyocabinet package.
Group: Libraries
Requires: tokyocabinet-data

%description lib
lib components for the tokyocabinet package.


%prep
%setup -q -n tokyocabinet-1.4.48

%build
export LANG=C
export SOURCE_DATE_EPOCH=1492311884
%configure --disable-static
make V=1  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1492311884
rm -rf %{buildroot}
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
/usr/libexec/tcawmgr.cgi

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
/usr/include/*.h
/usr/lib64/libtokyocabinet.so
/usr/lib64/pkgconfig/tokyocabinet.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
%doc /usr/share/man/man3/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libtokyocabinet.so.9
/usr/lib64/libtokyocabinet.so.9.11.0
