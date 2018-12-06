Name:           golang-github-d4l3k-messagediff
Summary:        Generate diffs of arbitrary structs in Go
Version:        1.2.1
Release:        3%{?dist}
License:        MIT

# https://github.com/d4l3k/messagediff
%global repo    messagediff
%global goipath github.com/d4l3k/%{repo}
%global tag     v1.2.1

%gometa

URL:            %{gourl}
Source0:        %{gourl}/archive/%{tag}/%{repo}-%{version}.tar.gz

%description
%{summary}


%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgeautosetup -p1


%install
%goinstall


%check
%gochecks


%files devel -f devel.file-list
%license LICENSE
%doc README.md CHANGELOG.md


%changelog
* Wed Oct 24 2018 Fabio Valentini <decathorpe@gmail.com> - 1.2.1-3
- Use standard GitHub SourceURL again for consistency between releases.
- Use forgeautosetup instead of gosetup.

* Fri Aug 31 2018 Fabio Valentini <decathorpe@gmail.com> - 1.2.1-2
- Update to use spec 3.0.

* Thu Jul 19 2018 Fabio Valentini <decathorpe@gmail.com> - 1.2.1-1
- Bump to version 1.2.1 (no code changes).

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-0.6.git29f32d8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-0.5.git29f32d8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Aug 07 2017 Fabio Valentini <decathorpe@gmail.com> - 1.1.0-0.4.git29f32d8
- Bump to commit 29f32d8.

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-0.3.git2fe2a1d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-0.2.git2fe2a1d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Mar 01 2017 Fabio Valentini <decathorpe@gmail.com> - 1.1.0-0.1.git2fe2a1d
- First package for Fedora

