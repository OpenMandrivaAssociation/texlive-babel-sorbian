Name:		texlive-babel-sorbian
Version:	60975
Release:	1
Summary:	TeXLive babel-sorbian package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-sorbian.r60975.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-sorbian.doc.r60975.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-sorbian.source.r60975.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
TeXLive babel-sorbian package.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/babel-sorbian
%doc %{_texmfdistdir}/doc/generic/babel-sorbian
#- source
%doc %{_texmfdistdir}/source/generic/babel-sorbian

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
