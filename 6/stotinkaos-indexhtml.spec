Summary: Browser default start page for StotinkaOS
Name: stotinkaos-indexhtml
Version: 6
Release: 8%{?dist}
Source: %{name}-%{version}.tar.gz
License: Distributable
Group: Documentation
BuildArchitectures: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Obsoletes: indexhtml <= 2:5-1 centos-indexhtml
Provides: redhat-indexhtml centos-indexhtml

%description
The indexhtml package contains the welcome page shown by your Web browser,
which you'll see after you've successfully installed CentOS Linux

%prep
%setup -q -n HTML

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_defaultdocdir}/HTML
cp -a . $RPM_BUILD_ROOT/%{_defaultdocdir}/HTML/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_defaultdocdir}/HTML/*

%changelog
* Fri Jun 03 2016 StotinkaOS Team <stotinkaos.bg@gmail.com> - 6-8.el6.sos
- Update to 6.8

* Sat Jan 31 2015 Ivaylo Kuzev <ivkuzev@gmail.com> - 6-6.el6.sos
- Initial build for StotinkaOS

* Wed Jun 29 2011 Karanbir Singh <kbsingh@centos.org> 6-1.el6.centos
- Roll in CentOS Branding
