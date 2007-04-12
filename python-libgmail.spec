%define oname libgmail
%define name python-%oname
%define version 0.1.5.1
%define release %mkrel 1

Summary: Python bindings to access Gmail
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://downloads.sourceforge.net/libgmail/%{oname}-%{version}.tar.bz2
License: GPL
Group: Development/Python
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Url: http://libgmail.sourceforge.net/
BuildArch: noarch
BuildRequires: python-devel

%description
This is a Python library to access Google Mail.

%prep
%setup -q -n %oname-%version

%build
python setup.py build

%install
python setup.py install --root=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%py_puresitedir/lgconstants.py*
%py_puresitedir/libgmail*

