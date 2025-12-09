Summary:	Beep the PC speaker any number of ways
Name:		beep
Version:	1.4.12
Release:	1
License:	GPLv2+
Group:		Sound
# Old stuff: http://www.johnath.com/beep/ - Use a more recent fork
Url:		https://github.com/spkr-beep/beep/
Source0:	https://github.com/spkr-beep/beep/archive/%{name}-%{version}.tar.gz
Source1:	70-pcspkr-beep.rules
Source2:	90-pcspkr-beep.rules
Source3:	pcspkr-beep.conf
Source4:	beep.sysusers.conf
Source5:	README.usage
Patch0:	beep-1.4.12-add-SIGHUP-handling.patch
Patch1:	beep-1.4.12-drop-Werror.patch
BuildRequires:	kernel-headers
#BuildRequires:	systemd-units
#BuildRequires:	ubsan-devel
# For /etc/modprobe.conf.d
#Requires:	kmod-compat
Requires(pre):	rpm-helper
Requires(pre):	systemd

%description
Beep allows the user to control the PC speaker with precision, allowing
different sounds to indicate different events. While it can be run quite
happily on the command line, it's intended place of residence is within
shell/Perl scripts, notifying the user when something interesting occurs.
Of course, it has no notion of what's interesting, but it's real good at the
notifying part.

%files
%doc COPYING CREDITS.md NEWS.md README.md PERMISSIONS.md
%doc README.usage
%config(noreplace) %{_sysconfdir}/modprobe.d/%{name}.conf
%config(noreplace) %{_sysconfdir}/modules-load.d/%{name}.conf
%{_udevrulesdir}/70-pcspkr-%{name}.rules
%{_udevrulesdir}/90-pcspkr-%{name}.rules
%{_sysusersdir}/%{name}.conf
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_docdir}/%{name}/contrib/*

%pre
%sysusers_create_package %{name} %{SOURCE4}

#-----------------------------------------------------------------------------

%prep
%autosetup -p1

install -m 0644 %{SOURCE5} .


%build
%make_build prefix="%{_prefix}" COMPILERS=clang CFLAGS_clang="%{optflags}" LDFLAGS="%{ldflags}" CPPFLAGS_clang="%{optflags}"


%install
%make_install prefix="%{_prefix}" COMPILERS=clang CFLAGS_clang="%{optflags}" LDFLAGS="%{ldflags}" CPPFLAGS_clang="%{optflags}"

# 1. Prepare the needed dirs
mkdir -p %{buildroot}%{_sysconfdir}/modprobe.d/
mkdir -p %{buildroot}%{_sysconfdir}/modules-load.d
mkdir -p %{buildroot}%{_udevrulesdir}/
mkdir -p %{buildroot}%{_sysusersdir}/

# 2. Install our stuff
install -m 644 %{SOURCE1} %{buildroot}%{_udevrulesdir}/
install -m 644 %{SOURCE2} %{buildroot}%{_udevrulesdir}/
install -m 644 %{SOURCE3} %{buildroot}%{_sysconfdir}/modprobe.d/%{name}.conf
install -m 644 %{SOURCE4} %{buildroot}%{_sysusersdir}/%{name}.conf

# To allow loading pcspkr module on-demand
echo "pcspkr" > %{buildroot}%{_sysconfdir}/modules-load.d/%{name}.conf

# Drop what we already pick up with our %%doc macro
rm -f  %{buildroot}%{_docdir}/%{name}/{CREDITS,NEWS}.md
