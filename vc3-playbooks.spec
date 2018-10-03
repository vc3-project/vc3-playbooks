#%define vers %{getenv:BUILDTAG}
Name: vc3-playbooks

Version: 1.1.0
Release: 1
Summary: Pilot and software installer

License: MIT
URL: https://github.com/vc3-project/vc3-playbooks

# tarball generation:
# ------------------- 
# cd ~/rpmbuild/SOURCES
# git clone --depth=1 https://github.com/vc3-project/vc3-playbooks
# rm -rf vc3-builder/.git*
# tar -cvzf vc3-builder-1.1.0-src.tgz vc3-builder
Source0: vc3-playbooks-1.1.0-src.tgz

BuildArch: noarch
# Requires: 

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}

%description


%prep
%setup -q -n vc3-playbooks

%build

%install
mkdir -p %{buildroot}/%{_sysconfdir}/vc3/vc3-playbooks
cp -r * %{buildroot}/%{_sysconfdir}/vc3/vc3-playbooks
rm -f %{buildroot}/%{_sysconfdir}/vc3/vc3-playbooks/vc3-playbooks.spec

%files
%{_sysconfdir}/vc3/vc3-playbooks/login/login-htcondor.yaml
%{_sysconfdir}/vc3/vc3-playbooks/login/login-jupyter.yaml
%{_sysconfdir}/vc3/vc3-playbooks/login/login-spark.yaml
%{_sysconfdir}/vc3/vc3-playbooks/login/login-workqueue.yaml
%{_sysconfdir}/vc3/vc3-playbooks/login/templates/condor_config.local.j2
%{_sysconfdir}/vc3/vc3-playbooks/login/templates/cvmfs_default_local.j2
%{_sysconfdir}/vc3/vc3-playbooks/login/templates/motd.j2
%{_sysconfdir}/vc3/vc3-playbooks/login/components/builder.yaml
%{_sysconfdir}/vc3/vc3-playbooks/login/components/condor.yaml
%{_sysconfdir}/vc3/vc3-playbooks/login/components/cvmfs.yaml
%{_sysconfdir}/vc3/vc3-playbooks/login/components/host.yaml
%{_sysconfdir}/vc3/vc3-playbooks/login/components/users.yaml
%{_sysconfdir}/vc3/vc3-playbooks/login/config/jupyterhub.service
%{_sysconfdir}/vc3/vc3-playbooks/login/config/jupyterhub_config.py
%{_sysconfdir}/vc3/vc3-playbooks/login/config/jupyterhub_config.pyc
%{_sysconfdir}/vc3/vc3-playbooks/login/config/jupyterhub_config.pyo


%changelog
* Wed Oct 03 2018 Lincoln Bryant <lincolnb@uchicago.edu> - 1.1.0-1
- Updated
* Mon May 07 2018 Lincoln Bryant <lincolnb@uchicago.edu> - 1.0.0-1
- Initial package
