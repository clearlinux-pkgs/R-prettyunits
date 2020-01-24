#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-prettyunits
Version  : 1.1.1
Release  : 26
URL      : https://cran.r-project.org/src/contrib/prettyunits_1.1.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/prettyunits_1.1.1.tar.gz
Summary  : Pretty, Human Readable Formatting of Quantities
Group    : Development/Tools
License  : MIT
BuildRequires : buildreq-R

%description
[![Linux Build Status](https://travis-ci.org/r-lib/prettyunits.svg?branch=master)](https://travis-ci.org/r-lib/prettyunits)
[![Windows Build status](https://ci.appveyor.com/api/projects/status/github/r-lib/prettyunits?svg=true)](https://ci.appveyor.com/project/gaborcsardi/prettyunits)
[![CRAN RStudio mirror downloads](http://cranlogs.r-pkg.org/badges/prettyunits)](https://CRAN.R-project.org/package=prettyunits)

%prep
%setup -q -c -n prettyunits

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1579882838

%install
export SOURCE_DATE_EPOCH=1579882838
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
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
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library prettyunits
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library prettyunits
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library prettyunits
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc prettyunits || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/prettyunits/DESCRIPTION
/usr/lib64/R/library/prettyunits/INDEX
/usr/lib64/R/library/prettyunits/LICENSE
/usr/lib64/R/library/prettyunits/Meta/Rd.rds
/usr/lib64/R/library/prettyunits/Meta/features.rds
/usr/lib64/R/library/prettyunits/Meta/hsearch.rds
/usr/lib64/R/library/prettyunits/Meta/links.rds
/usr/lib64/R/library/prettyunits/Meta/nsInfo.rds
/usr/lib64/R/library/prettyunits/Meta/package.rds
/usr/lib64/R/library/prettyunits/NAMESPACE
/usr/lib64/R/library/prettyunits/NEWS.md
/usr/lib64/R/library/prettyunits/R/prettyunits
/usr/lib64/R/library/prettyunits/R/prettyunits.rdb
/usr/lib64/R/library/prettyunits/R/prettyunits.rdx
/usr/lib64/R/library/prettyunits/help/AnIndex
/usr/lib64/R/library/prettyunits/help/aliases.rds
/usr/lib64/R/library/prettyunits/help/paths.rds
/usr/lib64/R/library/prettyunits/help/prettyunits.rdb
/usr/lib64/R/library/prettyunits/help/prettyunits.rdx
/usr/lib64/R/library/prettyunits/html/00Index.html
/usr/lib64/R/library/prettyunits/html/R.css
/usr/lib64/R/library/prettyunits/tests/testthat.R
/usr/lib64/R/library/prettyunits/tests/testthat/test-bytes.r
/usr/lib64/R/library/prettyunits/tests/testthat/test-ms.r
/usr/lib64/R/library/prettyunits/tests/testthat/test-vague-dt.r
