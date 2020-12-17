%define _unpackaged_files_terminate_build 0
%define _rpmdir ./

Summary: Video DownloadHelper Companion App
Name: net.downloadhelper.coapp
Version: 1.6.0
URL: https://www.downloadhelper.net/install-coapp
Release: 1
Packager: DarkWav
License: GGPLv3

%description
Video DownloadHelper Companion App

%build
cd %{buildroot}/../src
wget https://github.com/mi-g/vdhcoapp/releases/download/v%{version}/%{name}-%{version}-%{release}_amd64.deb
ar x ./%{name}-%{version}-%{release}_amd64.deb
tar -xf data.tar.gz
cd %{buildroot}
mkdir -p ./usr
cp -R ../src/usr/lib ./usr/lib
cp -R ../src/usr/lib ./usr/lib64
cp -R ../src/opt ./opt
cp -R ../src/etc ./etc
exit

%files
%{_libdir}/*
%{_usr}/lib/*
/opt/*
%{_sysconfdir}/*
%pre

%post

ln -s /usr/lib64/libaom.so.2 /usr/lib64/libaom.so.0

%postun

%clean

%changelog

