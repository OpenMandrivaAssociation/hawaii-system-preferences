Summary:	Hawaii system preferences
Name:		hawaii-system-preferences
Version:	0.4.0
Release:	1
License:	GPLv2+
Group:		Graphical desktop/Other
URL:		http://www.maui-project.org
Source0:	http://downloads.sourceforge.net/project/mauios/hawaii/%{name}/%{name}-%{version}.tar.gz
Source1:	hawaii-system-preferences.rpmlintrc
BuildRequires:	cmake
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5Qml)
BuildRequires:	cmake(Qt5Quick)
BuildRequires:	cmake(Qt5LinguistTools)
BuildRequires:	pkgconfig(polkit-qt5-1)

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
%dir %{_datadir}/hawaii-system-preferences
%dir %{_datadir}/hawaii-system-preferences/shells
%dir %{_datadir}/hawaii-system-preferences/modules
%dir %{_datadir}/hawaii-system-preferences/modules/hawaii
%dir %{_datadir}/hawaii-system-preferences/shells/org.hawaii.systempreferences
%dir %{_datadir}/hawaii-system-preferences/modules/hawaii/org.hawaii.systempreferences.background
%dir %{_datadir}/hawaii-system-preferences/modules/hawaii/org.hawaii.systempreferences.keyboard
%{_bindir}/hawaii-system-preferences
%{_libdir}/qml/org/hawaii/systempreferences/background/libbackgroundplugin.so
%{_libdir}/qml/org/hawaii/systempreferences/background/qmldir
%{_libdir}/qml/org/hawaii/systempreferences/keyboard/libkeyboardplugin.so
%{_libdir}/qml/org/hawaii/systempreferences/keyboard/qmldir
%{_datadir}/applications/*.desktop
%{_datadir}/hawaii-system-preferences/modules/hawaii/org.hawaii.systempreferences.background/*.qml
%{_datadir}/hawaii-system-preferences/modules/hawaii/org.hawaii.systempreferences.background/metadata.desktop
%{_datadir}/hawaii-system-preferences/modules/hawaii/org.hawaii.systempreferences.keyboard/*.qml
%{_datadir}/hawaii-system-preferences/modules/hawaii/org.hawaii.systempreferences.keyboard/metadata.desktop
%{_datadir}/hawaii-system-preferences/shells/org.hawaii.systempreferences/*.qml
%{_datadir}/hawaii-system-preferences/translations/*.qm
