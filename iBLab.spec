Summary:	Open source tools for Dallas Semiconductor's iButtons
Summary(pl.UTF-8):	Mające otwarte źródła narzędzia do urządzeń iButton firmy Dallas Semiconductors
Name:		iBLab
Version:	0
%define	snap	061026
Release:	0.20%{snap}.1
License:	BSD-like
Group:		Libraries
Source0:	http://anoncvs.aldigital.co.uk/snapshots/iBLab/%{name}-SNAP-%{snap}.tgz
# Source0-md5:	c10c7686d67909050a0bb06788d9dc2b
Patch0:		%{name}-build.patch
Patch1:		%{name}-ac.patch
URL:		http://anoncvs.aldigital.co.uk/iBLab/
BuildRequires:	autoconf
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
iBLab is (intended to be) a replacement set of open source tools for
accessing and manipulating Dallas Semiconductor's range of 'one touch
memories', commonly known as iButtons.

This package contains some test utilities.

%description -l pl.UTF-8
iBLab to (tworzony) zamiennik o otwartych źródłach narzędzi służących
do dostępu i operacji na urządzeniach Dallas Semiconductors z
"jednodotykową pamięcią", znanych jako iButtons.

Ten pakiet zawiera kilka testowych narzędzi.

%package devel
Summary:	iBLab development library
Summary(pl.UTF-8):	Biblioteka programistyczna iBLab
Group:		Development/Libraries
Requires:	libstdc++-devel

%description devel
iBLab is (intended to be) a replacement set of open source tools for
accessing and manipulating Dallas Semiconductor's range of 'one touch
memories', commonly known as iButtons.

This package contains the development library.

%description devel -l pl.UTF-8
iBLab to (tworzony) zamiennik o otwartych źródłach narzędzi służących
do dostępu i operacji na urządzeniach Dallas Semiconductors z
"jednodotykową pamięcią", znanych jako iButtons.

Ten pakiet zawiera bibliotekę programistyczną.


%prep
%setup -q -n anoncvs.aldigital.co.uk-iBLab
%patch0 -p1
%patch1 -p1

%build
%{__autoconf}
%{__autoheader}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir},%{_bindir}}

cp -p src/libiBLab.a $RPM_BUILD_ROOT%{_libdir}
cp -p src/iBLab{All,Button,InterfaceSerial,TMEX,Trace}.h $RPM_BUILD_ROOT%{_includedir}

install test/iBLab{Reset,IDSingle,Scan,Temperature,TMEXDir,TMEXCopy} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ANNOUNCE COPYRIGHT README
%attr(755,root,root) %{_bindir}/iBLab*

%files devel
%defattr(644,root,root,755)
%{_libdir}/libiBLab.a
%{_includedir}/iBLab*.h
