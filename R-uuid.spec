#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-uuid
Version  : 0.1.4
Release  : 46
URL      : https://cran.r-project.org/src/contrib/uuid_0.1-4.tar.gz
Source0  : https://cran.r-project.org/src/contrib/uuid_0.1-4.tar.gz
Summary  : Tools for Generating and Handling of UUIDs
Group    : Development/Tools
License  : BSD-3-Clause MIT
Requires: R-uuid-lib = %{version}-%{release}
BuildRequires : buildreq-R

%description
No detailed description available

%package lib
Summary: lib components for the R-uuid package.
Group: Libraries

%description lib
lib components for the R-uuid package.


%prep
%setup -q -c -n uuid
cd %{_builddir}/uuid

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1589520475

%install
export SOURCE_DATE_EPOCH=1589520475
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library uuid
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library uuid
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library uuid
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc uuid || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/uuid/COPYING
/usr/lib64/R/library/uuid/DESCRIPTION
/usr/lib64/R/library/uuid/INDEX
/usr/lib64/R/library/uuid/LICENSE
/usr/lib64/R/library/uuid/Meta/Rd.rds
/usr/lib64/R/library/uuid/Meta/features.rds
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

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/uuid/libs/uuid.so
/usr/lib64/R/library/uuid/libs/uuid.so.avx2
