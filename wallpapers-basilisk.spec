# %define photos_dir %_datadir/wallpapers
# %define photos_dir_lnk %_datadir/backgrounds
%define photos_dir %_datadir/backgrounds
%define wname wpbasilisk

Name: wallpapers-basilisk
Version: 1.0
Release: alt1

Summary: Wallpaper for DE - Basilisk anime.
Summary(ru_RU.UTF-8): Обои на рабочий стол - аниме Василиск.
License: GPLv3+
Group: Graphics

URL: https://github.com/angrymerz/wpbasilisk
Source: %name-%version.tar

BuildArch: noarch

%description
Pack with the theme of the Basilisk anime.

%description -l ru_RU.UTF-8
Набор обоев с темой аниме Василиск.

%prep
%setup

%install
mkdir -vp %buildroot%photos_dir/%wname
install -m 0644 %wname/* %buildroot%photos_dir/%wname/
# copy results
# cp -v ~/RPM/RPMS/noarch/%name-%version-%release.noarch.rpm ~/progs/%name/
# cp -v ~/RPM/SRPMS/%name-%version-%release.src.rpm ~/progs/%name/
# make link /usr/share/backgrounds/
# ln -vsf %photos_dir/%wname %photos_dir_lnk/

%files
%photos_dir/%wname/*

%changelog
* Sun May 11 2025 merz <angrymerz@gmail.com> 1.0-alt1
- Initial build for Sisyphus.