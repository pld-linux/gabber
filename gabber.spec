#
# Conditional build:
# _with_ipv6        - with IPv6 support
#

Summary:	A GNOME Jabber client
Summary(pl):	Klient Jabber dla GNOME
Summary(pt_BR):	Um cliente GNOME para o Jabber
Name:		gabber
Version:	1.9.0
Release:	0.1
License:	GPL
Group:		Applications/Communications
# take source 0 from cvs, please
Source0:	%{name}-%{version}.tar.gz
#Source0:	http://www.jabberstudio.org/projects/gabber/releases/download.php?file=%{name}-%{version}.tar.gz
URL:		http://gabber.sourceforge.net/
Requires:	gnupg
BuildRequires:	gconfmm-devel >= 2.0.0
BuildRequires:	jabberoo-devel >= 1.9.0.1
BuildRequires:	libglademm-devel >= 2.0.0
BuildRequires:	libsigc++-devel >= 1.2.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
CXXFLAGS="%{rpmcflags}"
%configure \
	--%{!?debug:dis}%{?debug:en}able-debug \
	--disable-schemas-install \
	%{?_with_ipv6:--enable-ipv6}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README TODO
%{_sysconfdir}/gconf/schemas/*
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/%{name}/*.so
%{_libdir}/%{name}/*.la
%{_datadir}/%{name}
%{_datadir}/applications/*
%{_pixmapsdir}/*
