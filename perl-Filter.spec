%{?scl:%scl_package perl-Filter}

# Run optional test
%if ! (0%{?rhel}) && ! (0%{?scl:1})
%bcond_without perl_Filter_enables_optional_test
%else
%bcond_with perl_Filter_enables_optional_test
%endif

Name:           %{?scl_prefix}perl-Filter
Epoch:          2
Version:        1.59
Release:        452%{?dist}
Summary:        Perl source filters
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Filter
Source0:        https://cpan.metacpan.org/authors/id/R/RU/RURBAN/Filter-%{version}.tar.gz
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  %{?scl_prefix}perl-devel
BuildRequires:  %{?scl_prefix}perl-generators
BuildRequires:  %{?scl_prefix}perl-interpreter
BuildRequires:  %{?scl_prefix}perl(Config)
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  %{?scl_prefix}perl(Getopt::Long)
BuildRequires:  %{?scl_prefix}perl(strict)
BuildRequires:  sed
# Run-time
BuildRequires:  %{?scl_prefix}perl(:VERSION) >= 5.6
BuildRequires:  %{?scl_prefix}perl(Carp)
BuildRequires:  %{?scl_prefix}perl(Exporter)
BuildRequires:  %{?scl_prefix}perl(warnings)
BuildRequires:  %{?scl_prefix}perl(XSLoader)
# Tests
BuildRequires:  %{?scl_prefix}perl(Cwd)
BuildRequires:  %{?scl_prefix}perl(FindBin)
BuildRequires:  %{?scl_prefix}perl(lib)
BuildRequires:  %{?scl_prefix}perl(Test::More) >= 0.88
%if %{with perl_Filter_enables_optional_test}
# Optional tests
BuildRequires:  m4
BuildRequires:  %{?scl_prefix}perl(POSIX)
%if !%{defined perl_bootstrap}
# Class::XSAccessor not used
# List::MoreUtils not used
# Perl::MinimumVersion 1.20 not used
# Test::CPAN::Meta 0.12 not used
# Test::Kwalitee not used
# Test::MinimumVersion 0.008 not used
BuildRequires:  %{?scl_prefix}perl(Test::Pod) >= 1.00
# Test::Pod::Coverage 1.04 not used
# Text::CSV_XS not used
%endif
BuildRequires:  %{?scl_prefix}perl(vars)
%endif
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%(%{?scl:scl enable %{scl} '}eval "$(perl -V:version)";echo $version%{?scl:'}))
Requires:       %{?scl_prefix}perl(Carp)

%{?perl_default_filter}

%description
Source filters alter the program text of a module before Perl sees it, much as
a C preprocessor alters the source text of a C program before the compiler
sees it.

%prep
%setup -q -n Filter-%{version}
# Clean examples
find examples -type f -exec chmod -x -- {} +
sed -i -e '1 s|.*|%(%{?scl:scl enable %{scl} '}perl -MConfig -e %{?scl:'"}'%{?scl:"'}print $Config{startperl}%{?scl:'"}'%{?scl:"'}%{?scl:'})|' \
    examples/filtdef

%build
%{?scl:scl enable %{scl} '}perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 OPTIMIZE="$RPM_OPT_FLAGS" && make %{?_smp_mflags}%{?scl:'}

%install
%{?scl:scl enable %{scl} '}make pure_install DESTDIR=$RPM_BUILD_ROOT%{?scl:'}
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{?scl:scl enable %{scl} '}make test%{?scl:'}

%files
%doc examples Changes README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Filter*
%{_mandir}/man3/*

%changelog
* Tue Jan 07 2020 Jitka Plesnikova <jplesnik@redhat.com> - 2:1.59-452
- Re-rebuild of bootstrapped packages

* Fri Dec 20 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2:1.59-451
- SCL

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2:1.59-440
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 02 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2:1.59-439
- Perl 5.30 re-rebuild of bootstrapped packages

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2:1.59-438
- Increase release to favour standalone package

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2:1.59-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Aug 06 2018 Petr Pisar <ppisar@redhat.com> - 2:1.59-1
- 1.59 bump

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2:1.58-418
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2:1.58-417
- Perl 5.28 re-rebuild of bootstrapped packages

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2:1.58-416
- Increase release to favour standalone package

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2:1.58-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Nov 16 2017 Petr Pisar <ppisar@redhat.com> - 2:1.58-1
- 1.58 bump

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2:1.57-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2:1.57-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 07 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2:1.57-4
- Perl 5.26 re-rebuild of bootstrapped packages

* Sat Jun 03 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2:1.57-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2:1.57-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 23 2017 Petr Pisar <ppisar@redhat.com> - 2:1.57-1
- 1.57 bump

* Wed May 18 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2:1.55-366
- Perl 5.24 re-rebuild of bootstrapped packages

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2:1.55-365
- Increase release to favour standalone package

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2:1.55-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jul 27 2015 Petr Pisar <ppisar@redhat.com> - 2:1.55-1
- 1.55 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2:1.54-347
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 10 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2:1.54-346
- Perl 5.22 re-rebuild of bootstrapped packages

* Thu Jun 04 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2:1.54-345
- Increase release to favour standalone package

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2:1.54-2
- Perl 5.22 rebuild

* Fri Jan 23 2015 Petr Pisar <ppisar@redhat.com> - 2:1.54-1
- 1.54 bump

* Fri Jan 02 2015 Petr Pisar <ppisar@redhat.com> - 2:1.53-1
- 1.53 bump

* Thu Dec 11 2014 Petr Pisar <ppisar@redhat.com> - 2:1.51-1
- 1.51 bump

* Sun Sep 07 2014 Jitka Plesnikova <jplesnik@redhat.com> - 2:1.50-6
- Perl 5.20 re-rebuild of bootstrapped packages

* Wed Sep 03 2014 Jitka Plesnikova <jplesnik@redhat.com> - 2:1.50-5
- Increase Epoch to favour standalone package

* Tue Aug 26 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1:1.50-4
- Perl 5.20 rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.50-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.50-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Jun 05 2014 Petr Pisar <ppisar@redhat.com> - 1:1.50-1
- 1.50 bump

* Wed Aug 14 2013 Jitka Plesnikova <jplesnik@redhat.com> - 1:1.49-5
- Perl 5.18 re-rebuild of bootstrapped packages

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.49-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jul 12 2013 Petr Pisar <ppisar@redhat.com> - 1:1.49-3
- Link minimal build-root packages against libperl.so explicitly

* Fri Jul 12 2013 Petr Pisar <ppisar@redhat.com> - 1:1.49-2
- Perl 5.18 rebuild

* Fri Jul 12 2013 Petr Pisar <ppisar@redhat.com> - 1:1.49-1
- Increase epoch to compete with perl.spec

* Thu Apr 04 2013 Petr Pisar <ppisar@redhat.com> - 1.49-1
- 1.49 bump

* Wed Apr 03 2013 Petr Pisar <ppisar@redhat.com> - 1.48-1
- 1.48 bump

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.45-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.45-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jul 10 2012 Petr Pisar <ppisar@redhat.com> - 1.45-3
- Perl 5.16 re-rebuild of bootstrapped packages

* Wed Jun 27 2012 Petr Pisar <ppisar@redhat.com> - 1.45-2
- Perl 5.16 rebuild

* Tue Jun 19 2012 Petr Pisar <ppisar@redhat.com> - 1.45-1
- 1.45 bump

* Wed Jun 06 2012 Petr Pisar <ppisar@redhat.com> - 1.43-3
- Perl 5.16 rebuild

* Thu May 31 2012 Petr Pisar <ppisar@redhat.com> - 1.43-2
- Skip optional Test::Pod on bootstraping perl

* Mon Feb 27 2012 Petr Pisar <ppisar@redhat.com> - 1.43-1
- 1.43 bump

* Tue Feb 14 2012 Petr Pisar <ppisar@redhat.com> 1.39-1
- Specfile autogenerated by cpanspec 1.78.
