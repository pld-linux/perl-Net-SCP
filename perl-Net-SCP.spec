#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	Net
%define		pnam	SCP
Summary:	Net::SCP - Perl extension for secure copy protocol
Summary(pl.UTF-8):	Net::SCP - perlowe rozszerzenie do obsługi protokołu bezpiecznego kopiowania
Name:		perl-Net-SCP
Version:	0.08
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Net/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	09005478b3eb9f151163f58d03cf83c4
URL:		http://search.cpan.org/dist/Net-SCP/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Net-SSH
BuildRequires:	perl-String-ShellQuote
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Simple wrappers around ssh and scp commands.

%description -l pl.UTF-8
Proste wrappery dla poleceń ssh i scp.

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
%doc Changes README
%{perl_vendorlib}/Net/*.pm
%{_mandir}/man3/*
