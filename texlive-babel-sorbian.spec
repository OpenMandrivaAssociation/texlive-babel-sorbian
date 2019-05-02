# revision 30294
# category Package
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-babel-sorbian
Version:	20190228
Release:	1
Summary:	TeXLive babel-sorbian package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-sorbian.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-sorbian.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-sorbian.source.tar.xz
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
%{_texmfdistdir}/tex/generic/babel-sorbian/lsorbian.ldf
%{_texmfdistdir}/tex/generic/babel-sorbian/usorbian.ldf
%doc %{_texmfdistdir}/doc/generic/babel-sorbian/lsorbian.pdf
%doc %{_texmfdistdir}/doc/generic/babel-sorbian/usorbian.pdf
#- source
%doc %{_texmfdistdir}/source/generic/babel-sorbian/lsorbian.dtx
%doc %{_texmfdistdir}/source/generic/babel-sorbian/sorbian.ins
%doc %{_texmfdistdir}/source/generic/babel-sorbian/usorbian.dtx

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
