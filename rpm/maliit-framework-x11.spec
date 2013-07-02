Name:       maliit-framework-x11

Summary:    Core libraries of Maliit and server (X11 environment)
Version:    0.99.0
Release:    1
Group:      System/Libraries
License:    LGPLv2.1
URL:        http://gitorious.org/maliit/maliit-framework
Source0:    %{name}-%{version}.tar.bz2
Source1:    maliit-server.sh
Source2:    maliit-server.service-x11
Patch0:     enable-systemd-activation.patch
Requires:   dbus-x11
Requires:   maliit-framework-x11-inputcontext
Requires:   qt5-qtdeclarative-import-qtquick2plugin
Requires:   qt5-plugin-platform-xcb
Requires:   systemd-user-session-targets
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcomposite)
BuildRequires:  pkgconfig(xdamage)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  fdupes
Provides:   maliit-framework > 0.99.0
Conflicts:   maliit-framework-wayland
Obsoletes:   libmaliit-quick
Obsoletes:   maliit-framework <= 0.99.0

%description
Core libraries of Maliit and server


%package inputcontext
Summary:    Qt5 plugin for connecting to Maliit input method server
Group:      System/Libraries
Requires:   %{name} = %{version}-%{release}
Provides:   qt5-plugin-platform-inputcontext-maliit
Obsoletes:  qt5-plugin-platform-inputcontext-maliit
Obsoletes:  maliit-framework-inputcontext

%description inputcontext
This package contains loadable plugin for Qt5 which allows to connect
to Maliit input method server


%package devel
Summary:    Maliit Framework Input Method Development Package
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
This package contains the files necessary to develop
input method plugins using Maliit


%package doc
Summary:    Maliit Framework Documentation
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description doc
Documentation for the Maliit Input Method Framework

%package examples
Summary:    Maliit Framework Input Method Examples
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description examples
This package contains examples applications for
the Maliit input method framework


%package tests
Summary:    Maliit Framework Input Method Tests Package
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description tests
This package contains the files necessary to test
the Maliit input method framework


%prep
%setup -q -n %{name}-%{version}/maliit-framework

# enable-systemd-activation.patch
%patch0 -p1

%build

%qmake5  \
    CONFIG+=enable-dbus-activation \
    CONFIG+=qt5-inputcontext

make %{?jobs:-j%jobs}


%install
rm -rf %{buildroot}
%qmake_install
install -D -m 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/profile.d/maliit-server.sh
install -D -m 0644 %{SOURCE2} %{buildroot}%{_libdir}/systemd/user/maliit-server.service
mkdir -p %{buildroot}%{_libdir}/systemd/user/user-session.target.wants
ln -s ../maliit-server.service %{buildroot}%{_libdir}/systemd/user/user-session.target.wants/

%fdupes  %{buildroot}/%{_libdir}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_bindir}/maliit-server
%{_libdir}/libmaliit-plugins.so*
%{_datadir}/dbus-1/services/org.maliit.server.service
%config %{_sysconfdir}/profile.d/maliit-server.sh
%{_libdir}/systemd/user/maliit-server.service
%{_libdir}/systemd/user/user-session.target.wants/maliit-server.service

%files inputcontext
%defattr(-,root,root,-)
%{_libdir}/qt5/plugins/platforminputcontexts/*.so

%files devel
%defattr(-,root,root,-)
%{_includedir}/maliit/*
%{_libdir}/pkgconfig/*.pc
%{_datadir}/qt5/mkspecs/features/*

%files doc
%defattr(-,root,root,-)
%{_docdir}/maliit-framework/html

%files examples
%defattr(-,root,root,-)
%{_bindir}/maliit-exampleapp-plainqt

%files tests
%defattr(-,root,root,-)
%{_libdir}/maliit-framework-tests/

