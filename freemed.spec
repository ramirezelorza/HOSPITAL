# $Id$
#
# Authors:
#      Jeff Buchbinder <jeff@freemedsoftware.org>
#
# FreeMED Electronic Medical Record and Practice Management System
# Copyright (C) 1999-2012 FreeMED Software Foundation
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.
#

Name:		freemed
Summary:	Opensource electronic medical record (EMR) software
Version:	0.9.0
Release:	1
License:	GPL
Group:		Applications/Medical
URL:		http://www.freemedsoftware.org/
BuildArch:	noarch

Source0:	%{name}-%{version}.tar.gz

BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root

Requires:	php >= 5.0, php-mysql >= 5.0, tetex, ghostscript, mkisofs, cdrecord, netpbm-progs, ImageMagick, cups, djvulibre, httpd >= 2.0
BuildPrereq:	make, perl

%description
FreeMED is an opensource electronic medical record (EMR) and medical
management system.

%prep

%setup

%build
make all

%install
rm -fr %{buildroot}
mkdir -p %{buildroot}%{_prefix}/share/freemed/
%makeinstall
# Install seperate init script

%clean
rm -fr %{buildroot}

%post

%preun

%postun

%files
%defattr(-,root,root)
%{_datadir}/%{name}

%changelog

* Sun Feb 25 2007 Jeff Buchbinder <jeff@freemedsoftware.org> - 0.9.0-1
  - v0.9.0 release

* Tue Feb 25 2006 Jeff Buchbinder <jeff@freemedsoftware.org> - 0.8.3-1
  - v0.8.3 release

* Sun Feb 19 2006 Jeff Buchbinder <jeff@freemedsoftware.com> - 0.8.2-1
  - v0.8.2 release

* Thu Nov 17 2005 Jeff Buchbinder <jeff@freemedsoftware.com> - 0.8.1.1-1
  - v0.8.1.1 release

* Sun Oct 30 2005 Jeff Buchbinder <jeff@freemedsoftware.com> - 0.8.1-1
  - v0.8.1 release

* Sat Aug 27 2005 Jeff Buchbinder <jeff@freemedsoftware.com> - 0.8.0-1
  - v0.8.0 release

* Tue Nov 30 2004 Jeff Buchbinder <jeff@freemedsoftware.com> - 0.7.2-1fc1
  - v0.7.2 release

* Mon Oct 18 2004 Jeff Buchbinder <jeff@freemedsoftware.com> - 0.7.1-1fc1
  - v0.7.1 release

* Fri May 28 2004 Jeff Buchbinder <jeff@freemedsoftware.com> - 0.7.0-1fc1
  - v0.7.0 release

* Fri Apr 16 2004 Jeff Buchbinder <jeff@freemedsoftware.com> - 0.7.0b3-1fc1
  - Initial Fedora Core 1 packaging (apologies to RH9 users)

