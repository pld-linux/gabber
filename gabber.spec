#
# Conditional build:
# _with_ipv6        - with IPv6 support
#
Summary:	A GNOME Jabber client
Summary(pl):	Klient Jabber dla GNOME
Summary(pt_BR):	Um cliente GNOME para o Jabber
Name:		gabber
Version:	0.8.8
Release:	1
License:	GPL
Group:		Applications/Communications
# Source0-md5:	e0748960c47982c1d6d17525c42efe41
Source0:	http://dl.sourceforge.net/gabber/%{name}-%{version}.tar.gz
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-ac_fixes.patch
Patch2:		%{name}-omf.patch
URL:		http://gabber.sourceforge.net/
BuildRequires:	ORBit-devel
BuildRequires:	gal-devel >= 0.19
BuildRequires:	gdk-pixbuf-gnome-devel
BuildRequires:	gettext-devel
BuildRequires:	gnome-libs-devel >= 1.2.13
BuildRequires:	gnomemm-devel >= 1.2.0
BuildRequires:	gnome-print-devel
BuildRequires:	gtk+-devel >= 1.2.5
BuildRequires:	gtkmm-devel >= 1.2.5
BuildRequires:	intltool
BuildRequires:	libglade-gnome-devel >= 0.17
BuildRequires:	libsigc++1-devel
BuildRequires:	libunicode-devel
BuildRequires:	openssl-devel >= 0.9.7
BuildRequires:	scrollkeeper
BuildRequires:	xmms-devel
Requires:	applnk
Requires:	gnupg
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/X11/GNOME
%define		_omf_dest_dir	%(scrollkeeper-config --omfdir)

%description
Gabber is a Gnome client for the distributed Open Source instant
messaging system called Jabber. Gabber aims to be a fairly complete
client while remaining easy to use, trying to maintain a balance
between too many features and being powerful enough.

%description -l pl
Gabber jest klientem GNOME dla dystrybuowanego na zasadach Open Source
systemu Natychmiastowych Wiadomo�ci (IM - Instant Messaging) o nazwie
Jabber. Gabber jest kompletnym klientem systemu Jabber pozostaj�c przy
tym prostym w u�yciu.

%description -l pt_BR
Gabber � um cliente GNOME para o sistema distribu�do de mensagens
instant�neas Jabber. Gabber � um cliente completo, sendo poderoso e ao
mesmo tempo f�cil de usar.

%prep
%setup -q
#%patch0 -p1
#%patch1 -p1
#%patch2 -p1

%build
CXXFLAGS="%{rpmcflags}"
%configure \
	--%{!?debug:dis}%{?debug:en}able-debug \
	--enable-gnome \
	--enable-panel \
	--enable-ssl \
	--enable-screensaver \
	--enable-xmms \
	%{?_with_ipv6:--enable-ipv6} \
	--disable-perl

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	Applicationsdir=%{_applnkdir}/Network/Communications \
	omf_dest_dir=%{_omf_dest_dir}/%{name}

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/bin/scrollkeeper-update
%postun -p /usr/bin/scrollkeeper-update

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README TODO
%{_sysconfdir}/sound/events/*
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man?/*
%{_applnkdir}/Network/Communications/*.desktop
%{_datadir}/%{name}
%{_omf_dest_dir}/%{name}
%{_pixmapsdir}/*
%{_datadir}/sounds/*
