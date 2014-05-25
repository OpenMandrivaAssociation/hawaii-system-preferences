Summary:	Hawaii system preferences
Name:		hawaii-system-preferences
Version:	0.2.0
Release:	1
License:	GPLv2+
Group:		Graphical desktop/Other
URL:		http://www.maui-project.org
Source0:	http://downloads.sourceforge.net/project/mauios/hawaii/%{name}/%{name}-%{version}.tar.gz
BuildRequires:	cmake
BuildRequires:	qt5-devel
BuildRequires:	cmake(Qtconfiguration)
BuildRequires:	cmake(Qtaccountsservice)
BuildRequires:	polkit-qt5-1-devel
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

%prep
%setup -q

%build
%cmake
%make

%install
%makeinstall_std -C build

%files
