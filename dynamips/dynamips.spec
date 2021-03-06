Name: dynamips
Version: 0.2.11
Release: 1%{?dist}
License: GPLv2+
URL: http://www.gns3.net/dynamips
Summary: Cisco router emulator

Source0: https://github.com/GNS3/%{name}/archive/v%{version}.tar.gz

BuildRequires: elfutils-libelf-devel
BuildRequires: libpcap-devel
BuildRequires: libuuid-devel


%description
dynamips emulates Cisco router on a traditional PC. It requires IOS images which
is not included in this package.


%prep
%setup -q


%build
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="$RPM_LD_FLAGS" %{__make} %{_smp_mflags}


%install
%{makeinstall} DESTDIR='%{buildroot}' PREFIX='%{_usr}'


%files
%doc ChangeLog COPYING MAINTAINERS README README.hypervisor RELEASE-NOTES TODO
%{_bindir}/dynamips
%{_bindir}/nvram_export
%{_mandir}/man1/dynamips.1.*
%{_mandir}/man1/nvram_export.1.*
%{_mandir}/man7/hypervisor_mode.7.*


%changelog
* Sun Feb 23 2014 Satoshi Matsumoto <kaorimatz@gmail.com> - 0.2.11-1
- Upgrade to upstream version 0.2.11

* Tue Feb 11 2014 Satoshi Matsumoto <kaorimatz@gmail.com> - 0.2.10-2
- Fix license to GPLv2+

* Thu Feb 06 2014 Satoshi Matsumoto <kaorimatz@gmail.com> - 0.2.10-1
- Initial package
