#
# TODO:
#	- clean up Requires (still)
#	- test cryptroot, dmraid, mdadm, opensc, openct modules
#
Summary:	Tools for generating an initramfs
Summary(pl.UTF-8):	Narzędzia do tworzenia initramfs
Name:		initramfs-tools
Version:	0.93.4
Release:	4
License:	Public Domain
Group:		Applications/System
Source0:	http://ftp.de.debian.org/debian/pool/main/i/initramfs-tools/%{name}_%{version}.tar.gz
# Source0-md5:	06415435a4ba85713ea50b34e212d73c
Patch0:		%{name}-undebianize.patch
Patch1:		%{name}-nobb.patch
Patch2:		%{name}-gz-modules.patch
Patch3:		%{name}-less-noise.patch
Patch4:		%{name}-initrdtools.patch
Patch5:		%{name}-klibcdir.patch
Patch6:		%{name}-no-backup.patch
URL:		http://git.debian.org/?p=kernel/initramfs-tools.git;a=shortlog
Requires:	/usr/bin/ldd
Requires:	/usr/bin/locale
# Probably gawk
Requires:	awk
Requires:	busybox >= 1.12.4-3
Requires:	coreutils
Requires:	cpio
Requires:	findutils
Requires:	grep
Requires:	gzip
Requires:	klibc >= 1.5.15-3
Requires:	klibc-utils-shared >= 1.5.15-3
Requires:	module-init-tools
Requires:	mount
Requires:	udev-initramfs
Requires:	util-linux-ng
Suggests:	cryptsetup-luks-initramfs
Suggests:	dmraid-initramfs >= 1.0.0-0.rc15.3
Suggests:	lvm2-initramfs
Suggests:	mdadm-initramfs
Suggests:	multipath-tools-initramfs
Suggests:	openct-initramfs
Suggests:	opensc-initramfs
Suggests:	busybox-initrd >= 1.15.3-2
Suggests:	cryptsetup-luks-initrd
Suggests:	device-mapper-initrd
Suggests:	dmraid-initrd
Suggests:	e2fsprogs-initrd
Suggests:	lvm2-initrd
Suggests:	mdadm-initrd
Suggests:	module-init-tools-initrd
Suggests:	suspend-initrd
Suggests:	udev-initrd
Suggests:	util-linux-ng-initrd
Suggests:	v86d-initrd
Suggests:	xfsprogs-initrd
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
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

sed -i -e 's|__KLIBCDIR__|%{_lib}|g' hook-functions mkinitramfs
sed -i -e 's|INITRDDIR="/usr/lib/initrd"|INITRDDIR="/usr/%{_lib}/initrd"|' mkinitramfs

# cleanup backups after patching
find '(' -name '*~' -o -name '*.orig' ')' -print0 | xargs -0 -r -l512 rm -f

%build

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_sysconfdir}/initramfs-tools/{hooks,/conf.d}
install -d $RPM_BUILD_ROOT%{_sysconfdir}/initramfs-tools/scripts/{init,local,nfs}-{bottom,premount,top}
install -d $RPM_BUILD_ROOT%{_datadir}/initramfs-tools/scripts/{init,local,nfs}-{bottom,premount,top}
install -d $RPM_BUILD_ROOT%{_datadir}/initramfs-tools/{conf.d,conf-hooks.d,modules.d}
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
%dir %{_datadir}/initramfs-tools/conf-hooks.d
%dir %{_datadir}/initramfs-tools/modules.d
%dir %{_datadir}/initramfs-tools/scripts
%dir %{_datadir}/initramfs-tools/scripts/init-bottom
%dir %{_datadir}/initramfs-tools/scripts/init-premount
%dir %{_datadir}/initramfs-tools/scripts/init-top
%dir %{_datadir}/initramfs-tools/scripts/local-bottom
%dir %{_datadir}/initramfs-tools/scripts/local-premount
%dir %{_datadir}/initramfs-tools/scripts/local-top
%dir %{_datadir}/initramfs-tools/scripts/nfs-bottom
%dir %{_datadir}/initramfs-tools/scripts/nfs-premount
%dir %{_datadir}/initramfs-tools/scripts/nfs-top
%{_datadir}/initramfs-tools/scripts/functions
%{_datadir}/initramfs-tools/scripts/local
%{_datadir}/initramfs-tools/scripts/nfs
%attr(755,root,root) %{_datadir}/initramfs-tools/scripts/init-premount/*
%attr(755,root,root) %{_datadir}/initramfs-tools/scripts/init-top/*
%attr(755,root,root) %{_datadir}/initramfs-tools/scripts/local-premount/*
%attr(755,root,root) %{_sbindir}/*
%dir /var/lib/initramfs-tools
%{_mandir}/man[58]/*
