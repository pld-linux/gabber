#
# Conditional build:
# _with_ipv6        - with IPv6 support
#
Summary:	A GNOME Jabber client
Summary(pl):	Klient Jabber dla GNOME
Summary(pt_BR):	Um cliente GNOME para o Jabber
Name:		gabber
Version:	0.8.7
Release:	5
License:	GPL
Group:		Applications/Communications
Source0:	http://prdownloads.sourceforge.net/gabber/%{name}-%{version}.tar.gz
# Source0-md5:	afd0c258b27dfb386e7ec668a9d371aa
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-ac_fixes.patch
Patch2:		%{name}-omf.patch
Patch3:		%{name}-desktop.patch
URL:		http://gabber.sourceforge.net/
BuildRequires:	ORBit-devel
BuildRequires:	autoconf
BuildRequires:	automake
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
BuildRequires:	openssl-devel >= 0.9.6a
BuildRequires:	scrollkeeper
BuildRequires:	xmms-devel
Requires(post,postun):	/sbin/ldconfig
Requires(post,postun):	scrollkeeper
Requires:	applnk
Requires:	gnupg
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_sysconfdir	/etc/X11/GNOME
%define		_mandir		%{_prefix}/man
%define		_omf_dest_dir	%(scrollkeeper-config --omfdir)

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
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
sed -e s/AM_GNOME_GETTEXT/AM_GNU_GETTEXT/ configure.in > configure.in.tmp
mv -f configure.in.tmp configure.in
rm -f missing
intltoolize --copy --force
%{__gettextize}
%{__aclocal} -I %{_aclocaldir}/gnome
%{__autoheader}
%{__autoconf}
%{__automake}
cd jabberoo
rm -f missing
%{__aclocal} -I %{_aclocaldir}/gnome
%{__autoheader}
%{__autoconf}
%{__automake}
cd ..
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
