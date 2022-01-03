Summary:	VMware VMDK Sparse Disk Utility
Summary(pl.UTF-8):	Narzędzie do rzadkich dysków VMware VMDK
Name:		vmdkutil
Version:	1.0.1
Release:	1
License:	BSD
Group:		Applications/File
Source0:	https://downloads.sourceforge.net/vmdkutil/%{name}-%{version}.cpp
# Source0-md5:	5e39d11395756e3843dded6d9635f3f5
Patch0:		%{name}-includes.patch
URL:		https://sourceforge.net/projects/vmdkutil/
BuildRequires:	libstdc++-devel >= 6:4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
VMware VMDK Sparse Disk Utility.

%description -l pl.UTF-8
Narzędzie do rzadkich dysków VMware VMDK.

%prep
%setup -q -c -T

cp -p %{SOURCE0} vmdkutil.cpp
%patch0 -p1

%build
%{__cxx} %{rpmldflags} %{rpmcxxflags} %{rpmcppflags} -o vmdkutil vmdkutil.cpp

%install
rm -rf $RPM_BUILD_ROOT

install -D vmdkutil $RPM_BUILD_ROOT%{_bindir}/vmdkutil

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/vmdkutil
