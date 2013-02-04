# NOTE
# - i'm installing under jquery, because then i have webserver alias already
#   set, and nobody else seems to care. then again, if you need it under moo
#   tools you could create own package for mootools
%define		plugin	jstorage
Summary:	jStorage - store data locally with JavaScript
Name:		jquery-%{plugin}
Version:	0.3.2
Release:	1
License:	MIT
Group:		Applications/WWW
Source0:	https://github.com/andris9/jStorage/archive/v%{version}.tar.gz?/%{plugin}-%{version}.tgz
# Source0-md5:	4f13636646ad69100cb8183d978b288f
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
%setup -qn jStorage-%{version}

grep '"%{version}"' jstorage.js

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appdir}
cp -p %{plugin}.min.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}-%{version}.min.js
cp -p %{plugin}.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}-%{version}.js
ln -s %{plugin}-%{version}.min.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}.js
ln -s %{plugin}-%{version}.min.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}.min.js
ln -s %{plugin}-%{version}.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}.src.js

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md test.html
%{_appdir}
