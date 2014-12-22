Name:           ros-indigo-libpointmatcher
Version:        1.2.2
Release:        0%{?dist}
Summary:        ROS libpointmatcher package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

ExclusiveArch:  x86_64

Requires:       boost-devel
Requires:       eigen3-devel
Requires:       ros-indigo-catkin
Requires:       ros-indigo-libnabo
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  eigen3-devel
BuildRequires:  ros-indigo-libnabo

%description
libpointmatcher is a modular ICP library, useful for robotics and computer
vision.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Sun Dec 21 2014 Francois Pomerleau <f.pomerleau@gmail.com> - 1.2.2-0
- Autogenerated by Bloom

