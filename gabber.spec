#
# Conditional build:
# _with_ipv6        - with IPv6 support
#
Summary:	A GNOME Jabber client
Summary(pl):	Klient Jabber dla GNOME
Summary(pt_BR):	Um cliente GNOME para o Jabber
Name:		gabber
Version:	1.9.1
Release:	0.1
License:	GPL
Group:		Applications/Communications
Source0:	http://www.jabberstudio.org/files/gabber/%{name}-%{version}.tar.gz
# Source0-md5:	02816f9f53521ff6cd8771ef098e4baf
Patch0:		%{name}-types.patch
URL:		http://gabber.sourceforge.net/
BuildRequires:	gconfmm-devel >= 2.0.0
BuildRequires:	jabberoo-devel >= 1.9.1
BuildRequires:	libglademm-devel >= 2.0.0
BuildRequires:	libsigc++-devel >= 1.2.3
Requires(post):	GConf2
Requires:	gnupg
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gabber is a GNOME client for the distributed Open Source instant
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
%setup -q -n Gabber-%{version}
%patch -p1

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
%{_desktopdir}/*
%{_pixmapsdir}/*
