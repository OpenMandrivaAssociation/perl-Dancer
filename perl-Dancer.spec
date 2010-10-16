%define upstream_name    Dancer
%define upstream_version 1.1901

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Template Toolkit wrapper for Dancer
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module//%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Encode)
BuildRequires: perl(File::Basename)
BuildRequires: perl(File::Spec)
BuildRequires: perl(HTTP::Body)
BuildRequires: perl(HTTP::Server::Simple::PSGI)
BuildRequires: perl(LWP)
BuildRequires: perl(MIME::Types)
BuildRequires: perl(Test::More)
BuildRequires: perl(Time::HiRes)
BuildRequires: perl(URI)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README CHANGES META.yml LICENSE
%{_bindir}/dancer
%{_mandir}/man1/dancer.1*
%{_mandir}/man3/*
%perl_vendorlib/*


