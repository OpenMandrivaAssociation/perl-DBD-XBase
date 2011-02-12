%define upstream_name    DBD-XBase
%define upstream_version 1.01

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Module for dealing with XBase files
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://www.fi.muni.cz/~adelton/perl/
Source0:    %upstream_name-%upstream_version.tar.bz2

# for testsuite:
#Buildrequires:	perl-DBI
BuildArch:		noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}

%description
Package DBD::XBase contains module XBase that can read and write dbf and
dbt/fpt files, as well as a DBI driver DBD::XBase, that allows work with these
files using SQL commands.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS=vendor PREFIX=%{_prefix}
%make

%check
%make test

%install
[ "%{buildroot}" != "/" ] && rm -rf %buildroot
%makeinstall PREFIX=$RPM_BUILD_ROOT%{_prefix}

%clean
[ "%{buildroot}" != "/" ] && rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README
%{_bindir}/*
%{perl_vendorlib}/XBase.pm
%dir %{perl_vendorlib}/DBD
%{perl_vendorlib}/DBD/*
%dir %{perl_vendorlib}/XBase
%{perl_vendorlib}/XBase/*
%{_mandir}/*/*
