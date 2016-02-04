Summary: Browser default start page for StotinkaOS
Name: stotinkaos-indexhtml
Version: 7
Release: 9%{?dist}.sos
Source: %{name}-%{version}.tar.gz
License: Distributable
Group: Documentation
BuildArchitectures: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Obsoletes: indexhtml <= 2:5-1
Obsoletes: centos-indexhtml redhat-indexhtml
Provides: redhat-indexhtml centos-indexhtml

%description
The indexhtml package contains the welcome page shown by your Web browser,
which you'll see after you've successfully installed StotinkaOS Linux

%prep
%setup -q -n HTML

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_defaultdocdir}/HTML
mkdir -p $RPM_BUILD_ROOT/%{_defaultdocdir}/HTML/en-US
cp -a . $RPM_BUILD_ROOT/%{_defaultdocdir}/HTML/
pushd $RPM_BUILD_ROOT/%{_defaultdocdir}/HTML/en-US
ln -s ../index.html .
ln -s ../img/ .
popd

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_defaultdocdir}/HTML/*

%changelog
* Sun Jan 31 2016 StotinkaOS Team <stotinkaos.bg@gmail.com> - 7-9.el7.sos
- Initial build for StotinkaOS 7

* Sun Jun 29 2014 Johnny Hughes <johnny@centos.org> 7-9.el7.centos
- Add en-US directory

* Fri May 16 2014 Johnny Hughes <johnny@centos.org> 7-8.el7.centos
- Roll in CentOS Branding
