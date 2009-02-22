#
# Conditional build:
%bcond_with	tests		# build with tests
%bcond_without	tests		# build without tests
#
Summary:	-
Summary(pl.UTF-8):	-
Name:		initramfs-tools
Version:	0.93
Release:	0.1
License:	Public Domain
Group:		Applications/System
Source0:	http://ftp.de.debian.org/debian/pool/main/i/initramfs-tools/%{name}_%{version}.tar.gz
# Source0-md5:	97b6188728c9ecacd21e9b4f06a3e86a
URL:		http://git.debian.org/?p=kernel/initramfs-tools.git;a=shortlog
#BuildRequires:	-
#BuildRequires:	autoconf
#BuildRequires:	automake
#BuildRequires:	intltool
#BuildRequires:	libtool
#Requires:	-
#Provides:	-
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%description -l pl.UTF-8

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
%doc AUTHORS CREDITS ChangeLog NEWS README THANKS TODO

%if 0
# if _sysconfdir != /etc:
#%%dir %{_sysconfdir}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%endif

#%{_examplesdir}/%{name}-%{version}
