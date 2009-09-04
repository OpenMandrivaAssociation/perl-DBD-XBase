%define name perl-DBD-XBase
%define real_name DBD-XBase
%define version 0.241
%define release	%mkrel 6

%define summary Module for dealing with XBase files

Summary:        %summary
Name:           %name
Version:        %version
Release:        %release
License:        GPL or Artistic
Group:          Development/Perl
URL:            http://www.fi.muni.cz/~adelton/perl/
Source0:        %real_name-%version.tar.bz2
BuildRoot:      %_tmppath/%name-buildroot
Buildrequires:	perl-devel
Requires:       perl
BuildArch:		noarch

%description
Package DBD::XBase contains module XBase that can read and write dbf and
dbt/fpt files, as well as a DBI driver DBD::XBase, that allows work with these
files using SQL commands.

%prep
%setup -q -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS=vendor PREFIX=%{_prefix}
%make
make test

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

