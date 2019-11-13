%define _unpackaged_files_terminate_build 0
%define _rpmdir ./

Summary: Minecraft Launcher
Name: minecraft-launcher
Version: 2.1.9618
Release: 1
License: All rights reserved
URL: https://mojang.com
Group: Amusements/Games
Packager: DarkWav

%description
Minecraft Launcher

%build
cd %{buildroot}/../src
wget https://aur.archlinux.org/cgit/aur.git/plain/minecraft-launcher.desktop?h=minecraft-launcher
mv minecraft-launcher.desktop?h=minecraft-launcher minecraft-launcher.desktop
wget https://launcher.mojang.com/download/minecraft-launcher.svg
wget https://launcher.mojang.com/download/linux/x86_64/minecraft-launcher_%{version}.tar.gz
tar -xf minecraft-launcher_%{version}.tar.gz
cd %{buildroot}
mkdir -p "opt"
mkdir -p "usr/bin"
install -Dm644 "%{buildroot}/../src/minecraft-launcher.svg"    "%{buildroot}/usr/share/icons/hicolor/symbolic/apps/minecraft-launcher.svg"
install -Dm644 "%{buildroot}/../src/minecraft-launcher.desktop"    "%{buildroot}/usr/share/applications/minecraft-launcher.desktop"
cp -Rv "%{buildroot}/../src/minecraft-launcher" "%{buildroot}/opt/%{name}"
ln -s "/opt/%{name}/minecraft-launcher" "%{buildroot}/usr/bin/%{name}"
exit

%files
%{_bindir}/minecraft-launcher
/opt/*
%{_datadir}/*
%pre

%post

%postun

%clean

%changelog
 
 
