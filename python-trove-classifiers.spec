Summary:	Canonical source for classifiers on PyPI (pypi.org)
Name:		python-trove-classifiers
Version:	2023.3.9
Release:	1
License:	Apache-2.0
Group:		Development/Python
URL:		https://pypi.org/project/trove-classifiers/
Source0:	https://files.pythonhosted.org/packages/source/t/trove-classifiers/trove-classifiers-%{version}.tar.gz
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)

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
%autosetup -p1 -n trove-classifiers-%{version}

%build
%py_build

%install
%py_install

