#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	File
%define	pnam	BaseDir
Summary:	File::BaseDir - use the freedesktop basedir spec
Summary(pl):	File::BaseDir - u¿ywanie specyfikacji basedir z freedesktop
Name:		perl-File-BaseDir
Version:	0.02
Release:	1
Vendor:		Jaap Karssenberg <pardus@cpan.org>
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	00e2729f364d430350355250cb9007e0
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

%description -l pl
Ten modu³ mo¿e byæ u¿ywany do znajdowania katalogów i plików zgodnie
ze specyfikacj± XDG Base Directory Specification. Dba o ustawienia
domy¶lne i u¿ywa File::Spec aby wyj¶cie by³o zale¿ne od platformy.

Ten modu³ jest odga³êzieniem File::MimeInfo.

Dla tego modu³u u¿yto specyfikacji XDG basedir w wersji 0.6.

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
