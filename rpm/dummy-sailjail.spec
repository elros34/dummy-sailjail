Name:       dummy-sailjail

Summary:    Dummy sailjail wrapper
Version:    1.1.18.2
Release:    2
Group:      Qt/Qt
License:    LICENSE
URL:        http://example.org/
Source0:    %{name}-%{version}.tar.bz2
Provides:   sailjail <= %{version}
Conflicts:  sailjail <= %{version}
#Obsoletes:  sailjail <= 1.0.23.1
Requires:   mapplauncherd-booster-browser

%description
Dummy sailjail wrapper


%prep
%setup -q -n %{name}-%{version}

%transfiletriggerin -- /usr/share/applications/
/usr/bin/disable_sailjail_in_desktop.sh $(cat)

%post
/usr/bin/disable_sailjail_in_desktop.sh $(ls /usr/share/applications/*.desktop)


%install
rm -rf %{buildroot}
install -D -m 0755 sailjail %{buildroot}/usr/bin/sailjail
install -D -m 0755 disable_sailjail_in_desktop.sh %{buildroot}/usr/bin/disable_sailjail_in_desktop.sh
mkdir -p %{buildroot}/etc
cp -r systemd/ %{buildroot}/etc/
mkdir -p %{buildroot}/usr/share
cp -r mapplauncherd/ %{buildroot}/usr/share/
mkdir -p %{buildroot}/usr/local/share/
cp -r dbus-1 %{buildroot}/usr/local/share/
ln -s /dev/null %{buildroot}/etc/systemd/user/booster-generic@.service
ln -s /dev/null %{buildroot}/etc/systemd/user/booster-qt5@.service
ln -s /dev/null %{buildroot}/etc/systemd/user/booster-browser@.service
ln -s /dev/null %{buildroot}/etc/systemd/user/booster-silica-qt5@.service
ln -s /dev/null %{buildroot}/etc/systemd/user/booster-silica-media@.service

%files
%defattr(-,root,root,-)
%{_bindir}/*
/etc/systemd/user/
/usr/share/mapplauncherd/
/usr/local/share/dbus-1/
