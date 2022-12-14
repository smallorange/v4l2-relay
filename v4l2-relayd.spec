%global commit 2e4d5c9ba53bfe8cfe16ea91932c8e5ecb090a87
%global commitdate 20220126 
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           v4l2-relayd
Summary:        Utils for relaying Gstreamer source to any other Gstreamer source.
Version:        0.1.2
Release:        1.%{commitdate}git%{shortcommit}%{?dist}
License:        GPLv2

Source:         https://gitlab.com/vicamo/v4l2-relayd//-/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

BuildRequires:  systemd-rpm-macros
BuildRequires:  gcc
BuildRequires:  g++
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  glib
BuildRequires:  glib-devel
BuildRequires:  gstreamer1-devel
BuildRequires:  gstreamer1-plugins-base-devel

Requires:       glib2
Requires:       gstreamer1
Requires:       gstreamer1-plugins-base

%description
This is used to relay the input Gstreamer source to an output Gstreamer source.

%prep

%autosetup -n %{name}-%{commit}

%build
./autogen.sh
export CFLAGS="${RPM_OPT_FLAGS}"
export CXXFLAGS="${RPM_OPT_FLAGS}"
echo $CFLAGS
make -j`nproc`

%install
mkdir -p %{buildroot}%{_bindir}
install -p -D -m 0755 src/v4l2-relayd %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_sysconfdir}/default
mkdir -p %{buildroot}%{_sysconfdir}/modprobe.d
mkdir -p %{buildroot}%{_sysconfdir}/modules-load.d
install -p -D -m 0644 data/etc/default/v4l2-relayd %{buildroot}%{_sysconfdir}/default
install -p -D -m 0644 data/etc/modprobe.d/v4l2-relayd.conf %{buildroot}%{_sysconfdir}/modprobe.d
install -p -D -m 0644 data/etc/modules-load.d/v4l2-relayd.conf %{buildroot}%{_sysconfdir}/modules-load.d
mkdir -p %{buildroot}/usr/lib/systemd
install -p -D -m 0644 data/systemd/v4l2-relayd.service %{buildroot}/usr/lib/systemd

%files
%license LICENSE
%{_bindir}/v4l2-relayd
%dir %{_sysconfdir}/default
%dir %{_sysconfdir}/modprobe.d
%dir %{_sysconfdir}/modules-load.d
%{_sysconfdir}/default/v4l2-relayd
%{_sysconfdir}/modprobe.d/v4l2-relayd.conf
%{_sysconfdir}/modules-load.d/v4l2-relayd.conf
%dir /usr/lib/systemd
/usr/lib/systemd/v4l2-relayd.service

%changelog
* Tue Nov 29 2022 Kate Hsuan <hpa@redhat.com> - 0.0-1.20220926git3b7cdb9
- First commit



