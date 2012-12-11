%define upstream_name    DBD-XBase
%define upstream_version 1.03

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Module for dealing with XBase files
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/DBD/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(DBI)
BuildArch:	noarch

%description
Package DBD::XBase contains module XBase that can read and write dbf and
dbt/fpt files, as well as a DBI driver DBD::XBase, that allows work with these
files using SQL commands.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README
%{_bindir}/*
%{perl_vendorlib}/XBase.pm
%dir %{perl_vendorlib}/DBD
%{perl_vendorlib}/DBD/*
%dir %{perl_vendorlib}/XBase
%{perl_vendorlib}/XBase/*
%{_mandir}/*/*


%changelog
* Thu Mar 10 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.30.0-1mdv2011.0
+ Revision: 643372
- update to new version 1.03

* Sun Feb 13 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.10.0-1
+ Revision: 637624
- new version
- update to new version 1.01

* Tue Feb 09 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.241.0-1mdv2011.0
+ Revision: 502716
- rebuild using %%perl_convert_version

  + Thierry Vignaud <tv@mandriva.org>
    - BR perl-DBI for the testsuite
    - rebuild

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.241-5mdv2009.0
+ Revision: 241203
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.241-3mdv2008.0
+ Revision: 86341
- rebuild


* Tue Jun 21 2005 Tibor Pittich <Tibor.Pittich@mandriva.org> 0.241-2mdk
- rebuild
- use mkrel

* Tue May 11 2004 Michael Scherer <misc@mandrake.org> 0.241-1mdk
- New release 0.241

* Wed Aug 27 2003 François Pons <fpons@mandrakesoft.com> 0.240-1mdk
- 0.240.

* Tue Jun 03 2003 Tibor Pittich <Tibor.Pittich@phuture.sk> 0.232-1mdk
- initial import into Mandrake. This module required perl-Cstools.

