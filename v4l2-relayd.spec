%global commit 2e4d5c9ba53bfe8cfe16ea91932c8e5ecb090a87
%global commitdate 20220126 
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           v4l2-relayd
Summary:        Utils for relaying the video stream between two video devices
Version:        0.1.2
Release:        9.%{commitdate}git%{shortcommit}%{?dist}
License:        GPL-2.0-only

Source0:        https://gitlab.com/vicamo/v4l2-relayd//-/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
Source1:        v4l2-relayd.preset

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
sed -i '/^EnvironmentFile=\/etc\/default\/v4l2-relayd/a EnvironmentFile=-\/run\/v4l2-relayd' %{buildroot}%{_unitdir}/v4l2-relayd.service
install -p -D -m 0644 %{SOURCE1} %{buildroot}%{_presetdir}/95-v4l2-relayd.preset

%post
%systemd_post v4l2-relayd.service

%preun
%systemd_preun v4l2-relayd.service

%postun
%systemd_postun_with_restart v4l2-relayd.service

%files
%license LICENSE
%{_bindir}/v4l2-relayd
%{_sysconfdir}/default/v4l2-relayd
%{_modprobedir}/v4l2-relayd.conf
%{_modulesloaddir}/v4l2-relayd.conf
%{_unitdir}/v4l2-relayd.service
%{_presetdir}/95-v4l2-relayd.preset

%changelog
* Fri Apr 7 2023 Kate Hsuan <hpa@redhat.com> - 0.1.2-9.20220126git2e4d5c9
- Removed unnecessary install command

* Thu Mar 23 2023 Kate Hsuan <hpa@redhat.com> - 0.1.2-8.20220126git2e4d5c9
- Drop the symbolic link of the environment file
- Add EnvironmentFile setting for /run/v4l2-relayd

* Wed Mar 22 2023 Kate Hsuan <hpa@redhat.com> - 0.1.2-7.20220126git2e4d5c9
- systemd post scripts
- removed configuration examples

* Mon Mar 20 2023 Kate Hsuan <hpa@redhat.com> - 0.1.2-6.20220126git2e4d5c9
- remove udev rules

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

