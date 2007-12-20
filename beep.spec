Summary:	Beep the pc speaker any number of ways
Name:		beep
Version:	1.2.2
Release:	%mkrel 7
License:	GPL
Group:		Sound
URL:		http://www.johnath.com/beep/
Source0:	http://www.johnath.com/beep/%{name}-%{version}.tar.bz2
Patch0:		beep_1.2.2-17.diff
BuildRoot:	%{_tmppath}/%{name}-buildroot

%description
Beep allows the user to control the pc-speaker with precision,
allowing different sounds to indicate different events. While it
can be run quite happily on the commandline, it's intended place
of residence is within shell/perl scripts, notifying the user when
something interesting occurs. Of course, it has no notion of
what's interesting, but it's real good at that notifying part.

%prep

%setup -q
%patch0 -p1

%build

gcc %{optflags} -Wall -o beep beep.c

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_mandir}/man1
install -m 755 beep %{buildroot}/%{_bindir}/
gunzip beep.1.gz
install -m 644 beep.1 %{buildroot}%{_mandir}/man1/

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGELOG COPYING CREDITS README
%{_bindir}/*
%{_mandir}/man1/*


