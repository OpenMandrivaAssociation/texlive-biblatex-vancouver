Name:		texlive-biblatex-vancouver
Version:	55339
Release:	1
Summary:	Vancouver style for BibLaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/biblatex-vancouver
License:	gpl3+
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-vancouver.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-vancouver.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides the Vancouver reference style for
BibLaTeX. It is based on the numeric style and requires biber.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/biblatex-vancouver
%doc %{_texmfdistdir}/doc/latex/biblatex-vancouver

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
