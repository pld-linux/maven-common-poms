
Summary:	Common poms for maven
Name:		maven-common-poms
Version:	1.0
Release:	0.1
License:	Apache v2.0
Group:		Development/Languages/Java
URL:		http://jpackage.org/
Source0:	http://execve.pl/PLD/%{name}.tar.gz
# Source0-md5:	6b6b9f1b2fcf590d2b82a59bda2f7b6e
Source1:	%{name}-depmap.xml
BuildRequires:	jpackage-utils >= 0:1.7.4
Requires:	jpackage-utils >= 0:1.7.4
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package is a collection of poms required by various maven
dependent packages.

%prep
%setup -q -n %{name}

%install
rm -rf $RPM_BUILD_ROOT

# Map
install -d $RPM_BUILD_ROOT%{_mavendepmapdir}
cp %{SOURCE1} $RPM_BUILD_ROOT%{_mavendepmapdir}/maven2-versionless-depmap.xml

install -d $RPM_BUILD_ROOT%{_javadir}/maven2
install -d $RPM_BUILD_ROOT%{_datadir}/maven2/default_poms
cp -a *.pom $RPM_BUILD_ROOT%{_datadir}/maven2/default_poms

install -d $RPM_BUILD_ROOT%{_javadir}/maven2
ln -s %{_datadir}/maven2/default_poms $RPM_BUILD_ROOT%{_javadir}/maven2

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_mavendepmapdir}/maven2-versionless-depmap.xml
%{_javadir}/maven2
%{_datadir}/maven2
