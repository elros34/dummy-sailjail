Name:       dummy-sailjail

Summary:    Dummy sailjail wrapper
Version:    1.1.12.1
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

%filetriggerin -- /usr/share/applications/
for desktopFile in $(cat); do
    if grep -q "\[X-Sailjail\]" $desktopFile && ! grep -q "^Sandboxing=Disabled" $desktopFile; then
        echo "Disabling sailjail in: $desktopFile"
        sed -i '/^\[X-Sailjail\]/a Sandboxing=Disabled' $desktopFile || true
    fi
done


%install
rm -rf %{buildroot}
install -D -m 0755 sailjail %{buildroot}/usr/bin/sailjail
mkdir -p %{buildroot}/etc
cp -r systemd/ %{buildroot}/etc/
mkdir -p %{buildroot}/usr/share
cp -r mapplauncherd/ %{buildroot}/usr/share/
mkdir -p %{buildroot}/usr/local/share/
cp -r dbus-1 %{buildroot}/usr/local/share/
ln -s /dev/null %{buildroot}/etc/systemd/user/booster-generic@.service
ln -s /dev/null %{buildroot}/etc/systemd/user/booster-qt5@.service
ln -s /dev/null %{buildroot}/etc/systemd/user/booster-browser@.service
ln -s /dev/null %{buildroot}/etc/systemd/user/booster-silica-media@.service

%files
%defattr(-,root,root,-)
%{_bindir}/sailjail
/etc/systemd/user/
/usr/share/mapplauncherd/
/usr/local/share/dbus-1/
