%include	/usr/lib/rpm/macros.perl
Summary:	Counts bibliography entries by type
Name:		bibcount
Version:	0.1
Release:	0.9
License:	???
Group:		Applications
Source0:	http://www.ecst.csuchico.edu/~jacobsd/bib/archives/%{name}
# Source0-md5:	6ef4985c4e5fbd5780c6d186c17add08
URL:		http://www.ecst.csuchico.edu/~jacobsd/bib/tools/bibtex.html
BuildRequires:	perl-base
BuildRequires:	rpm-perlprov
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Counts bibliography entries by type

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install %{SOURCE0} $RPM_BUILD_ROOT%{_bindir}
sed -i -e 's#/usr/local/bin/perl#/usr/bin/perl#' $RPM_BUILD_ROOT%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
