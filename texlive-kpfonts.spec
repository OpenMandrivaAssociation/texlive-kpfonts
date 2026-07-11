%global tl_name kpfonts
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	3.36
Release:	%{tl_revision}.1
Summary:	A complete set of fonts for text and mathematics
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/kpfonts
License:	lppl gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/kpfonts.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/kpfonts.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The family contains text fonts in roman, sans-serif and monospaced
shapes, with true small caps and old-style numbers; the package offers
full support of the textcomp package. The mathematics fonts include all
the AMS fonts, in both normal and bold weights. Each of the font types
is available in two main versions: default and 'light'. Each version is
available in four variants: default; oldstyle numbers; oldstyle numbers
with old ligatures such as ct and st, and long-tailed capital Q; and
veryoldstyle with long s. Other variants include small caps as default
or 'large small caps', and for mathematics both upright and slanted
shapes for Greek letters, as well as default and narrow versions of
multiple integrals. The fonts were originally derived from URW Palladio
(with URW's agreement) though the fonts are very clearly different in
appearance from their parent.

