%define snap 20150516

Summary:	Hawaii system preferences
Name:		hawaii-system-preferences
Version:	0.4.0
Release:	0.%{snap}.1
License:	GPLv2+
Group:		Graphical desktop/Other
URL:		https://hawaii-desktop.github.io
# git archive --format=tar --prefix=hawaii-system-preferences-0.4.0-$(date +%Y%m%d)/ HEAD | xz -vf > hawaii-system-preferences-0.4.0-$(date +%Y%m%d).tar.xz
Source0:	https://github.com/hawaii-desktop/hawaii-desktop/archive/%{name}-%{version}-%{snap}.tar.xz
#Source0:	https://github.com/hawaii-desktop/hawaii-desktop/archive/%{name}-%{version}.tar.gz
Source1:	hawaii-system-preferences.rpmlintrc
BuildRequires:	cmake
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
    url = https://github.com/hawaii-desktop/%{name}/archive/
    regex = "v(__VER__)\.tar\.gz"
    version = %{version}
}

%description
Hawaii system preferences.

%prep
%setup -qn %{name}-%{version}-%{snap}

%build
%cmake_qt5
%make

%install
%makeinstall_std -C build

%files
%dir %{_datadir}/hawaii-system-preferences
%dir %{_datadir}/hawaii-system-preferences/shells
%dir %{_datadir}/hawaii-system-preferences/modules
%dir %{_datadir}/hawaii-system-preferences/modules/hawaii
%dir %{_datadir}/hawaii-system-preferences/shells/org.hawaii.systempreferences
%dir %{_datadir}/hawaii-system-preferences/modules/hawaii/org.hawaii.systempreferences.background
%dir %{_datadir}/hawaii-system-preferences/modules/hawaii/org.hawaii.systempreferences.display
%dir %{_datadir}/hawaii-system-preferences/modules/hawaii/org.hawaii.systempreferences.keyboard
%dir %{_datadir}/hawaii-system-preferences/translations
%{_bindir}/hawaii-system-preferences
%{_libdir}/qml/org/hawaii/systempreferences/background/libbackgroundplugin.so
%{_libdir}/qml/org/hawaii/systempreferences/background/qmldir
%{_libdir}/qml/org/hawaii/systempreferences/display/libdisplayplugin.so
%{_libdir}/qml/org/hawaii/systempreferences/display/qmldir
%{_libdir}/qml/org/hawaii/systempreferences/keyboard/libkeyboardplugin.so
%{_libdir}/qml/org/hawaii/systempreferences/keyboard/qmldir
%{_datadir}/applications/*.desktop
%{_datadir}/hawaii-system-preferences/modules/hawaii/org.hawaii.systempreferences.background/*.qml
%{_datadir}/hawaii-system-preferences/modules/hawaii/org.hawaii.systempreferences.background/metadata.desktop
%{_datadir}/hawaii-system-preferences/modules/hawaii/org.hawaii.systempreferences.display/*.qml
%{_datadir}/hawaii-system-preferences/modules/hawaii/org.hawaii.systempreferences.display/metadata.desktop
%{_datadir}/hawaii-system-preferences/modules/hawaii/org.hawaii.systempreferences.keyboard/*.qml
%{_datadir}/hawaii-system-preferences/modules/hawaii/org.hawaii.systempreferences.keyboard/metadata.desktop
%{_datadir}/hawaii-system-preferences/shells/org.hawaii.systempreferences/*.qml
%{_datadir}/hawaii-system-preferences/translations/*.qm
