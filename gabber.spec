Summary:	A GNOME Jabber client
Summary(es):	Klient Jabber dla GNOME
Name:		gabber
Version:	0.8.2
Release:	3
License:	GPL
Group:		Applications/Communications
Group(de):	Applikationen/Kommunikation
Group(pl):	Aplikacje/Komunikacja
Source0:	http://prdownloads.sourceforge.net/gabber/%{name}-%{version}.tar.gz
Patch0:		%{name}-DESTDIR.patch
URL:		http://gabber.sourceforge.net/
BuildRequires:	ORBit-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gnome-libs-devel >= 1.2.13
BuildRequires:	gnomemm-devel >= 1.1.19
BuildRequires:	gettext-devel
BuildRequires:	gtk+-devel >= 1.2.5
BuildRequires:	gtkmm-devel >= 1.1.12
BuildRequires:	libtool
BuildRequires:	libglade-devel
BuildRequires:	libsigc++-devel
BuildRequires:	libunicode-devel
BuildRequires:	openssl-devel >= 0.9.6a
BuildRequires:	scrollkeeper
BuildRequires:	xml-i18n-tools
Prereq:		/sbin/ldconfig
Prereq:		scrollkeeper
Requires:	applnk
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

%prep
%setup -q
%patch0 -p1

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
	Applicationsdir=%{_applnkdir}/Network/Communications \
	omf_dest_dir=%{_omf_dest_dir}/omf/gabber

gzip -9nf AUTHORS NEWS README TODO

%find_lang %{name} --with-gnome --all-name

%post	-p /usr/bin/scrollkeeper-update
%postun -p /usr/bin/scrollkeeper-update

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz
%{_sysconfdir}/*/*/*
%attr(755,root,root) %{_bindir}/*
%{_applnkdir}/Network/Communications/*.desktop
%{_datadir}/%{name}
%{_omf_dest_dir}/omf/%{name}
%{_pixmapsdir}/*
%{_datadir}/sounds/*
