Name:		texlive-kpfonts
Version:	72680
Release:	1
Summary:	A complete set of fonts for text and mathematics
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/kpfonts
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/kpfonts.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/kpfonts.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The family contains text fonts in roman, sans-serif and
monospaced shapes, with true small caps and old-style numbers;
the package offers full support of the textcomp package. The
mathematics fonts include all the AMS fonts, in both normal and
bold weights. Each of the font types is available in two main
versions: default and 'light'. Each version is available in
four variants: default; oldstyle numbers; oldstyle numbers with
old ligatures such as ct and st, and long-tailed capital Q; and
veryoldstyle with long s. Other variants include small caps as
default or 'large small caps', and for mathematics both upright
and slanted shapes for Greek letters, as well as default and
narrow versions of multiple integrals. The fonts were
originally derived from URW Palladio (with URW's agreement)
though the fonts are very clearly different in appearance from
their parent.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/afm/public/kpfonts
%{_texmfdistdir}/fonts/enc/dvips/kpfonts
%{_texmfdistdir}/fonts/map/dvips/kpfonts
%{_texmfdistdir}/fonts/tfm/public/kpfonts
%{_texmfdistdir}/fonts/type1/public/kpfonts
%{_texmfdistdir}/fonts/vf/public/kpfonts
%{_texmfdistdir}/tex/latex/kpfonts
%doc %{_texmfdistdir}/doc/fonts/kpfonts

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
