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
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides the Vancouver reference style for BibLaTeX. It is
based on the numeric style and requires biber.

