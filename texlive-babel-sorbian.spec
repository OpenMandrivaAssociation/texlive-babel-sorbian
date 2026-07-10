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
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides language definitions file for support of both Upper
and Lower Sorbian, in babel. Some shortcuts are defined, as well as
translations to the relevant language of standard "LaTeX names".

%prep
%setup -q -c -a1 -a2
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/source
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/generic
%dir %{_datadir}/texmf-dist/source/generic
%dir %{_datadir}/texmf-dist/tex/generic
%dir %{_datadir}/texmf-dist/doc/generic/babel-sorbian
%dir %{_datadir}/texmf-dist/source/generic/babel-sorbian
%dir %{_datadir}/texmf-dist/tex/generic/babel-sorbian
%doc %{_datadir}/texmf-dist/doc/generic/babel-sorbian/README.md
%doc %{_datadir}/texmf-dist/doc/generic/babel-sorbian/lsorbian.pdf
%doc %{_datadir}/texmf-dist/doc/generic/babel-sorbian/usorbian.pdf
%doc %{_datadir}/texmf-dist/source/generic/babel-sorbian/lsorbian.dtx
%doc %{_datadir}/texmf-dist/source/generic/babel-sorbian/sorbian.ins
%doc %{_datadir}/texmf-dist/source/generic/babel-sorbian/usorbian.dtx
%{_datadir}/texmf-dist/tex/generic/babel-sorbian/lsorbian.ldf
%{_datadir}/texmf-dist/tex/generic/babel-sorbian/usorbian.ldf
