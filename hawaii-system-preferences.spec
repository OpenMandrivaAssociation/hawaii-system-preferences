Summary:	Hawaii system preferences
Name:		hawaii-system-preferences
Version:	0.6.90
Release:	1
License:	GPLv2+
Group:		Graphical desktop/Other
URL:		http://www.hawaiios.org
# git archive --format=tar --prefix=hawaii-system-preferences-0.4.0-$(date +%Y%m%d)/ HEAD | xz -vf > hawaii-system-preferences-0.4.0-$(date +%Y%m%d).tar.xz
#Source0:	https://github.com/hawaii-desktop/hawaii-desktop/archive/%{name}-%{version}-%{snap}.tar.xz
Source0:	https://github.com/hawaii-desktop/hawaii-system-preferences/releases/download/v%{version}/%{name}-%{version}.tar.gz
Source1:	hawaii-system-preferences.rpmlintrc
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5Qml)
BuildRequires:	cmake(Qt5Quick)
BuildRequires:	cmake(Qt5LinguistTools)
BuildRequires:  cmake(KF5Screen)
BuildRequires:	pkgconfig(polkit-qt5-1)

%track
prog %{name} = {
    url = https://github.com/hawaii-desktop/hawaii-system-preferences/releases/download/v%{version}
    regex = "v(__VER__)\.tar\.xz"
    version = %{version}
}

%description
Hawaii system preferences.

%prep
%setup -q

%build
%cmake_qt5
%make

%install
%makeinstall_std -C build

%files
%dir %{_libdir}/qml/org.hawaiios/systempreferences
%dir %{_datadir}/hawaii-system-preferences
%dir %{_datadir}/hawaii-system-preferences/modules
%dir %{_datadir}/hawaii-system-preferences/shells
%{_bindir}/hawaii-system-preferences
%{_libdir}/qml/org.hawaiios/systempreferences/*
%{_datadir}/applications/*.desktop
%{_datadir}/hawaii-system-preferences/modules/hawaii
%{_datadir}/hawaii-system-preferences/shells/org.hawaiios.systempreferences
