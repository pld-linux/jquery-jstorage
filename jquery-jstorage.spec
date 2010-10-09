# NOTE
# - i'm installing under jquery, because then i have webserver alias already
#   set, and nobody else seems to care. then again, if you need it under moo
#   tools you could create own package for mootools
%define		plugin	jstorage
Summary:	jStorage - store data locally with JavaScript
Name:		jquery-%{plugin}
Version:	0.1.4.1
Release:	1
License:	MIT
Group:		Applications/WWW
Source0:	http://github.com/andris9/jStorage/tarball/master#/%{plugin}-%{version}.tgz
# Source0-md5:	6a75f6418e39cce47b8c91d53e3d8338
URL:		http://www.jstorage.info/
BuildRequires:	rpmbuild(macros) >= 1.268
Requires:	jquery
Requires:	jquery-json
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir	%{_datadir}/jquery/%{plugin}

%description
jStorage is a simple wrapper plugin for Prototype, MooTools and jQuery
to cache data (string, numbers, objects, even XML nodes) on browser
side.

jStorage was first developed under the name of DOMCached but since a
lot of features were dropped to make it simpler (like the support for
namespaces and such) it was renamed. DOMCached had separate files for
working with Prototype and jQuery but jStorage can handle both in one
go.

%prep
%setup -qc
mv *-jStorage-*/* .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appdir}
cp -a jstorage.min.js $RPM_BUILD_ROOT%{_appdir}/jstorage.js

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README test.html
%{_appdir}