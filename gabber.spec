Summary:	A GNOME Jabber client
Summary(es):	Klient Jabber dla GNOME
Name:		gabber
Version:	0.8.2
Release:	1
License:	GPL
Group:		Applications/Communications
Group(de):	Applikationen/Kommunikation
Group(pl):	Aplikacje/Komunikacja
Source0:	http://prdownloads.sourceforge.net/gabber/%{name}-%{version}.tar.gz
URL:		http://gabber.sourceforge.net/
BuildRequires:	gnome-libs-devel >= 1.2.13
BuildRequires:	gtk+-devel >= 1.2.5
BuildRequires:	ORBit-devel
BuildRequires:	libglade-devel
BuildRequires:	libsigc++-devel
BuildRequires:	gtkmm-devel >= 1.1.12
BuildRequires:	gnomemm-devel
BuildRequires:	openssl-devel
BuildRequires:	libunicode-devel
BuildRequires:	iconv >= 2.2.0
BuildRequires:	gettext-devel
BuildRequires:	xml-i18n-tools
BuildRequires:	esound-devel
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	libtool
Requires:	iconv >= 2.2.0
Prereq:		/sbin/ldconfig
Requires:	applnk
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_sysconfdir	/etc/X11/GNOME
%define		_mandir		%{_prefix}/man

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

%prep
%setup -q

%build
rm missing
libtoolize --copy --force
xml-i18n-toolize --copy --force
gettextize --copy --force
aclocal -I macros
autoheader
autoconf
automake -a -c
%configure \
	--enable-gnome \
	--enable-panel \
	--disable-perl

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	Applicationsdir=%{_applnkdir}/Network/Communications
	
gzip -9nf AUTHORS NEWS README TODO

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz
%{_sysconfdir}/*/*/*
%attr(755,root,root) %{_bindir}/*
%{_applnkdir}/Network/Communications/*.desktop
%{_datadir}/%{name}
%{_datadir}/omf/%{name}
%{_pixmapsdir}/*
%{_datadir}/sounds/*
