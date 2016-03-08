%define dir %{_libdir}/nagios/plugins/igtf

Summary: Nagios plugins for IGTF CA distribution validation
Name: nagios-plugins-igtf
Version: 1.1.0
Release: 1%{?dist}
License: ASL 2.0
Group: Network/Monitoring
Source0: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

%description

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
install --directory ${RPM_BUILD_ROOT}%{dir}
install --mode 755 src/*  ${RPM_BUILD_ROOT}%{dir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{dir}

%changelog
* Tue Mar 8 2016 Emir Imamagic <eimamagi@srce.hr> - 1.1.0-1%{?dist}
- Added new CA probe
* Fri Sep 18 2015 Emir Imamagic <eimamagi@srce.hr> - 1.0.0-1%{?dist}
- Initial version of Nagios plugins for IGTF CA distribution validation
