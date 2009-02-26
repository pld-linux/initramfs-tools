#
# TODO:
#	- clean up Requires
#
Summary:	Tools for generating an initramfs
Summary(pl.UTF-8):	Narzędzia do tworzenia initramfs
Name:		initramfs-tools
Version:	0.93
Release:	0.7
License:	Public Domain
Group:		Applications/System
Source0:	http://ftp.de.debian.org/debian/pool/main/i/initramfs-tools/%{name}_%{version}.tar.gz
# Source0-md5:	97b6188728c9ecacd21e9b4f06a3e86a
Patch0:		%{name}-undebianize.patch
Patch1:		%{name}-nobb.patch
Patch2:		%{name}-gz-modules.patch
URL:		http://git.debian.org/?p=kernel/initramfs-tools.git;a=shortlog
# Probably gawk
Requires:	awk
Requires:	busybox >= 1.12.4-3
Requires:	coreutils
Requires:	cpio
Requires:	findutils
Requires:	glibc-misc
Requires:	grep
Requires:	gzip
Requires:	klibc >= 1.5.15-3
Requires:	klibc-utils-shared >= 1.5.15-3
Requires:	module-init-tools
Requires:	mount
Requires:	udev-initramfs
Requires:	util-linux-ng
Suggests:	cryptsetup-luks-initramfs
Suggests:	dmraid-initramfs
Suggests:	lvm2-initramfs
Suggests:	mdadm-initramfs
Suggests:	multipath-tools-initramfs
Suggests:	openct-initramfs
Suggests:	opensc-initramfs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
initramfs-tools is an hookable initramfs generator.
It can boot on NFS, LVM2, md, LUKS, dmraid, oldstyle devices, ...
The generated initramfs is generic, but can explicitly be tuned
for small.
It is written in POSIX shell, has an "end-user" friendly
invocation with update-initramfs and the low level mkinitramfs.
The initramfs uses klibc, comes together with a rescue shell.
It is possible to ssh into it.

%description -l pl.UTF-8
initramfs-tools to generator initramfs.
Umożliwia bootowanie ze zwykłych urządzeń, LVM2, md, LUKS, dmraid
czy NFS. Utworzony initramfs jest ogólny, ale można go dostroić
tak aby był minimalny.
initramfs-tools jest napisany w shellu zgodnym ze standardem POSIX.
Można go wywoływać poprzez przyjazny dla użytkownika update-initramfs
i niskopoziomowy mkinitramfs. Utworzony initramfs używa klibc, posiada
wbudowany ratunkowy shell do którego można zalogować się przez ssh.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

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
