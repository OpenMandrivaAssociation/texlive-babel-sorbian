%global tl_name babel-sorbian
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0j
Release:	%{tl_revision}.1
Summary:	Babel support for Upper and Lower Sorbian
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/babel-contrib/sorbian
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-sorbian.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-sorbian.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-sorbian.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides language definitions file for support of both Upper
and Lower Sorbian, in babel. Some shortcuts are defined, as well as
translations to the relevant language of standard "LaTeX names".

