%define major 0
%define libname %mklibname HawaiiSystemPreferences %{major}
%define develname %mklibname HawaiiSystemPreferences -d

Summary:	Hawaii system preferences
Name:		hawaii-system-preferences
Version:	0.3.0
Release:	1
License:	GPLv2+
Group:		Graphical desktop/Other
URL:		http://www.maui-project.org
Source0:	http://downloads.sourceforge.net/project/mauios/hawaii/%{name}/%{name}-%{version}.tar.gz
Source1:	hawaii-system-preferences.rpmlintrc
Requires:	%{libname} = %{EVRD}
BuildRequires:	cmake
BuildRequires:	qt5-devel
BuildRequires:	cmake(QtConfiguration)
BuildRequires:	cmake(QtAccountsService)
BuildRequires:	cmake(Qt5LinguistTools)
BuildRequires:	cmake(PolkitQt-1)

%track
prog %{name} = {
    url = http://downloads.sourceforge.net/project/mauios/hawaii/
    regex = "%{name}-(__VER__)\.tar\.gz"
    version = %{version}
}

%description
Hawaii system preferences.

%package -n %{libname}
Summary:	Main library for %{name}
Group:		System/Libraries

%description -n %{libname}
Main library for %{name}.

%package -n %{develname}
Summary:	Development files for %{name}
Group:		Development/C++
Requires:	%{libname} = %{EVRD}

%description -n %{develname}
Development files and headers for %{name}.

%prep
%setup -q

%build
%cmake
%make

%install
%makeinstall_std -C build

%files
%{_bindir}/hawaii-system-preferences
%{_libdir}/hawaii/plugins/preferences/*.so
%{_datadir}/applications/*.desktop
%{_datadir}/hawaii-system-preferences/plugins/desktop/translations/*.qm
%{_datadir}/hawaii-system-preferences/plugins/background/translations/*.qm
%{_datadir}/hawaii-system-preferences/translations/*.qm

%files -n %{libname}
%{_libdir}/libHawaiiSystemPreferences.so.%{major}*

%files -n %{develname}
%{_includedir}/Hawaii/SystemPreferences/PreferencesModule
%{_includedir}/Hawaii/SystemPreferences/PreferencesModulePlugin
%{_includedir}/Hawaii/SystemPreferences/SystemPreferencesExport
%{_includedir}/Hawaii/SystemPreferences/*.h
%{_libdir}/libHawaiiSystemPreferences.so
