%global gittag 0.5

Name:		tivodecode-ng
Version:	%{gittag}
Release:	5%{?dist}
Summary:	Convert a .TiVo file from TiVoToGo to a normal MPEG

# sha1.c is public domain.  The QUALCOMM license is just the SSLeay
# BSD 4-clause "Original" or "Old" License with the 4th clause
# removed, leaving it equivalent to the BSD license plus a patent
# grant.  The resulting package is therefore just BSD licensed.
License:	BSD
URL:		https://github.com/wmcbrine/tivodecode-ng
Source0:	%{url}/archive/%{gittag}/%{name}-%{version}.tar.gz

BuildRequires:	gcc-c++
BuildRequires:	make

Provides:	tivodecode = %{version}-%{release}
Obsoletes:	tivodecode < 0.2-0.17.pre4

%description
tivodecode-ng ("ng" for "next generation") is a portable command-line
tool for decrypting .TiVo video files into program streams or
transport streams, depending on the source. It also will decrypt the
metadata (title, description, etc.). It's based on tivodecode by
Jeremy Drake, with enhancements by several contributors. tivodecode-ng
adds support for transport streams, although that's a work in
progress. (Note that support for program streams is as complete as
ever.)


%prep
%autosetup -n %{name}-%{gittag}


%build
#autoreconf -i -f
%configure
%{make_build}


%install
%{make_install}


%files
%{_bindir}/*
%license COPYING.md
%doc AUTHORS.md README.md NEWS.md


%changelog
* Tue Aug 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jul 05 2021 Charles R. Anderson <cra@alum.wpi.edu> - 0.5-4
- Remove dist tag from Obsoletes:

* Sun Jul 04 2021 Charles R. Anderson <cra@alum.wpi.edu> - 0.5-3
- Remove QUALCOMM from license field and use url macro in Source0

* Sat Jul 03 2021 Charles R. Anderson <cra@alum.wpi.edu> - 0.5-2
- Remove Group and BR make

* Thu Jul 01 2021 Charles R. Anderson <cra@alum.wpi.edu> - 0.5-1
- initial release
