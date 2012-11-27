Summary:	Shared color profiles to be used in color management aware applications
Name:		shared-color-profiles
Version:	0.1.6
Release:	1
License:	Free (Public Domain, CC-BY-SA, CC-BY-ND, zlib, MIT - depending on profile)
Group:		Libraries
Source0:	http://people.freedesktop.org/~hughsient/releases/%{name}-%{version}.tar.xz
# Source0-md5:	f81b3316a3052a99784d01205425be88
URL:		http://github.com/hughsie/shared-color-profiles
# /usr/bin/colprof
BuildRequires:	argyllcms
# /usr/bin/cd-create-profile
# /usr/bin/cd-fix-profile
BuildRequires:	colord
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains various profiles which are useful for programs
that are color management aware.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%{_datadir}/color/icc/*.ic[cm]
%{_datadir}/color/icc/Oysonar
%{_datadir}/color/icc/Yamma
%{_datadir}/shared-color-profiles

