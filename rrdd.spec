Summary:	Send RRD update data over UDP
Summary(pl):	Wysy³anie aktualizacji RRD po UDP
Name:		rrdd
Version:	20050213
Release:	0
License:	"THE BEER-WARE LICENSE" (Revision 42)
Group:		Applications/Databases
Source0:	http://duch.mimuw.edu.pl/~hunter/%{name}-%{version}.tar.gz
# Source0-md5:	1b5cea5ba49c1deb6062006ece4e4ef5
URL:		http://phk.freebsd.dk/rrdd/
BuildRequires:	rrdtool-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The server is a small C program which received UDP datagrams with
stuff for "RRDupdate" in it, and if it looks right tries to do the
update.  The server will only act on existing files in the current
directory, so security should be OK if you make a dedicated directory
for storing your .rrd files.

The client can be used either like a C procedure or a program which
reads stdin for lines like "rrdtool -", with the footnote that it
only accepts "update" lines, sticks them in an UDP packet and ships
it off to the server.

This is server package.

%description -l pl
Serwer to ma³y program w C odbieraj±cy datagramy UDP z poleceniami
RRDupdate i, je¶li wygl±daj± one poprawnie, próbuj±cy uaktualniaæ bazê
RRD. Serwer dzia³a tylko na istniej±cych plikach w bie¿±cym katalogu,
przez co nie powinno byæ problemów z bezpieczeñstwem w przypadku
utworzenia dedykowanego katalogu do przechowywania plików .rrd.

Klient mo¿e byæ u¿ywany jako funkcja C lub jako program czytaj±cy ze
standardowego wej¶cia linie "rrdtool -" (przy czym akceptuje on tylko
linie "update"), pakuj±cy je w pakiet UDP i wysy³aj±cy do serwera.

Ten pakiet zawiera serwer.

%package client
Summary:	Send RRD update data over UDP
Summary(pl):	Wysy³anie aktualizacji RRD po UDP
Group:		Applications/Databases

%description client
This is client package.

%description -l pl client
To jest pakiet z klientem.

%prep
%setup -q -n %{name}

%build
cd client 
%{__cc} %{rpmldflags} %{rpmcflags} -Wall main.c rrrdupdate.c -o rrrdupdate
cd ../server
%{__cc} %{rpmldflags} %{rpmcflags} -Wall -lrrd rrdd.c -o rrdd

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install client/rrrdupdate server/rrdd $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr (755,root,root) %{_bindir}/rrdd

%files client
%defattr(644,root,root,755)
%attr (755,root,root) %{_bindir}/rrrdupdate
