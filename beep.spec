Summary:	The pc speaker
Name:		beep
Version:	1.3
Release:	%mkrel 1
License:	GPLv2
Group:		Sound
URL:		http://www.johnath.com/beep/
Source0:	http://www.johnath.com/beep/%{name}-%{version}.tar.gz
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

%build
gcc %{optflags} -Wall -o beep beep.c

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_mandir}/man1
install -m 755 beep %{buildroot}/%{_bindir}/
gunzip beep.1.gz
install -m 644 beep.1 %{buildroot}%{_mandir}/man1/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGELOG COPYING CREDITS README
%{_bindir}/*
%{_mandir}/man1/*




%changelog
* Tue Aug 17 2010 Sandro Cazzaniga <kharec@mandriva.org> 1.3-1mdv2011.0
+ Revision: 570825
- remove p0, previous applied
- new version

* Thu Feb 04 2010 Sandro Cazzaniga <kharec@mandriva.org> 1.2.2-11mdv2010.1
+ Revision: 500663
- Fix summary for this warning
  beep.i586: W: name-repeated-in-summary C Beep
- fix licence

* Tue Sep 01 2009 Thierry Vignaud <tv@mandriva.org> 1.2.2-10mdv2010.0
+ Revision: 424031
- rebuild

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 1.2.2-9mdv2009.0
+ Revision: 243211
- rebuild

* Thu Dec 20 2007 Olivier Blin <oblin@mandriva.com> 1.2.2-7mdv2008.1
+ Revision: 135828
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Fri Dec 22 2006 Oden Eriksson <oeriksson@mandriva.com> 1.2.2-7mdv2007.0
+ Revision: 101615
- Import beep

* Tue Jun 27 2006 Oden Eriksson <oeriksson@mandriva.com> 1.2.2-7mdv2007.0
- added one patch by debian

* Sat May 14 2005 Oden Eriksson <oeriksson@mandriva.com> 1.2.2-6mdk
- rebuild

* Thu Apr 08 2004 Michael Scherer <misc@mandrake.org> 1.2.2-5mdk 
- Build release

