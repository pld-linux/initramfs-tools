#
# TODO:
#	- pl desc
#	- clean up Requires
#	- our klibc is really messed up
#	- undebianize
#
Summary:	Tools for generating an initramfs
Summary(pl.UTF-8):	Narzędzia do tworzenia initramfs
Name:		initramfs-tools
Version:	0.93
Release:	0.1
License:	Public Domain
Group:		Applications/System
Source0:	http://ftp.de.debian.org/debian/pool/main/i/initramfs-tools/%{name}_%{version}.tar.gz
# Source0-md5:	97b6188728c9ecacd21e9b4f06a3e86a
URL:		http://git.debian.org/?p=kernel/initramfs-tools.git;a=shortlog
# Probably gawk
Requires:	awk
Requires:	busybox
Requires:	coreutils
Requires:	cpio
#Requires:	cryptsetup-luks
Requires:	findutils
Requires:	glibc-misc
Requires:	grep
Requires:	gzip
Requires:	klibc
Requires:	klibc-utils-shared
#Requires:	lvm2
Requires:	module-init-tools
Requires:	mount
Requires:	udev-core
Requires:	util-linux-ng
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains tools to create and boot an initramfs for
packaged 2.6 Linux kernel. The initramfs is a gzipped cpio archive.
At boot time, the kernel unpacks that archive into RAM, mounts and
uses it as initial root file system. The mounting of the real root
file system occurs in early user space. klibc provides utilities to
setup root. Having the root on EVMS, MD, LVM2, LUKS or NFS is also
supported. Any boot loader with initrd support is able to load an
initramfs archive.

#%description -l pl.UTF-8

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_sysconfdir}/initramfs-tools/scripts/{init-bottom,init-premount,init-top,local-bottom,local-premount,local-top,nfs-bottom,nfs-premount,nfs-top}
install -d $RPM_BUILD_ROOT%{_sysconfdir}/initramfs-tools/{hooks,/conf.d}
install -d $RPM_BUILD_ROOT%{_datadir}/initramfs-tools/{conf.d,hooksconf.d,modules.d}
install -d $RPM_BUILD_ROOT/var/lib/initramfs-tools
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man{5,8}}

cp -a init scripts hooks hook-functions $RPM_BUILD_ROOT%{_datadir}/initramfs-tools
install mkinitramfs update-initramfs $RPM_BUILD_ROOT%{_sbindir}
install conf/initramfs.conf conf/update-initramfs.conf conf/modules $RPM_BUILD_ROOT%{_sysconfdir}/initramfs-tools

install initramfs.conf.5 update-initramfs.conf.5 $RPM_BUILD_ROOT%{_mandir}/man5
install mkinitramfs.8 initramfs-tools.8 update-initramfs.8 $RPM_BUILD_ROOT%{_mandir}/man8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc HACKING docs/*
%dir %{_sysconfdir}/initramfs-tools
%dir %{_sysconfdir}/initramfs-tools/conf.d
%dir %{_sysconfdir}/initramfs-tools/hooks
%dir %{_sysconfdir}/initramfs-tools/scripts
%dir %{_sysconfdir}/initramfs-tools/scripts/init-bottom
%dir %{_sysconfdir}/initramfs-tools/scripts/init-premount
%dir %{_sysconfdir}/initramfs-tools/scripts/init-top
%dir %{_sysconfdir}/initramfs-tools/scripts/local-bottom
%dir %{_sysconfdir}/initramfs-tools/scripts/local-premount
%dir %{_sysconfdir}/initramfs-tools/scripts/local-top
%dir %{_sysconfdir}/initramfs-tools/scripts/nfs-bottom
%dir %{_sysconfdir}/initramfs-tools/scripts/nfs-premount
%dir %{_sysconfdir}/initramfs-tools/scripts/nfs-top
%{_sysconfdir}/initramfs-tools/initramfs.conf
%{_sysconfdir}/initramfs-tools/modules
%{_sysconfdir}/initramfs-tools/update-initramfs.conf
%dir %{_datadir}/initramfs-tools
%{_datadir}/initramfs-tools/hook-functions
%attr(755,root,root) %{_datadir}/initramfs-tools/init
%dir %{_datadir}/initramfs-tools/conf.d
%dir %{_datadir}/initramfs-tools/hooks
%attr(755,root,root) %{_datadir}/initramfs-tools/hooks/*
%dir %{_datadir}/initramfs-tools/hooksconf.d
%dir %{_datadir}/initramfs-tools/modules.d
%dir %{_datadir}/initramfs-tools/scripts
%{_datadir}/initramfs-tools/scripts/functions
%{_datadir}/initramfs-tools/scripts/local
%{_datadir}/initramfs-tools/scripts/nfs
%dir %{_datadir}/initramfs-tools/scripts/init-premount
%attr(755,root,root) %{_datadir}/initramfs-tools/scripts/init-premount/*
%dir %{_datadir}/initramfs-tools/scripts/init-top
%attr(755,root,root) %{_datadir}/initramfs-tools/scripts/init-top/*
%dir %{_datadir}/initramfs-tools/scripts/local-premount
%attr(755,root,root) %{_datadir}/initramfs-tools/scripts/local-premount/*
%attr(755,root,root) %{_sbindir}/*
%dir /var/lib/initramfs-tools
%{_mandir}/man[58]/*
