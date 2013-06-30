%define upstream_name    Dancer
%define upstream_version 1.3115

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	Template Toolkit wrapper for Dancer
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module//%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Encode)
BuildRequires:	perl(File::Basename)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(HTTP::Body)
BuildRequires:	perl(HTTP::Server::Simple::CGI)
BuildRequires:	perl(HTTP::Server::Simple::PSGI)
BuildRequires:	perl(LWP)
BuildRequires:	perl(Module::Runtime)
BuildRequires:	perl(MIME::Types)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Time::HiRes)
BuildRequires:	perl(Try::Tiny)
BuildRequires:	perl(URI)
BuildArch:	noarch

%description
Dancer is a web application framework designed to be as effortless as
possible for the developer, taking care of the boring bits as easily as
possible, yet staying out of your way and letting you get on with writing
your code.

Dancer aims to provide the simplest way for writing web applications, and
offers the flexibility to scale between a very simple lightweight web
service consisting of a few lines of code in a single file, all the way up
to a more complex fully-fledged web application with session support,
templates for views and layouts, etc.

If you don't want to write CGI scripts by hand, and find Catalyst too big
or cumbersome for your project, Dancer is what you need.

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
%doc README CHANGES META.yml LICENSE
%{_bindir}/dancer
%{_mandir}/man1/dancer.1*
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Mon May 02 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.304.0-1mdv2011.0
+ Revision: 662493
- update to new version 1.3040

* Sun Apr 17 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.303.0-1
+ Revision: 654040
- update to new version 1.3030

* Wed Mar 23 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.302.0-1
+ Revision: 648069
- update to new version 1.3020

* Sat Feb 12 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.301.0-1
+ Revision: 637366
- update to new version 1.3010

* Thu Dec 23 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.200.300-1mdv2011.0
+ Revision: 624079
- update to new version 1.2003

* Sun Nov 14 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.190.400-1mdv2011.0
+ Revision: 597575
- update to new version 1.1904

* Sat Oct 16 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.190.100-1mdv2011.0
+ Revision: 586104
- import perl-Dancer

