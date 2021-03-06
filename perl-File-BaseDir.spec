#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define	pdir	File
%define	pnam	BaseDir
Summary:	File::BaseDir - use the freedesktop basedir spec
Summary(pl.UTF-8):	File::BaseDir - używanie specyfikacji basedir z freedesktop
Name:		perl-File-BaseDir
Version:	0.03
Release:	1
Vendor:		Jaap Karssenberg <pardus@cpan.org>
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/File/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	527596f1507894dfaacdda72ea6dbb31
URL:		http://search.cpan.org/dist/File-BaseDir/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module can be used to find directories and files as specified by
the XDG Base Directory Specification. It takes care of defaults and
uses File::Spec to make the output platform specific.

This module forked from File::MimeInfo.

For this module the XDG basedir specification 0.6 was used.

%description -l pl.UTF-8
Ten moduł może być używany do znajdowania katalogów i plików zgodnie
ze specyfikacją XDG Base Directory Specification. Dba o ustawienia
domyślne i używa File::Spec aby wyjście było zależne od platformy.

Ten moduł jest odgałęzieniem File::MimeInfo.

Dla tego modułu użyto specyfikacji XDG basedir w wersji 0.6.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/File/*.pm
%{_mandir}/man3/*
