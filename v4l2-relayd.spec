%global commit 2e4d5c9ba53bfe8cfe16ea91932c8e5ecb090a87
%global commitdate 20220126 
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           v4l2-relayd
Summary:        Utils for relaying the video stream between two video devices
Version:        0.1.2
Release:        5.%{commitdate}git%{shortcommit}%{?dist}
License:        GPL-2.0-only

Source0:        https://gitlab.com/vicamo/v4l2-relayd//-/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
Source1:        v4l2-relayd-tgl
Source2:        v4l2-relayd-adl
Source3:        60-ipu6-v4l2-relayd.rules

Patch0:         0001-Set-a-new-ID-offset-for-the-private-event.patch

BuildRequires:  systemd-rpm-macros
BuildRequires:  gcc
BuildRequires:  g++
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  glib2-devel
BuildRequires:  gstreamer1-devel
BuildRequires:  gstreamer1-plugins-base-devel
BuildRequires:  systemd

Requires:       v4l2loopback

%description
This is used to relay the input GStreamer source to an output GStreamer
source or a V4L2 device.

%prep
%autosetup -p1 -n %{name}-%{commit}
autoreconf --force --install --verbose 

%build
%configure
%make_build

%install
%make_install modprobedir=%{_modprobedir}
ln -sf /run/v4l2-relayd %{buildroot}%{_sysconfdir}/default/v4l2-relayd
install -p -D -m 0644 %{SOURCE1} %{buildroot}%{_datadir}/defaults/etc/ipu6/v4l2-relayd
install -p -D -m 0644 %{SOURCE2} %{buildroot}%{_datadir}/defaults/etc/ipu6ep/v4l2-relayd
install -p -D -m 0644 data/etc/modprobe.d/v4l2-relayd.conf %{buildroot}%{_modprobedir}
install -p -D -m 0644 data/etc/modules-load.d/v4l2-relayd.conf %{buildroot}%{_modulesloaddir}
install -p -D -m 0644 data/systemd/v4l2-relayd.service %{buildroot}%{_unitdir}
install -p -D -m 0644 %{SOURCE3} %{buildroot}%{_udevrulesdir}/60-ipu6-v4l2-relayd.rules

%files
%license LICENSE
%{_bindir}/v4l2-relayd
%{_sysconfdir}/default/v4l2-relayd
%{_modprobedir}/v4l2-relayd.conf
%{_modulesloaddir}/v4l2-relayd.conf
%{_unitdir}/v4l2-relayd.service
%{_datadir}/defaults
%{_udevrulesdir}/60-ipu6-v4l2-relayd.rules

%changelog
* Tue Mar 14 2023 Kate Hsuan <hpa@redhat.com> - 0.1.2-5.20220126git2e4d5c9
- Configuration files for Tiger and Alder lake platforms
- udev rules for config file selection

* Tue Feb 21 2023 Kate Hsuan <hpa@redhat.com> - 0.1.2-4.20220126git2e4d5c9
- New private event ID

* Thu Feb 16 2023 Kate Hsuan <hpa@redhat.com> - 0.1.2-3.20220126git2e4d5c9
- Update build and installation scripts

* Thu Jan 12 2023 Kate Hsuan <hpa@redhat.com> - 0.1.2-2.20220126git2e4d5c9
- Add "Requires: v4l2loopback"

* Thu Dec 15 2022 Kate Hsuan <hpa@redhat.com> - 0.1.2-1.20220126git2e4d5c9
- First commit

