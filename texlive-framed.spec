# revision 26789
# category Package
# catalog-ctan /macros/latex/contrib/framed
# catalog-date 2012-06-01 12:48:04 +0200
# catalog-license other-free
# catalog-version 0.96
Name:		texlive-framed
Version:	0.96
Release:	8
Summary:	Framed or shaded regions that can break across pages
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/framed
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/framed.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/framed.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package creates three environments: - framed, which puts an
ordinary frame box around the region, - shaded, which shades
the region, and - leftbar, which places a line at the left
side. The environments allow a break at their start (the
\FrameCommand enables creation of a title that is "attached" to
the environment); breaks are also allowed in the course of the
framed/shaded matter. There is also a command \MakeFramed to
make your own framed-style environments.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/framed/framed.sty
%doc %{_texmfdistdir}/doc/latex/framed/framed.pdf
%doc %{_texmfdistdir}/doc/latex/framed/framed.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Tue Aug 07 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.96-1
+ Revision: 812267
- Update to latest release.

* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.95-2
+ Revision: 752094
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.95-1
+ Revision: 718504
- texlive-framed
- texlive-framed
- texlive-framed
- texlive-framed

