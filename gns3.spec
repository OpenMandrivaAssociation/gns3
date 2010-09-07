Name:		gns3
Version:	0.7.2
Release:	%mkrel 1
Summary:	Graphical network simulator that allows simulation of complex networks
URL:		http://www.gns3.net/
Source:		http://downloads.sourceforge.net/gns-3/GNS3-%{version}-src.tar.gz
License:	GPLv2+
Group:		Emulators
BuildArch:	noarch
Requires:	python-qt4
Requires:	dynagen
#Suggests: pemu
BuildRequires:	python-qt4
BuildRequires:	python-devel
Buildroot:	%{_tmppath}/%{name}-root

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

%build
python setup.py build

%install
rm -Rf %{buildroot}
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

%clean
rm -Rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/%{name}
%{py_sitedir}/GNS3*
%{_datadir}/applications/mandriva-%{name}.desktop
%defattr(644,root,root,755)
%doc AUTHORS README CHANGELOG
