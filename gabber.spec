#
# Conditional build:
# _with_ipv6        - with IPv6 support
#

%define snap 20021025

Summary:	A GNOME Jabber client
Summary(pl):	Klient Jabber dla GNOME
Summary(pt_BR):	Um cliente GNOME para o Jabber
Name:		gabber
Version:	1.9.0
Release:	0.%{snap}.1
License:	GPL
Group:		Applications/Communications
Source0:	http://jabberstudio.org/gabber/%{name}-%{version}.%{snap}.tar.gz
URL:		http://gabber.sourceforge.net/
Requires(post,postun):	/sbin/ldconfig
Requires(post,postun):	scrollkeeper
Requires:	gnupg
BuildRequires:	libgnomemm-devel >= 1.3.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_sysconfdir	/etc/X11/GNOME2
%define		_mandir		%{_prefix}/man

%description
Gabber is a Gnome client for the distributed Open Source instant
messaging system called Jabber. Gabber aims to be a fairly complete
client while remaining easy to use, trying to maintain a balance
between too many features and being powerful enough.

%description -l pl
Gabber jest klientem GNOME dla dystrybuowanego na zasadach Open Source
systemu Natychmiastowych Wiadomo¶ci (IM - Instant Messaging) o nazwie
Jabber. Gabber jest kompletnym klientem systemu Jabber pozostaj±c przy
tym prostym w u¿yciu.

%description -l pt_BR
Gabber é um cliente GNOME para o sistema distribuído de mensagens
instantâneas Jabber. Gabber é um cliente completo, sendo poderoso e ao
mesmo tempo fácil de usar.

%prep
%setup -q

%build
rm -f missing
glib-gettextize
intltoolize
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
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
