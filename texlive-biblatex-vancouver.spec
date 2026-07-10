%global tl_name biblatex-vancouver
%global tl_revision 75301

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.1
Release:	%{tl_revision}.1
Summary:	Vancouver style for BibLaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/biblatex-contrib/biblatex-vancouver
License:	gpl3+
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-vancouver.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-vancouver.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides the Vancouver reference style for BibLaTeX. It is
based on the numeric style and requires biber.

%prep
%setup -q -c -a1
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
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/biblatex-vancouver
%dir %{_datadir}/texmf-dist/tex/latex/biblatex-vancouver
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-vancouver/LICENSE
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-vancouver/README
%{_datadir}/texmf-dist/tex/latex/biblatex-vancouver/vancouver.bbx
%{_datadir}/texmf-dist/tex/latex/biblatex-vancouver/vancouver.cbx
