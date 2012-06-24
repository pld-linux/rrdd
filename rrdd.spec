Summary:	Send RRD update data over UDP
Summary(pl):	Wysy�a aktualizacje RRD przez UDP
Name:		rrdd
Version:	20050213
Release:	0
License:	"THE BEER-WARE LICENSE" (Revision 42)
Group:		Applications/Databases
Source0:	http://duch.mimuw.edu.pl/~hunter/%{name}-%{version}.tar.gz
# Source0-md5:	1b5cea5ba49c1deb6062006ece4e4ef5
URL:		http://phk.freebsd.dk/rrdd/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildRequires:	rrdtool-devel

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

%package client
Summary:     Send RRD update data over UDP
Summary(pl):    Wysy�a aktualizacje RRD przez UDP
Group:      Applications/Databases

%description client
This is client package.

%description -l pl client
To jest pakiet z klientem

%prep
%setup -q -n %{name}

%build

cd client 
gcc -Wall main.c rrrdupdate.c -o rrrdupdate
cd ..

cd server
gcc -Wall -lrrd rrdd.c -o rrdd
cd ..

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/bin/
install client/rrrdupdate server/rrdd $RPM_BUILD_ROOT/usr/bin/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr (755,root,root) /usr/bin/rrdd

%files client
%attr (755,root,root) /usr/bin/rrrdupdate
