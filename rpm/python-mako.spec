# fixme: should be defined in base system side
%define python3_sitearch %(%{__python3} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")

Name:       python3-mako
Summary:    Mako template library for Python 3
Version:    1.0.9
Release:    1
Group:      Development/Languages
License:    MIT
URL:        https://www.makotemplates.org/
Source0:    %{name}-%{version}.tar.bz2
BuildArch:      noarch
BuildRequires:  python3-devel
Requires:       python3-markupsafe

%description
Mako is a template library written in Python. It provides a non-XML
syntax which compiles into Python modules for performance. Mako's
syntax and API borrows from Django templates, Cheetah, Myghty, and
Genshi. Conceptually, Mako is an embedded Python (i.e. Python Server
Page) language, which refines the ideas of componentized layout and
inheritance, while maintaining close ties to Python calling and
scoping semantics.

%prep
%setup -q -n %{name}-%{version}/mako

%build
%{__python3} setup.py build

%install
rm -rf %{buildroot}
%{__python3} setup.py install --skip-build --root %{buildroot}

%files
%license LICENSE
%doc CHANGES README.rst examples
%{_bindir}/mako-render
%{python3_sitearch}/*
