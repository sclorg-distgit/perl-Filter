%{?scl:%scl_package perl-Filter}
%{!?scl:%global pkg_name %{name}}

Name:           %{?scl_prefix}perl-Filter
Epoch:          1
Version:        1.49
Release:        3.sc1%{?dist}
Summary:        Perl source filters
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Filter/
Source0:        http://www.cpan.org/modules/by-module/Filter/Filter-%{version}.tar.gz
BuildRequires:  %{?scl_prefix}perl
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MakeMaker)
BuildRequires:  %{?scl_prefix}perl(Getopt::Long)
BuildRequires:  %{?scl_prefix}perl(strict)
# Run-time
BuildRequires:  %{?scl_prefix}perl(Carp)
BuildRequires:  %{?scl_prefix}perl(Config)
BuildRequires:  %{?scl_prefix}perl(DynaLoader)
BuildRequires:  %{?scl_prefix}perl(Exporter)
BuildRequires:  %{?scl_prefix}perl(vars)
BuildRequires:  %{?scl_prefix}perl(warnings)
# Tests
BuildRequires:  %{?scl_prefix}perl(Cwd)
BuildRequires:  %{?scl_prefix}perl(Test::More)
# Optional tests
BuildRequires:  %{?scl_prefix}perl(POSIX)
%if !%{defined perl_bootstrap}
BuildRequires:  %{?scl_prefix}perl(Test::Pod) >= 1.00
%endif
%{?scl:%global perl_version %(scl enable %{scl} 'eval "`perl -V:version`"; echo $version')}
%{!?scl:%global perl_version %(eval "`perl -V:version`"; echo $version)}
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%{perl_version})

%if ( 0%{?rhel} && 0%{?rhel} < 7 )
%global our_docdir %%{?_pkgdocdir}%%{!?_pkgdocdir:%%{_docdir}/%%{?scl:%%{name}}%%{!?scl:%%{pkg_name}}-%%{version}}
%filter_from_provides /\.so()/d
%filter_requires_in %{our_docdir}
%filter_provides_in %{our_docdir}
%filter_setup
%endif

%{?perl_default_filter}

%description
Source filters alter the program text of a module before Perl sees it, much as
a C preprocessor alters the source text of a C program before the compiler
sees it.

%prep
%setup -q -n Filter-%{version}
# Clean examples
find examples -type f -exec chmod -x -- {} +
sed -i -e '1 s|.*|#!%{__perl}|' examples/filtdef

%build
%{?scl:scl enable %{scl} '}
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
%{?scl:'}
%{?scl:scl enable %{scl} "}
make %{?_smp_mflags}
%{?scl:"}

%install
%{?scl:scl enable %{scl} "}
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{?scl:"}
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{?scl:scl enable %{scl} "}
make test
%{?scl:"}

%files
%doc examples Changes README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Filter*
%{_mandir}/man3/*

%changelog
* Tue Dec 03 2013 Jitka Plesnikova <jplesnik@redhat.com> - 1:1.49-3
- Filter dependencies from docdir
- Resolves: rhbz#1037448

* Tue Nov 12 2013 Jitka Plesnikova <jplesnik@redhat.com> - 1:1.49-2
- Increase epoch to compete with perl.spec

* Mon May 20 2013 Jitka Plesnikova <jplesnik@redhat.com> - 1.49-1
- 1.49 bump

* Tue Feb 12 2013 Jitka Plesnikova <jplesnik@redhat.com> - 1.45-1
- Stack package - initial release
