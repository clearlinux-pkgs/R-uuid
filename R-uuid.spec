#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-uuid
Version  : 0.1
Release  : 1
URL      : https://cran.r-project.org/src/contrib/uuid_0.1-2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/uuid_0.1-2.tar.gz
Summary  : Tools for generating and handling of UUIDs
Group    : Development/Tools
License  : MIT
Requires: R-uuid-lib
BuildRequires : clr-R-helpers

%description
No detailed description available

%package lib
Summary: lib components for the R-uuid package.
Group: Libraries

%description lib
lib components for the R-uuid package.


%prep
%setup -q -c -n uuid

%build
export LANG=C
export SOURCE_DATE_EPOCH=1486941825

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1486941825
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library uuid
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library uuid


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/uuid/COPYING
/usr/lib64/R/library/uuid/DESCRIPTION
/usr/lib64/R/library/uuid/INDEX
/usr/lib64/R/library/uuid/LICENSE
/usr/lib64/R/library/uuid/Meta/Rd.rds
/usr/lib64/R/library/uuid/Meta/hsearch.rds
/usr/lib64/R/library/uuid/Meta/links.rds
/usr/lib64/R/library/uuid/Meta/nsInfo.rds
/usr/lib64/R/library/uuid/Meta/package.rds
/usr/lib64/R/library/uuid/NAMESPACE
/usr/lib64/R/library/uuid/NEWS
/usr/lib64/R/library/uuid/R/uuid
/usr/lib64/R/library/uuid/R/uuid.rdb
/usr/lib64/R/library/uuid/R/uuid.rdx
/usr/lib64/R/library/uuid/help/AnIndex
/usr/lib64/R/library/uuid/help/aliases.rds
/usr/lib64/R/library/uuid/help/paths.rds
/usr/lib64/R/library/uuid/help/uuid.rdb
/usr/lib64/R/library/uuid/help/uuid.rdx
/usr/lib64/R/library/uuid/html/00Index.html
/usr/lib64/R/library/uuid/html/R.css
/usr/lib64/R/library/uuid/libs/symbols.rds

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/uuid/libs/uuid.so
