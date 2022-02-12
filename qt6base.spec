#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : qt6base
Version  : 6.3
Release  : 306
URL      : file:///insilications/apps/qt6base-6.3.tar.gz
Source0  : file:///insilications/apps/qt6base-6.3.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 GPL-2.0 GPL-3.0 MIT
Requires: shared-mime-info
BuildRequires : Vulkan-Headers-dev
BuildRequires : Vulkan-Loader-dev
BuildRequires : Vulkan-Tools
BuildRequires : alsa-lib
BuildRequires : alsa-lib-dev
BuildRequires : alsa-plugins
BuildRequires : alsa-tools
BuildRequires : alsa-tools-dev
BuildRequires : alsa-ucm-conf
BuildRequires : alsa-utils
BuildRequires : appstream-glib
BuildRequires : appstream-glib-dev
BuildRequires : assimp-dev
BuildRequires : atk
BuildRequires : atk-dev
BuildRequires : atkmm-dev
BuildRequires : autogen
BuildRequires : autogen-dev
BuildRequires : automake
BuildRequires : automake-dev
BuildRequires : binutils-dev
BuildRequires : binutils-extras
BuildRequires : bison
BuildRequires : bison-dev
BuildRequires : boost-dev
BuildRequires : breeze
BuildRequires : breeze-gtk
BuildRequires : breeze-icons
BuildRequires : buildreq-cmake
BuildRequires : buildreq-configure
BuildRequires : buildreq-distutils3
BuildRequires : buildreq-gnome
BuildRequires : bzip2-dev
BuildRequires : bzip2-staticdev
BuildRequires : cairo
BuildRequires : cairo-dev
BuildRequires : cairomm-dev
BuildRequires : clr-avx-tools
BuildRequires : clr-rpm-config
BuildRequires : cmake
BuildRequires : cmake-dev
BuildRequires : colord-dev
BuildRequires : curl
BuildRequires : curl-dev
BuildRequires : curl-lib
BuildRequires : dbus
BuildRequires : dbus-dev
BuildRequires : dbus-glib
BuildRequires : dbus-glib-dev
BuildRequires : dbus-python
BuildRequires : dbus-staticdev
BuildRequires : dejagnu
BuildRequires : docbook-utils
BuildRequires : docbook-xml
BuildRequires : docutils
BuildRequires : double-conversion-dev
BuildRequires : double-conversion-staticdev
BuildRequires : doxygen
BuildRequires : eigen-data
BuildRequires : evdev
BuildRequires : expat
BuildRequires : expat-dev
BuildRequires : expat-staticdev
BuildRequires : expect
BuildRequires : extra-cmake-modules
BuildRequires : extra-cmake-modules-data
BuildRequires : fftw-dev
BuildRequires : fftw-staticdev
BuildRequires : findutils
BuildRequires : flex
BuildRequires : fontconfig
BuildRequires : fontconfig-data
BuildRequires : fontconfig-dev
BuildRequires : fonts-clear
BuildRequires : freeglut-dev
BuildRequires : freetype-dev
BuildRequires : freetype-staticdev
BuildRequires : fribidi-dev
BuildRequires : gcc-dev
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : gettext
BuildRequires : gettext-bin
BuildRequires : git
BuildRequires : glib-dev
BuildRequires : glib-staticdev
BuildRequires : glibc-dev
BuildRequires : glibc-libc32
BuildRequires : gobject-introspection
BuildRequires : gobject-introspection-dev
BuildRequires : gperf
BuildRequires : graphite-dev
BuildRequires : graphite-staticdev
BuildRequires : gtk+-dev
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : gtk3
BuildRequires : gtk3-dev
BuildRequires : gtk4
BuildRequires : gtk4-dev
BuildRequires : gtkmm4
BuildRequires : gtkmm4-dev
BuildRequires : gtkmm4-staticdev
BuildRequires : harfbuzz-dev
BuildRequires : harfbuzz-staticdev
BuildRequires : icu4c-dev
BuildRequires : icu4c-staticdev
BuildRequires : inotify-tools
BuildRequires : inotify-tools-dev
BuildRequires : libICE-dev
BuildRequires : libSM-dev
BuildRequires : libX11-data
BuildRequires : libX11-dev
BuildRequires : libX11-lib
BuildRequires : libXScrnSaver
BuildRequires : libXScrnSaver-dev
BuildRequires : libXScrnSaver-lib
BuildRequires : libXau-dev
BuildRequires : libXau-lib
BuildRequires : libXcomposite-dev
BuildRequires : libXcursor-dev
BuildRequires : libXcursor-lib
BuildRequires : libXdamage-dev
BuildRequires : libXdamage-lib
BuildRequires : libXdmcp-dev
BuildRequires : libXdmcp-lib
BuildRequires : libXext-dev
BuildRequires : libXext-lib
BuildRequires : libXfixes-dev
BuildRequires : libXfont2-dev
BuildRequires : libXft-dev
BuildRequires : libXft-lib
BuildRequires : libXi-dev
BuildRequires : libXi-lib
BuildRequires : libXinerama-dev
BuildRequires : libXmu-dev
BuildRequires : libXpm-dev
BuildRequires : libXrandr-dev
BuildRequires : libXrender-dev
BuildRequires : libXrender-lib
BuildRequires : libXres-dev
BuildRequires : libXt-dev
BuildRequires : libXtst-dev
BuildRequires : libXtst-lib
BuildRequires : libXv-dev
BuildRequires : libXxf86vm-dev
BuildRequires : libXxf86vm-lib
BuildRequires : libevent-dev
BuildRequires : libffi-dev
BuildRequires : libffi-staticdev
BuildRequires : libgcrypt-dev
BuildRequires : libinput-dev
BuildRequires : libjpeg-turbo-dev
BuildRequires : libjpeg-turbo-staticdev
BuildRequires : libpng-dev
BuildRequires : libpng-staticdev
BuildRequires : libtool
BuildRequires : libtool-dev
BuildRequires : libwebp
BuildRequires : libwebp-dev
BuildRequires : libwebp-staticdev
BuildRequires : libxcb-dev
BuildRequires : libxcb-lib
BuildRequires : libxml2-dev
BuildRequires : libxml2-staticdev
BuildRequires : libxslt-bin
BuildRequires : libxslt-dev
BuildRequires : llvm
BuildRequires : llvm-data
BuildRequires : llvm-dev
BuildRequires : llvm-lib
BuildRequires : llvm-staticdev
BuildRequires : m4
BuildRequires : md4c-dev
BuildRequires : md4c-staticdev
BuildRequires : mesa-dev
BuildRequires : meson
BuildRequires : ninja
BuildRequires : nodejs-dev
BuildRequires : openblas
BuildRequires : openjdk11
BuildRequires : openmpi-dev
BuildRequires : openssl-dev
BuildRequires : openssl-staticdev
BuildRequires : pacrunner-dev
BuildRequires : pcre-dev
BuildRequires : pcre-staticdev
BuildRequires : pcre2-dev
BuildRequires : pcre2-staticdev
BuildRequires : perl
BuildRequires : perl(XML::Parser)
BuildRequires : perl-Config-General
BuildRequires : perl-Config-Tiny
BuildRequires : perl-Crypt-SSLeay
BuildRequires : perl-DBI
BuildRequires : perl-DateTime-TimeZone
BuildRequires : perl-Encode-Locale
BuildRequires : perl-Error
BuildRequires : perl-File-Listing
BuildRequires : perl-HTML-Parser
BuildRequires : perl-HTML-Tagset
BuildRequires : perl-HTTP-Cookies
BuildRequires : perl-HTTP-Date
BuildRequires : perl-HTTP-Message
BuildRequires : perl-HTTP-Negotiate
BuildRequires : perl-IO-HTML
BuildRequires : perl-LWP-MediaTypes
BuildRequires : perl-LWP-Protocol-https
BuildRequires : perl-Params-Validate
BuildRequires : perl-Test-Simple
BuildRequires : perl-Try-Tiny
BuildRequires : perl-URI
BuildRequires : perl-XML-NamespaceSupport
BuildRequires : perl-XML-Parser
BuildRequires : perl-libwww-perl
BuildRequires : perl-man
BuildRequires : pipewire-dev
BuildRequires : pixman-dev
BuildRequires : pixman-staticdev
BuildRequires : pkg-config
BuildRequires : pkg-config-dev
BuildRequires : pkgconfig(alsa)
BuildRequires : pkgconfig(atspi-2)
BuildRequires : pkgconfig(bluez)
BuildRequires : pkgconfig(cairo)
BuildRequires : pkgconfig(cairo-ft)
BuildRequires : pkgconfig(cunit)
BuildRequires : pkgconfig(dav1d)
BuildRequires : pkgconfig(dbus-1)
BuildRequires : pkgconfig(egl)
BuildRequires : pkgconfig(expat)
BuildRequires : pkgconfig(fontconfig)
BuildRequires : pkgconfig(freetype2)
BuildRequires : pkgconfig(gbm)
BuildRequires : pkgconfig(gconf-2.0)
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : pkgconfig(gl)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(glproto)
BuildRequires : pkgconfig(gobject-2.0)
BuildRequires : pkgconfig(gobject-introspection-1.0)
BuildRequires : pkgconfig(gstreamer-base-1.0)
BuildRequires : pkgconfig(gthread-2.0)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(harfbuzz)
BuildRequires : pkgconfig(harfbuzz-subset)
BuildRequires : pkgconfig(hunspell)
BuildRequires : pkgconfig(icu-i18n)
BuildRequires : pkgconfig(icu-uc)
BuildRequires : pkgconfig(json-c)
BuildRequires : pkgconfig(krb5-gssapi)
BuildRequires : pkgconfig(lcms2)
BuildRequires : pkgconfig(libavcodec)
BuildRequires : pkgconfig(libavformat)
BuildRequires : pkgconfig(libavutil)
BuildRequires : pkgconfig(libbrotlicommon)
BuildRequires : pkgconfig(libbrotlidec)
BuildRequires : pkgconfig(libbrotlienc)
BuildRequires : pkgconfig(libbsd)
BuildRequires : pkgconfig(libdrm)
BuildRequires : pkgconfig(libevent)
BuildRequires : pkgconfig(libinput)
BuildRequires : pkgconfig(libjpeg)
BuildRequires : pkgconfig(liblzma)
BuildRequires : pkgconfig(libpci)
BuildRequires : pkgconfig(libpcre2-16)
BuildRequires : pkgconfig(libpng)
BuildRequires : pkgconfig(libproxy-1.0)
BuildRequires : pkgconfig(libpulse)
BuildRequires : pkgconfig(libpulse-mainloop-glib)
BuildRequires : pkgconfig(libsystemd)
BuildRequires : pkgconfig(libudev)
BuildRequires : pkgconfig(libunwind-generic)
BuildRequires : pkgconfig(libwebp)
BuildRequires : pkgconfig(libwebpdemux)
BuildRequires : pkgconfig(libwebpmux)
BuildRequires : pkgconfig(libxml-2.0)
BuildRequires : pkgconfig(libxslt)
BuildRequires : pkgconfig(libzstd)
BuildRequires : pkgconfig(md4c)
BuildRequires : pkgconfig(mtdev)
BuildRequires : pkgconfig(nettle)
BuildRequires : pkgconfig(nss)
BuildRequires : pkgconfig(opus)
BuildRequires : pkgconfig(osmesa)
BuildRequires : pkgconfig(pciaccess)
BuildRequires : pkgconfig(poppler-cpp)
BuildRequires : pkgconfig(pthread-stubs)
BuildRequires : pkgconfig(re2)
BuildRequires : pkgconfig(sm)
BuildRequires : pkgconfig(valgrind)
BuildRequires : pkgconfig(vpx)
BuildRequires : pkgconfig(wayland-client)
BuildRequires : pkgconfig(wayland-cursor)
BuildRequires : pkgconfig(wayland-egl)
BuildRequires : pkgconfig(wayland-protocols)
BuildRequires : pkgconfig(wayland-server)
BuildRequires : pkgconfig(x11)
BuildRequires : pkgconfig(x11-xcb)
BuildRequires : pkgconfig(xcb)
BuildRequires : pkgconfig(xcb-icccm)
BuildRequires : pkgconfig(xcb-image)
BuildRequires : pkgconfig(xcb-keysyms)
BuildRequires : pkgconfig(xcb-renderutil)
BuildRequires : pkgconfig(xcomposite)
BuildRequires : pkgconfig(xcursor)
BuildRequires : pkgconfig(xdamage)
BuildRequires : pkgconfig(xi)
BuildRequires : pkgconfig(xkbcommon)
BuildRequires : pkgconfig(xkbcommon-x11)
BuildRequires : pkgconfig(xrandr)
BuildRequires : pkgconfig(xrender)
BuildRequires : pkgconfig(xscrnsaver)
BuildRequires : pkgconfig(xshmfence)
BuildRequires : pkgconfig(xtst)
BuildRequires : pkgconfig(zlib)
BuildRequires : protobuf-dev
BuildRequires : pugixml-dev
BuildRequires : pulseaudio
BuildRequires : pulseaudio-dev
BuildRequires : pypi(antlr4_python3_runtime)
BuildRequires : pypi(black)
BuildRequires : pypi(click)
BuildRequires : pypi(flask)
BuildRequires : pypi(google_api_python_client)
BuildRequires : pypi(html5lib)
BuildRequires : pypi(humanfriendly)
BuildRequires : pypi(jinja2)
BuildRequires : pypi(markupsafe)
BuildRequires : pypi(mock)
BuildRequires : pypi(mypy)
BuildRequires : pypi(nose)
BuildRequires : pypi(oauth2client)
BuildRequires : pypi(pillow)
BuildRequires : pypi(portalocker)
BuildRequires : pypi(protobuf)
BuildRequires : pypi(pybind11)
BuildRequires : pypi(pylint)
BuildRequires : pypi(pyparsing)
BuildRequires : pypi(pyyaml)
BuildRequires : pypi(requests)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(six)
BuildRequires : pypi(sphinx)
BuildRequires : pypi(sympy)
BuildRequires : pypi(tox)
BuildRequires : pypi(typing)
BuildRequires : pypi(watchdog)
BuildRequires : pypi-requests
BuildRequires : python3
BuildRequires : python3-core
BuildRequires : python3-dev
BuildRequires : python3-staticdev
BuildRequires : sed
BuildRequires : snappy-dev
BuildRequires : snappy-staticdev
BuildRequires : sqlite-autoconf-dev
BuildRequires : sqlite-autoconf-staticdev
BuildRequires : systemd-dev
BuildRequires : tiff-dev
BuildRequires : tiff-staticdev
BuildRequires : utf8cpp-dev
BuildRequires : util-linux
BuildRequires : util-linux-dev
BuildRequires : wayland
BuildRequires : xcb-util-cursor-dev
BuildRequires : xcb-util-dev
BuildRequires : xcb-util-image-dev
BuildRequires : xcb-util-keysyms-dev
BuildRequires : xcb-util-renderutil-dev
BuildRequires : xcb-util-wm-dev
BuildRequires : xdg-dbus-proxy
BuildRequires : xdg-desktop-portal
BuildRequires : xdg-desktop-portal-dev
BuildRequires : xdg-desktop-portal-gtk
BuildRequires : xdg-desktop-portal-kde
BuildRequires : xdg-user-dirs
BuildRequires : xdg-user-dirs-gtk
BuildRequires : xdg-utils
BuildRequires : xdotool
BuildRequires : xdpyinfo
BuildRequires : xf86-input-evdev
BuildRequires : xf86-input-evdev-dev
BuildRequires : xf86-input-libinput
BuildRequires : xf86-video-amdgpu
BuildRequires : xf86-video-ati
BuildRequires : xf86-video-fbdev
BuildRequires : xf86-video-nouveau
BuildRequires : xf86-video-qxl
BuildRequires : xf86-video-vboxvideo
BuildRequires : xf86-video-vesa
BuildRequires : xf86-video-vmware
BuildRequires : xfontsel
BuildRequires : xhost
BuildRequires : xinit
BuildRequires : xinput
BuildRequires : xkbcomp
BuildRequires : xkeyboard-config
BuildRequires : xkill
BuildRequires : xmlstarlet
BuildRequires : xmodmap
BuildRequires : xorg-server
BuildRequires : xorg-server-dev
BuildRequires : xorgproto
BuildRequires : xorgproto-dev
BuildRequires : xprop
BuildRequires : xrandr
BuildRequires : xrdb
BuildRequires : xrdp
BuildRequires : xrestop
BuildRequires : xscreensaver
BuildRequires : xsel
BuildRequires : xset
BuildRequires : xsetroot
BuildRequires : xvfb-run
BuildRequires : xwd
BuildRequires : xwininfo
BuildRequires : xz
BuildRequires : xz-dev
BuildRequires : xz-staticdev
BuildRequires : yaml-cpp
BuildRequires : yaml-cpp-dev
BuildRequires : yaml-cpp-staticdev
BuildRequires : zlib
BuildRequires : zlib-dev
BuildRequires : zlib-staticdev
BuildRequires : zstd-dev
BuildRequires : zstd-staticdev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
qtokenautomaton is a token generator, that generates a simple, Unicode aware
tokenizer for C++ that uses the Qt API.

%prep
%setup -q -n qt6base-6.3
cd %{_builddir}/qt6base-6.3

%build
unset http_proxy
unset https_proxy
unset no_proxy
export SSL_CERT_FILE=/var/cache/ca-certs/anchors/ca-certificates.crt
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1644656450
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
## altflags1 content
## altflags1
unset ASFLAGS
export QT_HASH_SEED=0
export QT_RCC_SOURCE_DATE_OVERRIDE=1
export CFLAGS="-ggdb3 -ggnu-pubnames -Ofast -DNDEBUG -mno-vzeroupper --param=lto-max-streaming-parallelism=14 -march=native -mtune=native -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -flive-range-shrinkage -flto=14 -fno-plt -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -static-libstdc++ -static-libgcc -Wl,--build-id=sha1 -Wno-inline"
export ASMFLAGS="-ggdb3 -ggnu-pubnames -Ofast -DNDEBUG -mno-vzeroupper --param=lto-max-streaming-parallelism=14 -march=native -mtune=native -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -flive-range-shrinkage -flto=14 -fno-plt -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -static-libstdc++ -static-libgcc -Wl,--build-id=sha1 -Wno-inline"
export CXXFLAGS="-ggdb3 -ggnu-pubnames -Ofast -DNDEBUG -mno-vzeroupper --param=lto-max-streaming-parallelism=14 -march=native -mtune=native -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -flive-range-shrinkage -flto=14 -fno-plt -Wno-error -Wp,-D_REENTRANT -fvisibility-inlines-hidden -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -static-libstdc++ -static-libgcc -Wl,--build-id=sha1 -Wno-inline"
export FCFLAGS="-ggdb3 -ggnu-pubnames -Ofast -DNDEBUG -mno-vzeroupper --param=lto-max-streaming-parallelism=14 -march=native -mtune=native -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -flive-range-shrinkage -flto=14 -fno-plt -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -static-libstdc++ -static-libgcc -Wl,--build-id=sha1 -Wno-inline"
export FFLAGS="-ggdb3 -ggnu-pubnames -Ofast -DNDEBUG -mno-vzeroupper --param=lto-max-streaming-parallelism=14 -march=native -mtune=native -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -flive-range-shrinkage -flto=14 -fno-plt -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -static-libstdc++ -static-libgcc -Wl,--build-id=sha1 -Wno-inline"
export LDFLAGS="-ggdb3 -ggnu-pubnames -Ofast -DNDEBUG -mno-vzeroupper --param=lto-max-streaming-parallelism=14 -march=native -mtune=native -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -flive-range-shrinkage -flto=14 -fno-plt -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -static-libstdc++ -static-libgcc -Wl,--build-id=sha1 -Wno-inline"
export AR=/usr/bin/gcc-ar
export RANLIB=/usr/bin/gcc-ranlib
export NM=/usr/bin/gcc-nm
export MAKEFLAGS=%{?_smp_mflags}
%global _lto_cflags 1
%global _disable_maintainer_mode 1
export CCACHE_DISABLE=true
export CCACHE_NOHASHDIR=true
export CCACHE_CPP2=true
export CCACHE_SLOPPINESS=pch_defines,time_macros,locale,file_stat_matches,file_stat_matches_ctime,include_file_ctime,include_file_mtime,modules,system_headers,clang_index_store,file_macro
export CCACHE_DIR=/var/tmp/ccache
export CCACHE_BASEDIR=/builddir/build/BUILD
export PKG_CONFIG_PATH="/usr/lib64/pkgconfig:/usr/share/pkgconfig"
export LD_LIBRARY_PATH="/usr/local/nvidia/lib64:/usr/local/nvidia/lib64/gbm:/usr/local/nvidia/lib64/vdpau:/usr/local/nvidia/lib64/xorg/modules/drivers:/usr/local/nvidia/lib64/xorg/modules/extensions:/usr/local/cuda/lib64:/usr/lib64/haswell:/usr/lib64/dri:/usr/lib64:/usr/lib:/aot/intel/oneapi/compiler/latest/linux/compiler/lib/intel64_lin:/aot/intel/oneapi/compiler/latest/linux/lib:/aot/intel/oneapi/mkl/latest/lib/intel64:/aot/intel/oneapi/tbb/latest/lib/intel64/gcc4.8:/usr/share:/usr/lib64/wine:/usr/local/nvidia/lib32:/usr/local/nvidia/lib32/vdpau:/usr/lib32:/usr/lib32/wine"
export LIBRARY_PATH="/usr/local/nvidia/lib64:/usr/local/nvidia/lib64/gbm:/usr/local/nvidia/lib64/vdpau:/usr/local/nvidia/lib64/xorg/modules/drivers:/usr/local/nvidia/lib64/xorg/modules/extensions:/usr/local/cuda/lib64:/usr/lib64/haswell:/usr/lib64/dri:/usr/lib64:/usr/lib:/aot/intel/oneapi/compiler/latest/linux/compiler/lib/intel64_lin:/aot/intel/oneapi/compiler/latest/linux/lib:/aot/intel/oneapi/mkl/latest/lib/intel64:/aot/intel/oneapi/tbb/latest/lib/intel64/gcc4.8:/usr/share:/usr/lib64/wine:/usr/local/nvidia/lib32:/usr/local/nvidia/lib32/vdpau:/usr/lib32:/usr/lib32/wine"
export PATH="/usr/lib64/ccache/bin:/usr/local/cuda/bin:/usr/local/nvidia/bin:/usr/bin/haswell:/usr/bin:/usr/sbin"
export CPATH="/usr/local/cuda/include"
export DISPLAY=:0
export __GL_SYNC_TO_VBLANK=1
export __GL_SYNC_DISPLAY_DEVICE=HDMI-0
export VDPAU_NVIDIA_SYNC_DISPLAY_DEVICE=HDMI-0
export LANG=en_US.UTF-8
export XDG_CONFIG_DIRS=/usr/share/xdg:/etc/xdg
export XDG_SEAT=seat0
export XDG_SESSION_TYPE=tty
export XDG_CURRENT_DESKTOP=KDE
export XDG_SESSION_CLASS=user
export XDG_VTNR=1
export XDG_SESSION_ID=1
export XDG_RUNTIME_DIR=/run/user/1000
export XDG_DATA_DIRS=/usr/local/share:/usr/share
export KDE_SESSION_VERSION=5
export KDE_SESSION_UID=1000
export KDE_FULL_SESSION=true
export KDE_APPLICATIONS_AS_SCOPE=1
export VDPAU_DRIVER=nvidia
export LIBVA_DRIVER_NAME=vdpau
export LIBVA_DRIVERS_PATH=/usr/lib64/dri
export GTK_RC_FILES=/etc/gtk/gtkrc
export FONTCONFIG_PATH="/usr/share/defaults/fonts"
export GTK_IM_MODULE="xim"
export QT_IM_MODULE="cedilla"
export FREETYPE_PROPERTIES="truetype:interpreter-version=40"
export NO_AT_BRIDGE=1
export GTK_A11Y=none
export PLASMA_USE_QT_SCALING=1
export QT_AUTO_SCREEN_SCALE_FACTOR=0
export QT_ENABLE_HIGHDPI_SCALING=0
export QT_FONT_DPI=88
export GTK_USE_PORTAL=1
export DESKTOP_SESSION=plasma
## altflags1 end
%cmake ..   -G Ninja \
-DCMAKE_BUILD_TYPE=None \
-DCMAKE_INSTALL_PREFIX=/usr \
-DINSTALL_SYSCONFDIR=/usr/share \
-DCMAKE_INSTALL_SYSCONFDIR=/usr/share \
-DINSTALL_LIBDIR=/usr/lib64 \
-DCMAKE_INSTALL_LIBDIR=/usr/lib64 \
-DINSTALL_ARCHDATADIR:STRING=/usr/lib64/qt6 \
-DINSTALL_BINDIR:STRING=/usr/lib64/bin \
-DINSTALL_DATADIR:STRING=/usr/share/qt6 \
-DINSTALL_DESCRIPTIONSDIR:STRING=/usr/share/qt6/modules \
-DINSTALL_DOCDIR:STRING=/usr/share/qt6/doc \
-DINSTALL_EXAMPLESDIR:STRING=/usr/share/qt6/examples \
-DINSTALL_INCLUDEDIR:STRING=/usr/include/qt6 \
-DINSTALL_LIBEXECDIR:STRING=/usr/lib64/qt6/libexec \
-DINSTALL_MKSPECSDIR:STRING=/usr/lib64/qt6/mkspecs \
-DINSTALL_PLUGINSDIR:STRING=/usr/lib64/qt6/plugins \
-DINSTALL_QMLDIR:STRING=/usr/lib64/qt6/qml \
-DINSTALL_TESTSDIR:STRING=/usr/share/qt6/tests \
-DINSTALL_TRANSLATIONSDIR:STRING=/usr/share/qt6/translations \
-DCMAKE_JOB_POOLS:STRING="compile=15;link=1" \
-DCMAKE_JOB_POOL_COMPILE:STRING="compile" \
-DCMAKE_JOB_POOL_LINK:STRING="link" \
-DCMAKE_NM=/usr/bin/gcc-nm \
-DCMAKE_RANLIB=/usr/bin/gcc-ranlib \
-DCMAKE_AR=/usr/bin/gcc-ar \
-DCMAKE_VERBOSE_MAKEFILE:BOOL=ON \
-DBUILD_SHARED_LIBS:BOOL=OFF \
-DWARNINGS_ARE_ERRORS:BOOL=OFF \
-DFEATURE_rpath:BOOL=OFF \
-DFEATURE_separate_debug_info:BOOL=OFF \
-DFEATURE_force_asserts:BOOL=OFF \
-DFEATURE_developer_build:BOOL=OFF \
-DFEATURE_journald:BOOL=ON \
-DFEATURE_gc_binaries:BOOL=OFF \
-DFEATURE_brotli:BOOL=OFF \
-DFEATURE_relocatable:BOOL=OFF \
-DFEATURE_cups:BOOL=OFF \
-DFEATURE_avx512bw:BOOL=OFF \
-DFEATURE_avx512cd:BOOL=OFF \
-DFEATURE_avx512dq:BOOL=OFF \
-DFEATURE_avx512er:BOOL=OFF \
-DFEATURE_avx512f:BOOL=OFF \
-DFEATURE_avx512ifma:BOOL=OFF \
-DFEATURE_avx512pf:BOOL=OFF \
-DFEATURE_avx512vbmi:BOOL=OFF \
-DFEATURE_avx512vl:BOOL=OFF \
-DQT_USE_DEFAULT_CMAKE_OPTIMIZATION_FLAGS:BOOL=ON \
-DUSE_DEFAULT_CMAKE_OPTIMIZATION_FLAGS:BOOL=ON \
-DFEATURE_enable_new_dtags:BOOL=ON \
-DFEATURE_avx:BOOL=ON \
-DFEATURE_avx2:BOOL=ON \
-DINPUT_dbus=linked \
-DFEATURE_dbus_linked:BOOL=ON \
-DINPUT_openssl=linked \
-DFEATURE_openssl_linked:BOOL=ON \
-DFEATURE_reduce_relocations:BOOL=ON \
-DFEATURE_static_runtime:BOOL=ON \
-DFEATURE_pkg_config:BOOL=ON \
-DFEATURE_gui:BOOL=ON \
-DFEATURE_widgets:BOOL=ON \
-DFEATURE_dbus:BOOL=ON \
-DFEATURE_accessibility:BOOL=ON \
-DFEATURE_glib:BOOL=ON \
-DFEATURE_inotify:BOOL=ON \
-DFEATURE_pcre2:BOOL=ON \
-DFEATURE_ssl:BOOL=ON \
-DFEATURE_pdf:BOOL=ON \
-DFEATURE_fontconfig:BOOL=ON \
-DFEATURE_gtk3:BOOL=ON \
-DINPUT_opengl:BOOL=ON \
-DFEATURE_egl:BOOL=ON \
-DFEATURE_egl_x11:BOOL=ON \
-DFEATURE_vulkan:BOOL=ON \
-DFEATURE_xcb_xlib:BOOL=ON \
-DFEATURE_directfb:BOOL=OFF \
-DFEATURE_eglfs:BOOL=ON \
-DFEATURE_gbm:BOOL=ON \
-DFEATURE_kms:BOOL=ON \
-DFEATURE_linuxfb:BOOL=ON \
-DFEATURE_xcb:BOOL=ON \
-DFEATURE_libudev:BOOL=ON \
-DFEATURE_evdev=ON \
-DFEATURE_libinput:BOOL=ON \
-DFEATURE_mtdev:BOOL=ON \
-DFEATURE_xkbcommon:BOOL=ON \
-DFEATURE_gif:BOOL=ON \
-DFEATURE_ico:BOOL=ON \
-DFEATURE_libpng:BOOL=ON \
-DFEATURE_icu:BOOL=ON \
-DFEATURE_xml:BOOL=ON \
-DFEATURE_zstd:BOOL=ON \
-DFEATURE_libjpeg:BOOL=ON \
-DFEATURE_libmd4c:BOOL=ON \
-DFEATURE_system_doubleconversion:BOOL=ON \
-DFEATURE_system_freetype:BOOL=ON \
-DFEATURE_system_harfbuzz:BOOL=ON \
-DFEATURE_system_jpeg:BOOL=ON \
-DFEATURE_system_png:BOOL=ON \
-DFEATURE_system_xcb_xinput:BOOL=ON \
-DFEATURE_system_webp:BOOL=ON \
-DFEATURE_system_zlib:BOOL=ON \
-DFEATURE_system_pcre2:BOOL=ON \
-DFEATURE_system_zlib:BOOL=ON \
-DFEATURE_system_sqlite:BOOL=ON \
-DBUILD_qtwayland:BOOL=OFF \
-DQT_BUILD_TESTS:BOOL:BOOL=OFF \
-DQT_BUILD_BENCHMARKS:BOOL:BOOL=OFF \
-DQT_BUILD_EXAMPLES:BOOL:BOOL=OFF \
-DCMAKE_CXX_LINK_PIE_SUPPORTED:BOOL=OFF \
-DQT_DISABLE_RPATH:BOOL=OFF \
-DCMAKE_AUTOMOC_PATH_PREFIX:BOOL=ON \
-DCMAKE_C_FLAGS:STRING="-ggdb3 -ggnu-pubnames -Ofast -DNDEBUG -mno-vzeroupper --param=lto-max-streaming-parallelism=14 -march=native -mtune=native -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -flive-range-shrinkage -flto=14 -fno-plt -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -static-libstdc++ -static-libgcc -Wl,--build-id=sha1 -Wno-inline" \
-DCMAKE_CXX_FLAGS:STRING="-ggdb3 -ggnu-pubnames -Ofast -DNDEBUG -mno-vzeroupper --param=lto-max-streaming-parallelism=14 -march=native -mtune=native -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -flive-range-shrinkage -flto=14 -fno-plt -Wno-error -Wp,-D_REENTRANT -fvisibility-inlines-hidden -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -static-libstdc++ -static-libgcc -Wl,--build-id=sha1 -Wno-inline" \
-DCMAKE_EXE_LINKER_FLAGS:STRING="-ggdb3 -ggnu-pubnames -Ofast -DNDEBUG -mno-vzeroupper --param=lto-max-streaming-parallelism=14 -march=native -mtune=native -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -flive-range-shrinkage -flto=14 -fno-plt -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -static-libstdc++ -static-libgcc -Wl,--build-id=sha1 -Wno-inline" \
-DCMAKE_MODULE_LINKER_FLAGS:STRING="-ggdb3 -ggnu-pubnames -Ofast -DNDEBUG -mno-vzeroupper --param=lto-max-streaming-parallelism=14 -march=native -mtune=native -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -flive-range-shrinkage -flto=14 -fno-plt -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -static-libstdc++ -static-libgcc -Wl,--build-id=sha1 -Wno-inline" \
-DCMAKE_SHARED_LINKER_FLAGS:STRING="-ggdb3 -ggnu-pubnames -Ofast -DNDEBUG -mno-vzeroupper --param=lto-max-streaming-parallelism=14 -march=native -mtune=native -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -flive-range-shrinkage -flto=14 -fno-plt -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -static-libstdc++ -static-libgcc -Wl,--build-id=sha1 -Wno-inline"
## make_prepend64 content
sd "\-D\-DDBUS_STATIC_BUILD" -- "-DDBUS_STATIC_BUILD" $(fd -uu --glob *.ninja)
sd "\-D\-DDBUS_STATIC_BUILD" -- "-DDBUS_STATIC_BUILD" $(fd -uu --glob *.ninja)
sd "\-DDBUS_STATIC_BUILD" -- "DBUS_STATIC_BUILD" $(fd -uu --glob *.json)
## make_prepend64 end
## make_macro content
ninja --verbose
## make_macro end
popd

%install
export SOURCE_DATE_EPOCH=1644656450
rm -rf %{buildroot}
export GCC_IGNORE_WERROR=1
## altflags1 content
## altflags1
unset ASFLAGS
export QT_HASH_SEED=0
export QT_RCC_SOURCE_DATE_OVERRIDE=1
export CFLAGS="-ggdb3 -ggnu-pubnames -Ofast -DNDEBUG -mno-vzeroupper --param=lto-max-streaming-parallelism=14 -march=native -mtune=native -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -flive-range-shrinkage -flto=14 -fno-plt -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -static-libstdc++ -static-libgcc -Wl,--build-id=sha1 -Wno-inline"
export ASMFLAGS="-ggdb3 -ggnu-pubnames -Ofast -DNDEBUG -mno-vzeroupper --param=lto-max-streaming-parallelism=14 -march=native -mtune=native -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -flive-range-shrinkage -flto=14 -fno-plt -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -static-libstdc++ -static-libgcc -Wl,--build-id=sha1 -Wno-inline"
export CXXFLAGS="-ggdb3 -ggnu-pubnames -Ofast -DNDEBUG -mno-vzeroupper --param=lto-max-streaming-parallelism=14 -march=native -mtune=native -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -flive-range-shrinkage -flto=14 -fno-plt -Wno-error -Wp,-D_REENTRANT -fvisibility-inlines-hidden -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -static-libstdc++ -static-libgcc -Wl,--build-id=sha1 -Wno-inline"
export FCFLAGS="-ggdb3 -ggnu-pubnames -Ofast -DNDEBUG -mno-vzeroupper --param=lto-max-streaming-parallelism=14 -march=native -mtune=native -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -flive-range-shrinkage -flto=14 -fno-plt -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -static-libstdc++ -static-libgcc -Wl,--build-id=sha1 -Wno-inline"
export FFLAGS="-ggdb3 -ggnu-pubnames -Ofast -DNDEBUG -mno-vzeroupper --param=lto-max-streaming-parallelism=14 -march=native -mtune=native -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -flive-range-shrinkage -flto=14 -fno-plt -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -static-libstdc++ -static-libgcc -Wl,--build-id=sha1 -Wno-inline"
export LDFLAGS="-ggdb3 -ggnu-pubnames -Ofast -DNDEBUG -mno-vzeroupper --param=lto-max-streaming-parallelism=14 -march=native -mtune=native -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -flive-range-shrinkage -flto=14 -fno-plt -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -static-libstdc++ -static-libgcc -Wl,--build-id=sha1 -Wno-inline"
export AR=/usr/bin/gcc-ar
export RANLIB=/usr/bin/gcc-ranlib
export NM=/usr/bin/gcc-nm
export MAKEFLAGS=%{?_smp_mflags}
%global _lto_cflags 1
%global _disable_maintainer_mode 1
export CCACHE_DISABLE=true
export CCACHE_NOHASHDIR=true
export CCACHE_CPP2=true
export CCACHE_SLOPPINESS=pch_defines,time_macros,locale,file_stat_matches,file_stat_matches_ctime,include_file_ctime,include_file_mtime,modules,system_headers,clang_index_store,file_macro
export CCACHE_DIR=/var/tmp/ccache
export CCACHE_BASEDIR=/builddir/build/BUILD
export PKG_CONFIG_PATH="/usr/lib64/pkgconfig:/usr/share/pkgconfig"
export LD_LIBRARY_PATH="/usr/local/nvidia/lib64:/usr/local/nvidia/lib64/gbm:/usr/local/nvidia/lib64/vdpau:/usr/local/nvidia/lib64/xorg/modules/drivers:/usr/local/nvidia/lib64/xorg/modules/extensions:/usr/local/cuda/lib64:/usr/lib64/haswell:/usr/lib64/dri:/usr/lib64:/usr/lib:/aot/intel/oneapi/compiler/latest/linux/compiler/lib/intel64_lin:/aot/intel/oneapi/compiler/latest/linux/lib:/aot/intel/oneapi/mkl/latest/lib/intel64:/aot/intel/oneapi/tbb/latest/lib/intel64/gcc4.8:/usr/share:/usr/lib64/wine:/usr/local/nvidia/lib32:/usr/local/nvidia/lib32/vdpau:/usr/lib32:/usr/lib32/wine"
export LIBRARY_PATH="/usr/local/nvidia/lib64:/usr/local/nvidia/lib64/gbm:/usr/local/nvidia/lib64/vdpau:/usr/local/nvidia/lib64/xorg/modules/drivers:/usr/local/nvidia/lib64/xorg/modules/extensions:/usr/local/cuda/lib64:/usr/lib64/haswell:/usr/lib64/dri:/usr/lib64:/usr/lib:/aot/intel/oneapi/compiler/latest/linux/compiler/lib/intel64_lin:/aot/intel/oneapi/compiler/latest/linux/lib:/aot/intel/oneapi/mkl/latest/lib/intel64:/aot/intel/oneapi/tbb/latest/lib/intel64/gcc4.8:/usr/share:/usr/lib64/wine:/usr/local/nvidia/lib32:/usr/local/nvidia/lib32/vdpau:/usr/lib32:/usr/lib32/wine"
export PATH="/usr/lib64/ccache/bin:/usr/local/cuda/bin:/usr/local/nvidia/bin:/usr/bin/haswell:/usr/bin:/usr/sbin"
export CPATH="/usr/local/cuda/include"
export DISPLAY=:0
export __GL_SYNC_TO_VBLANK=1
export __GL_SYNC_DISPLAY_DEVICE=HDMI-0
export VDPAU_NVIDIA_SYNC_DISPLAY_DEVICE=HDMI-0
export LANG=en_US.UTF-8
export XDG_CONFIG_DIRS=/usr/share/xdg:/etc/xdg
export XDG_SEAT=seat0
export XDG_SESSION_TYPE=tty
export XDG_CURRENT_DESKTOP=KDE
export XDG_SESSION_CLASS=user
export XDG_VTNR=1
export XDG_SESSION_ID=1
export XDG_RUNTIME_DIR=/run/user/1000
export XDG_DATA_DIRS=/usr/local/share:/usr/share
export KDE_SESSION_VERSION=5
export KDE_SESSION_UID=1000
export KDE_FULL_SESSION=true
export KDE_APPLICATIONS_AS_SCOPE=1
export VDPAU_DRIVER=nvidia
export LIBVA_DRIVER_NAME=vdpau
export LIBVA_DRIVERS_PATH=/usr/lib64/dri
export GTK_RC_FILES=/etc/gtk/gtkrc
export FONTCONFIG_PATH="/usr/share/defaults/fonts"
export GTK_IM_MODULE="xim"
export QT_IM_MODULE="cedilla"
export FREETYPE_PROPERTIES="truetype:interpreter-version=40"
export NO_AT_BRIDGE=1
export GTK_A11Y=none
export PLASMA_USE_QT_SCALING=1
export QT_AUTO_SCREEN_SCALE_FACTOR=0
export QT_ENABLE_HIGHDPI_SCALING=0
export QT_FONT_DPI=88
export GTK_USE_PORTAL=1
export DESKTOP_SESSION=plasma
## altflags1 end
pushd clr-build
%ninja_install
popd
## install_append content
install -dm 0755 %{buildroot}/usr/bin/
pushd %{buildroot}/usr/lib64/bin
for i in * ; do
    ln -sf /usr/lib64/bin/$i %{buildroot}/usr/bin/${i}-qt6
done
popd
install -dm 0755 %{buildroot}/usr/lib64/haswell/
pushd %{buildroot}/usr/lib64/haswell/
for lib in ../lib*.so*; do
    ln -sf $lib %{buildroot}/usr/lib64/haswell/;
done
popd
## install_append end

%files
%defattr(-,root,root,-)
