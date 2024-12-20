Summary:	Canonical source for classifiers on PyPI (pypi.org)
Name:		python-trove-classifiers
Version:	2024.10.21.16
Release:	1
License:	Apache-2.0
Group:		Development/Python
URL:		https://pypi.org/project/trove-classifiers/
Source0:	https://files.pythonhosted.org/packages/source/t/trove-classifiers/trove_classifiers-%{version}.tar.gz
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)
BuildRequires:	python%{pyver}dist(calver)
BuildArch:	noarch

%description
Canonical source for classifiers on PyPI.

Classifiers categorize projects per PEP 301. Use this package to validate
classifiers in packages for PyPI upload or download.

%files
%license LICENSE
%doc README.md
%{py_sitedir}/trove_classifiers
%{py_sitedir}/trove_classifiers-*.*-info

#--------------------------------------------------------------------

%prep
%autosetup -p1 -n trove_classifiers-%{version}

%build
%py_build

%install
%py_install
