#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: distutils3
#
Name     : pypi-ufo2ft
Version  : 2.33.4
Release  : 6
URL      : https://files.pythonhosted.org/packages/f5/a0/1096922a4aec341767d0b91832e4193ecb8981bb0d86a8716861dbd078c8/ufo2ft-2.33.4.tar.gz
Source0  : https://files.pythonhosted.org/packages/f5/a0/1096922a4aec341767d0b91832e4193ecb8981bb0d86a8716861dbd078c8/ufo2ft-2.33.4.tar.gz
Summary  : A bridge between UFOs and FontTools.
Group    : Development/Tools
License  : MIT
Requires: pypi-ufo2ft-license = %{version}-%{release}
Requires: pypi-ufo2ft-python = %{version}-%{release}
Requires: pypi-ufo2ft-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(py)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
|GitHub Actions status| |PyPI Version| |Codecov| |Gitter Chat|
ufo2ft
======
ufo2ft ("UFO to FontTools") is a fork of
`ufo2fdk <https://github.com/typesupply/ufo2fdk>`__ whose goal is to
generate OpenType font binaries from UFOs without the FDK dependency.

%package license
Summary: license components for the pypi-ufo2ft package.
Group: Default

%description license
license components for the pypi-ufo2ft package.


%package python
Summary: python components for the pypi-ufo2ft package.
Group: Default
Requires: pypi-ufo2ft-python3 = %{version}-%{release}

%description python
python components for the pypi-ufo2ft package.


%package python3
Summary: python3 components for the pypi-ufo2ft package.
Group: Default
Requires: python3-core
Provides: pypi(ufo2ft)
Requires: pypi(booleanoperations)
Requires: pypi(cffsubr)
Requires: pypi(fonttools)

%description python3
python3 components for the pypi-ufo2ft package.


%prep
%setup -q -n ufo2ft-2.33.4
cd %{_builddir}/ufo2ft-2.33.4
pushd ..
cp -a ufo2ft-2.33.4 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1691429245
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-ufo2ft
cp %{_builddir}/ufo2ft-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-ufo2ft/74779b3f20d06c23995b9181b4084fa788e6d694 || :
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-ufo2ft/74779b3f20d06c23995b9181b4084fa788e6d694

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
