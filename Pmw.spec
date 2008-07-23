%define name Pmw
%define major 1
%define minor 2
%define release %mkrel 10


Summary:   Python toolkit for building compound Tkinter widgets
Name:      %name
Version:   %major.%minor
Release:   %release
License:   MIT
Group:     Development/Python
Url:	   http://www.dscpl.com.au/pmw
Source:    %name.%major.%minor.tar.bz2
BuildRoot: %{_tmppath}/%name-root
Requires:  blt tkinter python
Buildarch: noarch
BuildRequires:	python-devel

%description
Pmw is a toolkit for building high-level compound widgets in Python 
using the Tkinter module. It consists of a set of base classes and a 
library of flexible and extensible megawidgets built on this foundation. 
These megawidgets include notebooks, comboboxes, selection widgets, paned 
widgets, scrolled widgets and dialog windows. 

%prep

%setup -q -n %name

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%python_sitelib
mkdir -p $RPM_BUILD_ROOT/%_docdir/%name-%major.%minor
mv README %{name}_%{major}_%{minor}/doc
mv %{name}_%{major}_%{minor}/doc/* $RPM_BUILD_ROOT/%_docdir/%name-%major.%minor
rm -r %{name}_%{major}_%{minor}/doc
cd ..
cp -r %name $RPM_BUILD_ROOT/%python_sitelib

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-,root,root,0755)
%doc %_docdir/%name-%major.%minor
%python_sitelib/%name


