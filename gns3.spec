Name:		gns3
Version:	0.8.2
Release:	2
Summary:	Graphical network simulator that allows simulation of complex networks
URL:		https://www.gns3.net/
Source0:	http://downloads.sourceforge.net/gns-3/GNS3-%{version}-src.tar.gz
License:	GPLv2+
Group:		Emulators
BuildArch:	noarch
Requires:	python-qt4
Requires:	dynagen
#Suggests: pemu
BuildRequires:	python-qt4
BuildRequires:	python-devel
Patch0:		local_path_removed.patch

%description
GNS3 is a graphical network simulator that allows simulation of complex
networks.

To allow complete simulations, GNS3 is strongly linked with :

    * Dynamips, the core program that allows Cisco IOS emulation.
    * Dynagen, a text-based front-end for Dynamips.
    * Pemu, a Cisco PIX firewall emulator based on Qemu.

GNS3 is an excellent complementary tool to real labs for Cisco network
engineers, administrators and people wanting to pass certifications such as
CCNA, CCNP, CCIP or CCIE.

It can also be used to experiment features of Cisco IOS or to check
configurations that need to be deployed later on real routers.

%prep
%setup -q -n GNS3-%{version}-src
%patch0 -p1

%build
python setup.py build

%install
python setup.py install --root=%{buildroot}

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop <<EOF
[Desktop Entry]
Name=GNS3
Comment=Graphical Network Simulator
Exec=%{_bindir}/%{name} 
Terminal=false
Type=Application
StartupNotify=true
Categories=X-MandrivaLinux-MoreApplications-Emulators;Emulator;
EOF

%files
%{_bindir}/%{name}
%{py_sitedir}/GNS3*
%{_datadir}/applications/mandriva-%{name}.desktop
%{_datadir}/examples/gns3/baseconfig.txt
%{_prefix}/libexec/%{name}
%defattr(644,root,root,755)
%doc AUTHORS README CHANGELOG


%changelog
* Fri May 11 2012 Alexander Khrukin <akhrukin@mandriva.org> 0.8.2-1
+ Revision: 798278
- version update 0.8.2

* Mon Jun 27 2011 Buchan Milne <bgmilne@mandriva.org> 0.7.4-1
+ Revision: 687476
- update to new version 0.7.4

* Tue Feb 22 2011 Buchan Milne <bgmilne@mandriva.org> 0.7.3-1
+ Revision: 639382
- update to new version 0.7.3

* Fri Nov 12 2010 Bogdano Arendartchuk <bogdano@mandriva.com> 0.7.2-2mdv2011.0
+ Revision: 596946
- rebuild for python 2.7

* Tue Sep 07 2010 Buchan Milne <bgmilne@mandriva.org> 0.7.2-1mdv2011.0
+ Revision: 576589
- update to new version 0.7.2

* Mon Mar 01 2010 Sandro Cazzaniga <kharec@mandriva.org> 0.7-1mdv2010.1
+ Revision: 513037
- update to 0.7
- fix license

* Thu May 14 2009 Frederik Himpe <fhimpe@mandriva.org> 0.6.1-1mdv2010.0
+ Revision: 375721
- update to new version 0.6.1

* Sun Feb 01 2009 Buchan Milne <bgmilne@mandriva.org> 0.6-1mdv2009.1
+ Revision: 336213
- More buildrequires
- Fix buildrequires
- import gns3

