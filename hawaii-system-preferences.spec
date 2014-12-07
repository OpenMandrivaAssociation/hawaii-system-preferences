Summary:	Hawaii system preferences
Name:		hawaii-system-preferences
Version:	0.3.0
Release:	2
License:	GPLv2+
Group:		Graphical desktop/Other
URL:		http://www.maui-project.org
Source0:	http://downloads.sourceforge.net/project/mauios/hawaii/%{name}/%{name}-%{version}.tar.gz
Source1:	hawaii-system-preferences.rpmlintrc
BuildRequires:	cmake
BuildRequires:	qt5-devel
BuildRequires:	cmake(QtConfiguration)
BuildRequires:	cmake(QtAccountsService)
BuildRequires:	cmake(Qt5LinguistTools)
BuildRequires:	pkgconfig(polkit-qt5-1)
BuildRequires:	libhawaii-devel

%track
prog %{name} = {
    url = http://downloads.sourceforge.net/project/mauios/hawaii/
    regex = "%{name}-(__VER__)\.tar\.gz"
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
%dir %{_datadir}/hawaii/preferences
%dir %{_datadir}/hawaii-system-preferences
%dir %{_datadir}/hawaii-system-preferences/translations
%dir %{_datadir}/hawaii/preferences/org.hawaii.preferences.background
%dir %{_datadir}/hawaii/preferences/org.hawaii.preferences.desktop
%dir %{_datadir}/hawaii/preferences/org.hawaii.preferences.keyboard
%dir %{_datadir}/hawaii/preferences/org.hawaii.preferences.network
%{_bindir}/hawaii-system-preferences
%{_libdir}/hawaii/qml/Hawaii/SystemPreferences/Background/libbackgroundplugin.so
%{_libdir}/hawaii/qml/Hawaii/SystemPreferences/Background/qmldir
%{_datadir}/applications/hawaii-*.desktop
%{_datadir}/hawaii/preferences/org.hawaii.preferences.background/*
%{_datadir}/hawaii/preferences/org.hawaii.preferences.desktop/*
%{_datadir}/hawaii/preferences/org.hawaii.preferences.keyboard/*
%{_datadir}/hawaii/preferences/org.hawaii.preferences.network/*
%{_datadir}/hawaii-system-preferences/translations/*.qm
