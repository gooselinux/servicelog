Name:           servicelog
Version:        1.1.7
Release:        2%{?dist}
Summary:        Servicelog Tools

Group:          System Environment/Base
License:        GPLv2
URL:            http://linux-diag.sourceforge.net/servicelog
Source0:        http://downloads.sourceforge.net/linux-diag/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

#Requires(pre):       shadow-utils

BuildRequires:  libservicelog-devel >= 1.1.9-2
BuildRequires:  autoconf libtool librtas-devel help2man

# because of librtas-devel in libservicelog
ExclusiveArch: ppc ppc64

%description
Command-line interfaces for viewing and manipulating the contents of
the servicelog database. Contains entries that are useful
for performing system service operations, and for providing a history
of service operations that have been performed on the system.

%prep
%setup -q -n %{name}-1.1

%build
autoreconf -fiv
%configure
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT
help2man -s 8 -N $RPM_BUILD_ROOT/%{_sbindir}/slog_common_event > $RPM_BUILD_ROOT/%{_mandir}/man8/slog_common_event.8

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc COPYING
%{_bindir}/servicelog
%{_bindir}/v1_servicelog
%{_bindir}/v29_servicelog
%{_bindir}/servicelog_notify
%{_bindir}/log_repair_action
%{_sbindir}/slog_common_event
%{_bindir}/servicelog_manage
%{_mandir}/man[18]/*.[18]*

%changelog
* Wed Jun 16 2010 Roman Rakus <rrakus@redhat.com> - 1.1.7-2
- Generate missing man page from help (help2man)
  Resolves: #599360

* Tue May 18 2010 Roman Rakus <rrakus@redhat.com> - 1.1.7-1
- Initial packaging

