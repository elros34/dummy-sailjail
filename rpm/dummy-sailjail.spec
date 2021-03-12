Name:       dummy-sailjail

Summary:    Dummy sailjail wrapper
Version:    1.0.23.1
Release:    3
Group:      Qt/Qt
License:    LICENSE
URL:        http://example.org/
Source0:    %{name}-%{version}.tar.bz2
Provides:   sailjail = 1.0.23.1
Conflicts:  sailjail = 1.0.23.1
#Obsoletes:  sailjail <= 1.0.23.1
Requires:   mapplauncherd-booster-browser

%description
Dummy sailjail wrapper


%prep
%setup -q -n %{name}-%{version}

%install
rm -rf %{buildroot}
install -D -m 0755 sailjail %{buildroot}/usr/bin/sailjail
mkdir -p %{buildroot}/etc
cp -r systemd/ %{buildroot}/etc/
mkdir -p %{buildroot}/usr/share
cp -r mapplauncherd/ %{buildroot}/usr/share/
mkdir -p %{buildroot}/usr/local/share/
cp -r dbus-1 %{buildroot}/usr/local/share/

%files
%defattr(-,root,root,-)
%{_bindir}/sailjail
/etc/systemd/user/
/usr/share/mapplauncherd/
/usr/local/share/dbus-1/
