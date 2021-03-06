Name: kaorimatz-release
Version: 21
Release: 0.1%{?dist}
License: MIT
URL: http://packages.kaorimatz.org/fedora
Summary: Configurations for kaorimatz repository

Source0: kaorimatz.repo
Source1: kaorimatz-rawhide.repo
Source2: RPM-GPG-KEY-kaorimatz

BuildArch: noarch


%description
This package contains the GPG key and the yum configuration files for the
"kaorimatz" repository.


%prep


%build


%install
%{__install} -D -m 644 %{SOURCE0} %{buildroot}%{_sysconfdir}/yum.repos.d/kaorimatz.repo
%{__install} -D -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/yum.repos.d/kaorimatz-rawhide.repo
%{__install} -D -m 644 %{SOURCE2} %{buildroot}%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-kaorimatz


%files
%dir %{_sysconfdir}/yum.repos.d
%config(noreplace) %{_sysconfdir}/yum.repos.d/kaorimatz*.repo
%dir %{_sysconfdir}/pki/rpm-gpg
%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-kaorimatz


%changelog
* Mon Mar 10 2014 Satoshi Matsumoto <kaorimatz@gmail.com> - 21-0.1
- Update to Fedora 21 (Rawhide)

* Mon Mar 10 2014 Satoshi Matsumoto <kaorimatz@gmail.com> - 20-1
- Update to Fedora 20

* Sat Mar 08 2014 Satoshi Matsumoto <kaorimatz@gmail.com> - 19-1
- Initial package
