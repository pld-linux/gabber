#
# Conditional build:
# _with_ipv6        - with IPv6 support
#
Summary:	A GNOME Jabber client
Summary(pl.UTF-8):	Klient Jabber dla GNOME
Summary(pt_BR.UTF-8):	Um cliente GNOME para o Jabber
Name:		gabber
Version:	1.9.4
Release:	1.1
License:	GPL
Group:		Applications/Communications
Source0:	http://www.jabberstudio.org/files/gabber/Gabber-%{version}.tar.gz
# Source0-md5:	eea74466431b962349ae9a911f010ea2
Patch0:		%{name}-types.patch
Patch1:		%{name}-conffix.patch
URL:		http://gabber.jabberstudio.org/
BuildRequires:	gconfmm-devel >= 2.0.0
BuildRequires:	jabberoo-devel >= 1.9.1
BuildRequires:	libglademm-devel >= 2.0.0
BuildRequires:	libsigc++12-devel >= 1.2.3
BuildRequires:	aspell-devel
Requires(post):	GConf2
Requires:	gnupg
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gabber is a GNOME client for the distributed Open Source instant
messaging system called Jabber. Gabber aims to be a fairly complete
client while remaining easy to use, trying to maintain a balance
between too many features and being powerful enough.

%description -l pl.UTF-8
Gabber jest klientem GNOME dla dystrybuowanego na zasadach Open Source
systemu Natychmiastowych Wiadomości (IM - Instant Messaging) o nazwie
Jabber. Gabber jest kompletnym klientem systemu Jabber pozostając przy
tym prostym w użyciu.

%description -l pt_BR.UTF-8
Gabber é um cliente GNOME para o sistema distribuído de mensagens
instantâneas Jabber. Gabber é um cliente completo, sendo poderoso e ao
mesmo tempo fácil de usar.

%prep
%setup -q -n Gabber-%{version}
%patch -P0 -p1
%patch -P1 -p1

%build
CXXFLAGS="%{rpmcflags}"
%configure \
	--%{!?debug:dis}%{?debug:en}able-debug \
	--disable-schemas-install \
	%{?_with_ipv6:--enable-ipv6}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1

# modules are loaded through Glib::Module, i.e. gmodule interface
rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}/*.{a,la}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README TODO
%{_sysconfdir}/gconf/schemas/*
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/Gabber
%attr(755,root,root) %{_libdir}/Gabber/*.so
%{_datadir}/Gabber
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*
