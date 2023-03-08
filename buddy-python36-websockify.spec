Name:           buddy-python36-websockify
	
Version:        0.11.0
	
Release:        1.0.0%{?dist}
	
Summary:        WSGI based adapter for the Websockets protocol
	
 
	
License:        LGPLv3
	
URL:            https://github.com/novnc/websockify
	
Source0:        https://github.com/novnc/websockify/archive/refs/tags/v%{version}.tar.gz
	
BuildArch:      noarch
	
BuildRequires:  python%{python3_pkgversion}-devel
	
BuildRequires:  python%{python3_pkgversion}-setuptools
	
 
	
Requires:       python%{python3_pkgversion}-setuptools
	
	
 
	
%description
	
Python WSGI based adapter for the Websockets protocol
	
 
	
%package -n buddy-python%{python3_pkgversion}-websockify
	
Summary:        WSGI based adapter for the Websockets protocol
	
%{?python_provide:%python_provide buddy-python%{python3_pkgversion}-websockify}
	
 
	
%description -n buddy-python%{python3_pkgversion}-websockify
	
Python WSGI based adapter for the Websockets protocol
	
 
	
%prep
	
%autosetup -n websockify-%{version} -p1
	
 
	
# TODO: Have the following handle multi line entries
	
sed -i '/setup_requires/d; /install_requires/d; /dependency_links/d' setup.py
	
 
	
%build
		
%py3_build
	
	
%install
	
%py3_install
	
#%%{__python} setup.py install -O1 --skip-build --root %%{buildroot}
	
 
	
rm -Rf %{buildroot}/usr/share/websockify
	
mkdir -p %{buildroot}%{_mandir}/man1/
	
install -m 444 docs/websockify.1 %{buildroot}%{_mandir}/man1/
	
 
	
 
	
%files -n python%{python3_pkgversion}-websockify
	
%doc LICENSE.txt docs
	
%{_mandir}/man1/websockify.1*
	
%{python3_sitelib}/websockify/*
	
%{python3_sitelib}/websockify-%{version}-py?.?.egg-info
	
%{_bindir}/websockify
	

%changelog
	
* Wed Mar 08 2023 Lillian Kelting <lkelting@uco.edu> - 0.11.0-0.0.1
	
- Initial pull of source	
