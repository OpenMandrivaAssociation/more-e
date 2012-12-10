%define rel 5
%define name    more-e
%define version 0.1
%define release %mkrel %{rel}
%define prefix /usr

Name:      %name
Version:    %version
Release:   %release
License:    GPL
Summary:10 additional themes for Enlightenment
Group:      Graphical desktop/Enlightenment
Source:     %name-%version.tar.bz2
URL:          http://themes.freshmeat.net/browse/60/?topic_id=60
BuildRoot:  %_tmppath/%name-%version-%release-root
Requires:enlightenment >= 0.16
BuildArchitectures: noarch

%description
This package contains 10 recent/updated themes for Enlightenmet.
They were assembled by Charles A Edwards <eslrahc@bellsouth.net> on Dec 07 2003
All themes are avaiable separately from the themes collection at Freshmeat.net.

Inckuded themes:
o 0ri0n--A red and gray theme. 
o cronos--A nice transparent theme
o cutting-edge_MinEguE--Based on MinEguE with a transparent cut edge effect.
o eviljester--An evil theme.
o handofgod--A port of the original Hand Of God theme. 
o lhb--The Brushed Metal theme with different graphics and a different pager.  
o xanalloy--Based on an the older versions of the "DarkAlloy" theme

%prep
rm -fr $RPM_BUILD_ROOT
%setup -q -n %name-%version 

install -d $RPM_BUILD_ROOT/%prefix/X11R6/share/enlightenment/themes
mv -f themes/* $RPM_BUILD_ROOT/%prefix/X11R6/share/enlightenment/themes

#change perms on 600 files
chmod 644 $RPM_BUILD_ROOT/%prefix/X11R6/share/enlightenment/themes/xanalloy/dialogs/images/slider_base_ver.png 
chmod 644  $RPM_BUILD_ROOT/%prefix/X11R6/share/enlightenment/themes/xanalloy/dialogs/images/slider_base_hor.png
chmod 755 $RPM_BUILD_ROOT/%prefix/X11R6/share/enlightenment/themes/cutting-edge_MinEguE
chmod 644 -f $RPM_BUILD_ROOT/%prefix/X11R6/share/enlightenment/themes/0ri0n/common/common.cfg

#rm hidden, backup, and zero-length files
rm -rf `find $RPM_BUILD_ROOT -name .xvpics`
rm -rf $RPM_BUILD_ROOT/%prefix/X11R6/share/enlightenment/themes/handofgod/slideouts/slideouts.cfg
rm -rf $RPM_BUILD_ROOT/%prefix/X11R6/share/enlightenment/themes/lhb/slideouts/slideouts.cfg
rm -rf $RPM_BUILD_ROOT/%prefix/X11R6/share/enlightenment/themes/cutting-edge_MinEguE/borders/common/border.cfg~
rm -rf $RPM_BUILD_ROOT/%prefix/X11R6/share/enlightenment/themes/cronos/buttons/buttons.cfg
rm -rf $RPM_BUILD_ROOT/%prefix/X11R6/share/enlightenment/themes/cutting-edge_MinEguE/slideouts/slideouts.cfg 
rm -rf $RPM_BUILD_ROOT/%prefix/X11R6/share/enlightenment/themes/cutting-edge_MinEguE/backgrounds/backgrounds.cfg
rm -rf $RPM_BUILD_ROOT/%prefix/X11R6/share/enlightenment/themes/cronos/slideouts/slideouts.cfg
rm -rf $RPM_BUILD_ROOT/%prefix/X11R6/share/enlightenment/themes/cutting-edge_MinEguE/borders/STICK/border.cfg~
rm -rf $RPM_BUILD_ROOT/%prefix/X11R6/share/enlightenment/themes/0ri0n/slideouts/slideouts.cfg 
rm -rf $RPM_BUILD_ROOT/%prefix/X11R6/share/enlightenment/themes/cronos/borders/SHAPED/border.cfg 
rm -rf $RPM_BUILD_ROOT/%prefix/X11R6/share/enlightenment/themes/cutting-edge_MinEguE/tooltips/tooltips.cfg~
rm -rf $RPM_BUILD_ROOT/%prefix/X11R6/share/enlightenment/themes/cutting-edge_MinEguE/borders/TRANSIENT/border.cfg
rm -rf $RPM_BUILD_ROOT/%prefix/X11R6/share/enlightenment/themes/0ri0n/buttons/buttons.cfg
rm -rf $RPM_BUILD_ROOT/%prefix/X11R6/share/enlightenment/themes/lhb/ABOUT/MAIN~ 
rm -rf $RPM_BUILD_ROOT/%prefix/X11R6/share/enlightenment/themes/lhb/buttons/buttons.cfg 
rm -rf $RPM_BUILD_ROOT/%prefix/X11R6/share/enlightenment/themes/cutting-edge_MinEguE/borders/SHAPED/border.cfg 
rm -rf $RPM_BUILD_ROOT/%prefix/X11R6/share/enlightenment/themes/cutting-edge_MinEguE/borders/FIXED_SIZE/border.cfg
rm -rf $RPM_BUILD_ROOT/%prefix/X11R6/share/enlightenment/themes/cutting-edge_MinEguE/buttons/buttons.cfg
 
%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr (-,root,root)
%doc README
%{prefix}/X11R6/share/enlightenment/themes/0ri0n
#%{prefix}/X11R6/share/enlightenment/themes/BlackE_nob
%{prefix}/X11R6/share/enlightenment/themes/cronos
%{prefix}/X11R6/share/enlightenment/themes/cutting-edge_MinEguE
%{prefix}/X11R6/share/enlightenment/themes/eviljester
%{prefix}/X11R6/share/enlightenment/themes/handofgod
%{prefix}/X11R6/share/enlightenment/themes/lhb
#%{prefix}/X11R6/share/enlightenment/themes/mawtoomanydrugs
#%{prefix}/X11R6/share/enlightenment/themes/nebulongalaticserenity
%{prefix}/X11R6/share/enlightenment/themes/xanalloy



%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 0.1-5mdv2011.0
+ Revision: 620393
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.1-4mdv2010.0
+ Revision: 430090
- rebuild

* Thu Jan 03 2008 Olivier Blin <oblin@mandriva.com> 0.1-3mdv2008.1
+ Revision: 140955
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - import more-e


* Tue Jun 06 2006 Charles A Edwards <eslrahc@mandriva.org> 0.1-3mdv2007.0
- mkrel
- rebuild

* Thu Feb 03 2005 Charles A Edwards <eslrahc@mandrake.org> 0.1-2mdk
- belated bday

* Mon Dec 08 2003 Charles A Edwards <eslrahc@mandrake.org> 0.1-1mdk
- first mdk pkg
