#! /usr/bin/python3
# -*- coding: utf-8 -*-

# Translation

import os
import gettext
import locale
APP = "hsuite"
WHERE_AM_I = os.path.abspath(os.path.dirname(__file__))
LOCALE_DIR = os.path.join(WHERE_AM_I, 'translations/mo')
locale.setlocale(locale.LC_ALL, locale.getlocale())
locale.bindtextdomain(APP, LOCALE_DIR)
gettext.bindtextdomain(APP, LOCALE_DIR)
gettext.textdomain(APP)
_ = gettext.gettext

# Descriptions

opera = _("""Opera

Fast, secure, easy-to-use browser
Try the Opera browser - now with a built-in ad blocker, battery saver and free VPN.

Opera is one of the most underrated browsers out yet. However, it's one of the bests, if not the best. It's based on Chromium, so it's basicly Chrome on steroids. It's faster, lighter, more secure and more productive. The Opera Sync is the best on the market, and the sidebar with integrated messengers is really productive.

Give the web browser of the future a try!
""")
chrome = _("""Google Chrome

Google Chrome is the most popular browser nowadays for Android and PC also. It's reliable, stable and fast, however, you know, Google doesn't respect your privacy sometimes...

But at the end of the day, Chrome is still one of the best choices
if you'd like to use a well-known, cross platform browser.
""")
web = _("""Gnome Web

Gnome Web is a simple and lightweight yet powerful browser. It only supports Linux, so it isn't the best for you if you would like to have your settings and pages synced on the go. It is the best for old hardware and laptops (bacause it is very battery friendly). It could be a good choice if you are coming from mac, because its user interface is similar to Safari.

Note: It also the only browser that supports touchpad gestures for Linux out of the box.
""")
firefox = _("""Mozilla Firefox

Meet Firefox Quantum. Fast for good.

Features:

    - A powerful, new engine that’s built for rapidfire performance.
    - Better, faster page loading that uses less computer memory.
    - Gorgeous design and smart features for intelligent browsin

Firefox is made by Mozilla, the non-profit champions of a healthy internet.
Mozilla also tackles issues like privacy, misinformation and trolling by investing in fellowships, campaigns and new technologies designed to make the internet healthier.
""")
vivaldi = _("""Vivaldi

A browser should adapt to you, not the other way around.

We believe that many people want to customize and tweak every square inch of their browser to make it their own. They want access to advanced tools without sacrificing performance or security. And they want to be heard.

"We’re building a browser that is powerful, personal and flexible. A browser that adapts to you, not the other way around."

This is the philosophy of the Vivaldi team. The CEO was also the founder of Opera.

I recommend you to try this browser out. (Android version is in beta stage, avilable from the Play store)
""")
edge = _("""Microsoft Edge

Microsoft Edge was originally announced as a replacement for Internet Explorer, which had been the default browser in Windows operating systems since 1995. However, both Edge and Internet Explorer are included with Windows 10, with Edge simply acting as the default browser.

Microsoft Edge requires at least 1 gigabyte of memory. The browser offers better security and better organization than Internet Explorer, as well as a reading list which is similar to (but separate from) bookmarks.

Now Chromium based Edge browser is on the way, and hopefully it is arriving to Linux between 2020 and 2021.
""")
wps = _("""WPS Office

WPS Office is the complete free office suite, integrates all office word processor functions: Word, Presentation, Spreadsheet, PDF, and fully compatible with Microsoft Word, Excel, PowerPoint, Google Doc and Adobe PDF format. If you need to use advanced features(e.: PDF2WORD, more cloud storage space), you can subscribe Preminum.

The aim of WPS Office is to provide you one-stop working solution since 1989. Various of office tools and unique and intuitive UI design ensures you enjoy the best office experience. You could easy to do all office documents processing on-the-go on Windows PC. WPS Office suite allows you can create, view, edit and share office documents.

It's the best free MS Office alternative for Linux in my opinion.
""")
libreoffice = _("""Libreoffice

LibreOffice is developed by users who, just like you, believe in the principles of Free Software and in sharing their work with the world in non-restrictive ways. At the core of these principles are the four essential freedoms and the tenets of The Document Foundation's Next Decade Manifesto.

We believe that users should have the freedom to run, copy, distribute, study, change and improve the software that we distribute. While we do offer no-cost downloads of the LibreOffice suite of programs, Free Software is first and foremost a matter of liberty, not price. We campaign for these freedoms because we believe that everyone deserves them.
""")
onlyoffice = _("""Only Office

ONLYOFFICE Desktop Editors is a free open source office suite that combines text, spreadsheet and presentation editors allowing to create, view and edit documents stored on your Windows/Linux PC or Mac without an Internet connection. It is fully compatible with Office Open XML formats: .docx, .xlsx, .pptx.

The ONLYOFFICE desktop suite pack allows extending the functionality with the pre-installed plugins, e. you can insert special symbols and ClipArts, edit pictures, translate text, send documents as mail attachments right from the editors, etc.

The suite also provides quick access to broad collaborative capabilities. Users are able to switch to the online mode by connecting to the cloud (ONLYOFFICE cloud, Nextcloud, ownCloud) and collaborate on documents with the team in real time.
""")
officeonline = _("""Microsoft Office Online

Microsoft Office Online can serve as a free Microsoft Office alternative, as it lets you edit and share files created in a word processor, spreadsheet, and presentation program, as well access MS Outlook and OneNote.

Everything done through Microsoft Office Online is performed through a web browser and saved online so you can access the files from anywhere.
""")
gsuite = _("""Google G Suite

G Suite—formerly known as Google Apps for Work—is a Software as a Service (SaaS) product that groups all the cloud-based productivity and collaboration tools developed by Google for businesses, institutes, and nonprofits. Included with every subscription you get access to custom Gmail addresses, Docs, Sheets, Slides, Calendar, Drive, Sites, and so much more.
""")
freeoffice = _("""Softmaker Free Office

SoftMaker Office is an office suite developed since 1987 by the German company SoftMaker Software GmbH, Nurember SoftMaker is available as a one-time purchase option, in Standard and Professional editions, as well as a subscription-based version known as SoftMaker Office NX (available as Home and Universal editions).

A freeware version is released as well, under the name of SoftMaker FreeOffice. FreeOffice supersedes SoftMaker Office 2006 and 2008, which were released as freeware after originally being available for purchase.
""")
gedit = _("""Gedit

It is is the default text editor of the GNOME desktop environment and part of the GNOME Core Applications. Designed as a general-purpose text editor, gedit emphasizes simplicity and ease of use, with a clean and simple GUI, according to the philosophy of the GNOME project. It includes tools for editing source code and structured text such as markup languages.

It is free and open-source software subject to the requirements of the GNU General Public License version 2 or later.

gedit is also available for Mac OS X and Microsoft Windows.

Personally, I use gedit with extensions for programming, HSuite has been also written in gedit until v0.4.
""")
emacs = _("""GNU Emacs

EMACS (Editor MACroS) is a family of text editors that are characterized by their extensibility. The manual for the most widely used variant, GNU Emacs, describes it as "the extensible, customizable, self-documenting, real-time display editor". Development of the first Emacs began in the mid-1970s, and work on its direct descendant, GNU Emacs, continues actively as of 2019.

Emacs has over 10,000 built-in commands and its user interface allows the user to combine these commands into macros to automate work. Implementations of Emacs typically feature a dialect of the Lisp programming language that provides a deep extension capability, allowing users and developers to write new commands and applications for the editor. Extensions have been written to manage email, files, outlines, and RSS feeds, as well as clones of ELIZA, Pong, Conway's Life, Snake and Tetris.
""")
code = _("""Visual Studio Code

Visual Studio Code is a source-code editor developed by Microsoft for Windows, Linux and macOS. It includes support for debugging, embedded Git control and GitHub, syntax highlighting, intelligent code completion, snippets, and code refactorin It is highly customizable, allowing users to change the theme, keyboard shortcuts, preferences, and install extensions that add additional functionality. The source code is free and open source and released under the permissive MIT License. The compiled binaries are freeware and free for private or commercial use.

Since v0.5 I'm writing HSuite in VSCode. It's a minimalistic, simple and fully featured program somewhere between a simple text editor and a complete IDE.
""")
atom = _("""Atom Editor

Atom is a free and open-source text and source code editor for macOS, Linux, and Microsoft Windows with support for plug-ins written in Node.js, and embedded Git Control, developed by GitHub. Atom is a desktop application built using web technologies. Most of the extending packages have free software licenses and are community-built and maintained. Atom is based on Electron (formerly known as Atom Shell), a framework that enables cross-platform desktop applications using Chromium and Node.js. It is written in CoffeeScript and Less.
""")
stext = _("""Sublime Text Editor

Sublime Text is a proprietary cross-platform source code editor with a Python application programming interface (API). It natively supports many programming languages and markup languages, and functions can be added by users with plugins, typically community-built and maintained under free-software licenses.
""")
geany = _("""Geany

Geany is a lightweight GUI text editor using Scintilla and GTK+, including basic IDE features. It is designed to have short load times, with limited dependency on separate packages or external libraries on Linux. It has been ported to a wide range of operating systems, such as BSD, Linux, macOS, Solaris and Windows. The Windows port lacks an embedded terminal window; also missing from the Windows version are the external development tools present under Unix, unless installed separately by the user. Among the supported programming languages and markup languages are C, C++, C#, Java, JavaScript, PHP, HTML, LaTeX, CSS, Python, Perl, Ruby, Pascal, Haskell, Erlang, Vala and many others.
""")
skype = _("""Skype

Skype is for connecting with the people that matter most in your life and work. It's built for both one-on-one and group conversations and works wherever you are – via mobile, PC, Xbox and Alexa. Skype messaging and HD voice and video calling will help you share experiences and get things done with others.

With Skype, you can have meetings and create great things with your workgroup, share a story or celebrate a birthday with friends and family, and learn a new skill or hobby with a teacher. It’s free to use Skype – to send messages and have audio and video calls with groups of up to 50 people!

If you pay a little, you can do more things, in more ways, with more people – like call phones or SMS messages. You can pay as you go or buy a subscription, whatever works for you.

Try Skype out today and start adding your friends, family and colleagues. They won’t be hard to find; hundreds of millions of people are already using Skype to do all sorts of things together.
""")
discord = _("""Discord

Discord is a proprietary freeware VoIP application and digital distribution platform—designed initially for the video gaming community—that specializes in text, image, video and audio communication between users in a chat channel. Discord runs on Windows, macOS, Android, iOS, Linux, and in web browsers. As of 21 July 2019, there are over 250 million unique users of the software.
""")
telegram = _("""Telegram

Telegram is a cloud-based instant messaging and voice over IP service. Telegram client apps are available for Android, iOS, Windows Phone, Windows NT, macOS and Linux. Users can send messages and exchange photos, videos, stickers, audio and files of any type.

Telegram's client-side code is open-source software but the source code for recent versions is not always immediately published, whereas its server-side code is closed-source and proprietary. The service also provides APIs to independent developers. In March 2018, Telegram stated that it had 200 million monthly active users.
""")
signal = _("""Signal

Signal is a cross-platform encrypted messaging service developed by the Signal Foundation and Signal Messenger LLC. It uses the Internet to send one-to-one and group messages, which can include files, voice notes, images and videos. Its mobile apps can also make one-to-one voice and video calls, and the Android version can optionally function as an SMS app.

Signal uses standard cellular telephone numbers as identifiers and uses end-to-end encryption to secure all communications to other Signal users. The apps include mechanisms by which users can independently verify the identity of their contacts and the integrity of the data channel.

All Signal software are free and open-source. The clients are published under the GPLv3 license, while the server code is published under the AGPLv3 license. The non-profit Signal Foundation was launched in February 2018 with an initial funding of $50 million.
""")
hexchat = _("""HexChat

HexChat is an Internet Relay Chat client (IRC), forked from XChat. It has a choice of a tabbed document interface or tree interface, support for multiple servers, and numerous configuration options. Both command-line and graphical versions were available.
""")
franz = _("""Franz

Franz Messaging app is one of my top best messaging apps for linux platform. It’s a free, simple to use chat app that combines all the various chat & messaging services features into one promising application.

Currently it supports
    ~ Slack
    ~ WhatsApp
    ~ WeChat
    ~ HipChat
    ~ Facebook Messenger
    ~ Telegram
    ~ Google Hangouts
    ~ GroupMe
    ~ Skype
    ~ Gmail
    ~ Google Messages
    ~ Google Calendar
    ~ Discord
    ~ Linkedin
    ~ Outlook
    ~ and many more.

At the moment, you are only able to install and run the app on the following operating systems “Mac, Windows & Linux”.

If you have multiple business and private accounts, then Franz Messaging app will allow you to add all your accounts so its easy to manage them from a single dashboard. What this means is, you could add / manage five different Facebook Messenger accounts all at once.
""")
ad = _("""0 A.D.

The best strategic game for Linux (in my opinion)

0 A.D. (pronounced "zero ey-dee") is a free, open-source, cross-platform real-time strategy (RTS) game of ancient warfare. In short, it is a historically-based war/economy game that allows players to relive or rewrite the history of Western civilizations, focusing on the years between 500 B.C. and 500 A.D. The project is highly ambitious, involving state-of-the-art 3D graphics, detailed artwork, sound, and a flexible and powerful custom-built game engine.

It also supports online and LAN multiplayer, custom map creation, adding mods to the game and if you would like to take part in the development you can do that also.
""")
tux = _("""SuperTux

The game, that every hardcore Linux users should play out.

SuperTux is a free and open-source two-dimensional platform video game published under the GNU General Public License (GPL).[1] The game was inspired by Nintendo's Super Mario Bros. series; instead of Mario, the hero in the game is Tux, the official mascot of the Linux kernel.
""")
lutris = _("""Lutris

Lutris is an Open Source gaming platform for Linux. It installs and launches games so you can start playing without the hassle of setting up your games. Get your games from GOG, Steam, Battle.net, Origin, Uplay and many other sources running on any Linux powered gaming machine.
""")
pol = _("""Play On Linux

One of the best ways to play Windows games on Linux.

PlayOnLinux is a piece of software which allows you to easily install and use numerous games and apps designed to run with Microsoft® Windows®.
Few games are compatible with GNU/Linux at the moment and it certainly is a factor preventing the migration to this system. PlayOnLinux brings a cost-free, accessible and efficient solution to this problem.
""")
steam = _("""Steam

The overall best when it comes to gaming on every platform.

Steam is the ultimate game platform, also for Linux. It offers Steam Play feature. Steam Play allows you to purchase your games once and play anywhere. Whether you have purchased your Steam Play enabled game on a Mac or PC (both Windows and Linux), you will be able to play on the other platform free of charge. So a lots of Windows only games can be played on Linux without problems.
""")
minecraft = _("""Minecraft

Everyone knows this game... But if you don't, here's a short description.

Minecraft is a sandbox video game created by Swedish game developer Markus Persson and released by Mojang in 2011. The game allows players to build with a variety of different blocks in a 3D procedurally generated world, requiring creativity from players. Other activities in the game include exploration, resource gathering, crafting, and combat. Multiple game modes that change gameplay are available, including—but not limited to—a survival mode, in which players must acquire resources to build the world and maintain health, and a creative mode, where players have unlimited resources to build with. The Java Edition of the game allows players to modify the game with mods to create new gameplay mechanics, items, textures and assets. In September 2014, Microsoft announced a deal to buy Mojang and the Minecraft intellectual property for US$2.5 billion, with the acquisition completed two months later.'
""")
tuxkart = _("""SuperTuxKart

Karts. Nitro. Action! SuperTuxKart is a 3D open-source arcade racer with a variety characters, tracks, and modes to play. Our aim is to create a game that is more fun than realistic, and provide an enjoyable experience for all ages.

In Story mode, you must face the evil Nolok, and defeat him in order to make the Mascot Kingdom safe once again! You can race by yourself against the computer, compete in several Grand Prix cups, or try to beat your fastest time in Time Trial mode. You can also race or battle with up to eight friends on a single computer, play on a local network or play online with other players all over the world.
""")
popsicle = _("""Popsicle

Popsicle is a lightweight open source USB image writer tool written in Rust by System76, the company behind a lots of outsandingly great Linux Desktops/Laptops and the heavy customized Ubuntu based distro, Pop!_OS.
""")
woeusb = _("""WoeUSB

Write Windows ISO to removable storage.

WoeUSB is Linux tool for creating Windows USB stick installer from a real Windows DVD or an image. It contains two programs, woeusb and woeusbgui. It’s a fork of Congelli501’s WinUSB software which received its last update in 2012.

woeusb is a CLI utility that does the actual creation of a bootable Windows installation USB storage device from either an existing Windows installation or a disk image. woeusbgui (as the name suggests,) is a woeusb GUI wrapper based on WxWidgets.
""")
wine = _("""Wine

Run Windows programs on Linux

Wine (originally an acronym for "Wine Is Not an Emulator") is a compatibility layer capable of running Windows applications on several POSIX-compliant operating systems, such as Linux, macOS, & BSD. Instead of simulating internal Windows logic like a virtual machine or emulator, Wine translates Windows API calls into POSIX calls on-the-fly, eliminating the performance and memory penalties of other methods and allowing you to cleanly integrate Windows applications into your desktop.
""")
vbox = _("""Oracle Virtualbox

Run virtual machines on your PC

A VirtualBox or VB is a software virtualization package that installs on an operating system as an application. VirtualBox allows additional operating systems to be installed on it, as a Guest OS, and run in a virtual environment. In 2010, VirtualBox was the most popular virtualization software application. Supported operating systems include Windows XP, Windows Vista, Windows 7, macOS X, Linux, Solaris, and OpenSolaris.

VirtualBox was originally developed by Innotek GmbH and released in 2007 as an open-source software package. The company was later purchased by Sun Microsystems. Oracle Corporation now develops the software package and titles it Oracle VM VirtualBox.
""")
gparted = _("""GParted

The ultimate partition manager for Linux

The gparted application is the GNOME partition editor for creating, reorganizing, and deleting disk partitions.
A disk device can be subdivided into one or more partitions. The gparted application enables you to change the partition organization on a disk device while preserving the contents of the partition.

With gparted you can accomplish the following tasks:
- Create a partition table on a disk device.
- Enable and disable partition flags such as boot and hidden.
- Perform actions with partitions such as create, delete, resize, move, check, label, copy, and paste.
""")
gestures = _("""Touchpad Gestures (with fusuma)

Fusuma is a command line tool that allows you to configure the trackpad, and even includes multi-touch gestures. It's not perfect (nor does it remotely emulate the smoothness of the trackpad experience on either macOS or Chrome OS), but Fusuma does make using a trackpad on Linux exponentially better.
""")
audacity = _("""Audacity

The free and open-source audio tool

Audacity is the name of a popular open source multilingual audio editor and recorder software that is used to record and edit sounds. It is free and works on Windows, Mac OS X, GNU/Linux and other operating systems.

Audacity can be used to perform a number of audio editing and recording tasks such as making ringtones, mixing stero tracks, transferring tapes and records to computer or CD, splitting recordings into separate tracks and more. The Audacity Wiki provides indepth tutorials on how to do these types of tasks in Audacity. Vendors can also freely bundle Audacity with their products or sell or distribute copies of Audacity under the GNU General Public License (GPL).
""")
deja = _("""Déja-Dup

One of the most powerful backup solutions for Linux

Deja-dup: is a simple yet powerful backup tool included with Ubuntu. It offers the power of resync with incremental backups, encryption, scheduling, and support for remote services. With Deja-dup, you can quickly revert files to previous versions or restore missing files from a file manager window.

You can do full system backups, Home folder backup or even settings backup in Ubuntu. You can backup to your GDrive storage also.
""")
timeshift = _("""Timeshift

The best backup solution (in my opinion) for Linux

Timeshift for Linux is an application that provides functionality similar to the System Restore feature in Windows and the Time Machine tool in Mac OS. Timeshift protects your system by taking incremental snapshots of the file system at regular intervals. These snapshots can be restored at a later date to undo all changes to the system.

In RSYNC mode, snapshots are taken using rsync and hard-links. Common files are shared between snapshots which saves disk space. Each snapshot is a full system backup that can be browsed with a file manager.

In BTRFS mode, snapshots are taken using the in-built features of the BTRFS filesystem. BTRFS snapshots are supported only on BTRFS systems having an Ubuntu-type subvolume layout (with @ and @home subvolumes).

Timeshift is similar to applications like rsnapshot, BackInTime and TimeVault but with different goals. It is designed to protect only system files and settings. User files such as documents, pictures and music are excluded. This ensures that your files remains unchanged when you restore your system to an earlier date.
""")
teamv = _("""TeamViewer

TeamViewer (TeamViewer 6) is a popular piece of  software used for Internet-based remote access and support. TeamViewer software can connect to any PC or server, so you can remote control your partner's PC as if you were sitting right in front of it. For the remote session to work the partner has to start a small application, which does not require installation or administrative rights.

TeamViewer 6 is the latest version of the software and works with Windows, Mac, Linux operating systems and Mobile (Android, Apple iPad, Apple iPhone) devices. TeamViewer 6 is free for all non-commercial users.
""")
box = _("""Gnome Boxes

The simpliest way to run virtual machines as a normal, non-expert user.

GNOME Boxes is an application of the GNOME Desktop Environment, used to access remote or virtual systems. Boxes uses the QEMU, KVM, and libvirt virtualisation technologies.

GNOME Boxes requires the CPU to support some kind of Hardware-assisted virtualization (Intel VT-x, for example).
""")
barrier = _("""Barrier by debauchee

Barrier is KVM software forked from Symless's synergy 1.9 codebase. Synergy was a commercialized reimplementation of the original CosmoSynergy written by Chris Schoeneman.

Whereas synergy has moved beyond its goals from the 1.x era, Barrier aims to maintain that simplicity. Barrier will let you use your keyboard and mouse from machine A to control machine B (or more). It's that simple.
""")
mint = _("""Linux Mint

Linux Mint was my first distro, and now I am a hardcore Linux user, so it was really beginner friendly :)
First of all, the DE (Cinnamon) looks nearly exactly like Windows, so it is easy to get used to it. It is also pretty lightweight and stable for the everydays. It also supports deskletts and plugins. It has all the codecs and drivers that you will need out of the box, and it has a driver manager also. Regarding the OS itself, it is based on Ubuntu LTS version so it is compatible with everything and it is also reliable. The community is excellent! If you have some questions or problems, just ask, and probably within a few days you will get a solution. I recommend it to every beginner.
""")
ubuntu = _("""Ubuntu

Ubuntu is one of the oldest and most popular consumer Linux distos. Because of this, the support is outstandin It has a lots of flavours (Kubuntu with KDE, Xubuntu with XFCE, Lubuntu with LXQT and so on...), the main version uses GNOME as its DE with some tweaks. It is stable and up to date enough for daily usage, and it has lots of programs in its repos. If you still can not find something there are lots of PPAs out there. It runs on nearly everything without problems, and the installation process is extremely easy and straightforward.
""")
solus = _("""Solus Linux

Solus is a pretty fresh Linux distro built from scratch by a small (but growing) group of talented developers and users. The story behind the project is also very special. The community is rather small, but very helpful. The OS is extremely stable and well optimized, and its own DE, Budgie is also very modern and usable. The only drawback is that because of it is based on nothing, not every package is avilable. However, probablyy you will find everything right in the official repos without the need of any 3rd party repo. If not, then you can request new packages on the official site. I recommend it for those who are not afraid of a littlebit of learning to make everything work.
""")
deepin = _("""Deepin Linux

Deepin is the beautiful, minimalist, well supported, regularly updated and perfectly optimized distro from China with lots of great features and an interesting name. It is based on Debian (Unstable), it has a rolling release update method and a lots of own programs (DDE, DWM, Deepin Boot maker, Deepin Installer/Music/Movie/Backup/Clone/Recovery/Print/Connect and so on...). If you would like to use something that works out of the box (in nearly every case), and you do not want to learn anything about computers and Linux, then this is the perfect choice for you.
""")
elementary = _("""Elementary OS

Elementary is the macOS of the Linux world. Not because it is expensive or closed source, but because of its simplicity and user friendliness. If you are a beginner, then maybe this is the perfect distro for you. It is nothing special, no bloatware, based on Ubuntu, simple interface, stability and performance. What else do you need? Regarding its pretty old-school look, trust me, you will get used to it after around a week, and after that you will just love it.
""")
steamos = _("""Steam OS

SteamOS is the primary operating system for the Steam Machine gaming platform by Valve Corporation. It is based on Debian Linux. It was released alongside the start of end-user beta testing of Steam Machines in December 2013.
""")
debian = _("""Debian

Debian GNU/Linux, is a Linux distribution composed of free and open-source software, developed by the community-supported Debian Project, which was established by Ian Murdock on August 16, 1993. The first version, Debian 0.01, was released on September 15, 1993, and the first stable version, 1.1, was released on June 17, 1996. The Debian Stable branch is the most popular edition for personal computers and servers, and is the basis for many other distributions.
""")
fedora = _("""Fedora

Fedora Linux is a Linux distribution developed by the independent community-supported Fedora Project, sponsored primarily by Red Hat with substantial support by other companies. Fedora contains software distributed under various free and open-source licenses and aims to be on the leading edge of such technologies. Fedora is the upstream source of the commercial Red Hat Enterprise Linux distribution.
""")
opensuse = _("""openSUSE

openSUSE, formerly SUSE Linux and SuSE Linux Professional, is a Linux distribution sponsored by SUSE Linux GmbH and other companies. It is widely used throughout the world. The focus of its development is creating usable open-source tools for software developers and system administrators, while providing a user-friendly desktop and feature-rich server environment.
""")
arch = _("""Arch Linux

Arch Linux is a Linux distribution for computers based on x86-64 architectures. The Arch Linux repositories contain both libre, and nonfree software, and the default Arch Linux kernel contains nonfree proprietary blobs, hence the distribution is not endorsed by the GNU project.

The design approach of the development team follows the KISS principle ("keep it simple, stupid") as the general guideline. It focuses on elegance, code correctness, minimalism, simplicity, and expects the user to be willing to make some effort to understand the system's operation. A package manager written specifically for Arch Linux, pacman, is used to install, remove and update software packages.
""")
gentoo = _("""Gentoo

Gentoo Linux is a Linux distribution built using the Portage package management system. Unlike a binary software distribution, the source code is compiled locally according to the user's preferences and is often optimized for the specific type of computer. Precompiled binaries are available for some larger packages or those with no available source code.
""")
lfs = _("""LFS

Linux From Scratch (LFS) is a project that provides you with step-by-step instructions for building your own custom Linux system, entirely from source code.
""")

drauger = _("""Drauger OS

Drauger OS is a Linux desktop gaming operating system. It aims to provide a platform for gamers to use where they can get great performance without sacrificing their security. Furthermore, it aims to make it easy for anyone to game, whether they use a keyboard and mouse, or some sort of controller.

Based off Ubuntu LTS releases, Drauger OS is stable, secure, and gets updates thanks to the Ubuntu repositories for 5 years (even if a given Drauger OS release is not supported for the full 5 years by Drauger OS Development itself.)
""")

slax = _("""Slax

Slax is a really portable lightweight Linux distro based on Debian which you can use it on a USB drive without installing it.
The ISO file size is just under 300 MB – which makes it a great option for older computers. The user interface is simple and usable with essential pre-built packages for an average user. You can even try to customize the OS and make permanent changes on the fly if you require it.

Give it a try!

Minimum system requirements for Slax:
RAM: 128 MB (offline usage) / 512 MB (for web browser usage)
CPU: i686 or newer
""")

pepper = _("""Peppermint OS

Peppermint is a cloud-focused Linux distribution that doesn’t need high-end hardware. It is based on Ubuntu and uses LXDE desktop environment to give you a smoother experience.
Originally created with the web-centric approach of netbooks in mind, Peppermint includes the ICE application for integrating any website or web app as a standalone desktop app.

You’ll find the documentation helpful as well. A dedicated forum also exists to help troubleshooting issues and answering your questions.

Minimum system requirements for Peppermint OS:
RAM: 1 GB of RAM (recommended 2 GB)
CPU: Processor based on Intel x86 architecture
Disk space: At least 4 GB of available disk space
""")

bodhi = _("""Bodhi Linux

Yet another light Linux distribution – Bodhi Linux, that gives life to older PCs & Laptops. Bodhi Linux is quite known for its minimal approach and the support for low-end hardware.

It doesn’t feature a lot of things pre-installed – hence, you will notice that the ISO file size will be less than 1 GB.
The presence of Moksh Desktop makes Bodhi Linux is a decent choice for older hardware configurations while providing a good user experience.

Minimum hardware requirements for Bodhi Linux:
RAM: 256 MB of RAM
CPU: 1.0 GHz
Disk space: 5 GB of drive space
""")

sparky = _("""SparkyLinux

SparkyLinux is another lightweight distro but at the same time, it also targets modern computers.

Depending on what you need – you will find two variants of SparkyLinux. One based on Debian’s stable release and the other based on Debian’s testing branch. So, you can opt for anyone you see fit.
In addition to the variants, you will also find different editions of ISO to download. For instance, an LXQT desktop-based edition, a GameOver edition with pre-installed stuff, and so on.
You can head down to their download page and click on “Stable” or “(Semi-)Rolling” releases to find all the editions listed.

Minimum hardware requirements for SparkyLinux:
RAM: 512 MB
CPU: Pentium 4, or AMD Athlon
Disk space: 2 GB (CLI Edition), 10 GB (Home Edition), 20 GB (GameOver Edition)
""")

puppy = _("""Puppy Linux

Puppy Linux uses JWM and Openbox window managers by default which makes it very easy on system resources.
Because Puppy Linux is built to be fast, it does not come along with bundles of applications. It does have some basic apps, though. In other words, it can get your work done if you want to utilize a really old computer.

Minimum hardware requirements for Puppy Linux:
RAM:  256 MB
CPU: 600 Hz Processor
""")

tiny = _("""Tiny Core

Probably, technically, the most lightweight distro there is. However, it isn’t a complete Linux distribution for an average desktop user.
Tiny Core simply incorporates the fundamental core of an OS which includes the kernel and the root filesystem. In other words, it features the foundation of a desktop OS.

If you simply want a system to boot up coupled with a wired Internet connection, you can get started using it. But, you should not expect proper hardware support out of the box.
So, if you’re someone who knows how to set up or compile tools necessary with Tiny Core Linux to make it a complete desktop experience, you can give it a try.

Minimum hardware requirements for Tiny Core Linux:
RAM:  64 MB (128 MB recommended)
CPU: i486DX
""")

hsuite = _("""HSuite

Actually, I could copy-paste it from the About section, but I do not see the point of it. So why is this here at all? Because HSuite is kind of a platform, where I can also host my own work (including HSuite itself). So it is basically for simpler navigation and easier reach of source code.
""")

henv = _("""HEnv

HEnv is a small tool that helps me in development. The name itself stands for H-Environment. Currently it does automatic debian packaging only, more functions are going to be added later.
""")


descDict = {opera : _('App Spotlight'), chrome : _('App Spotlight'), web : _('App Spotlight'), firefox : _('App Spotlight'), vivaldi : _('App Spotlight'), edge : _('App Spotlight'), wps : _('App Spotlight'), libreoffice : _('App Spotlight'), freeoffice : _('App Spotlight'), onlyoffice : _('App Spotlight'), gedit : _('App Spotlight'), emacs : _('App Spotlight'), code : _('App Spotlight'), atom : _('App Spotlight'), stext : _('App Spotlight'), geany : _('App Spotlight'), skype : _('App Spotlight'), discord : _('App Spotlight'), telegram : _('App Spotlight'), signal : _('App Spotlight'), hexchat : _('App Spotlight'), franz : _('App Spotlight'), ad : _('App Spotlight'), tux : _('App Spotlight'), lutris : _('App Spotlight'), pol : _('App Spotlight'), steam : _('App Spotlight'), minecraft : _('App Spotlight'), tuxkart : _('App Spotlight'), popsicle : _('App Spotlight'), woeusb : _('App Spotlight'), wine : _('App Spotlight'), vbox : _('App Spotlight'), gparted : _('App Spotlight'), gestures : _('App Spotlight'), audacity : _('App Spotlight'), officeonline : _('App Spotlight'), gsuite : _('App Spotlight'), deja : _('App Spotlight'), timeshift : _('App Spotlight'), teamv : _('App Spotlight'), box : _('App Spotlight'), barrier : _('App Spotlight'), mint : _('Distro Boutique'), ubuntu : _('Distro Boutique'), solus : _('Distro Boutique'), deepin : _('Distro Boutique'), elementary : _('Distro Boutique'), steamos : _('Distro Boutique'), debian : _('Distro Boutique'),fedora : _('Distro Boutique'), opensuse : _('Distro Boutique'), arch : _('Distro Boutique'), gentoo : _('Distro Boutique'), lfs : _('Distro Boutique'), drauger : _('Distro Boutique'), slax : _('Distro Boutique'), pepper : _('Distro Boutique'), bodhi : _('Distro Boutique'), sparky : _('Distro Boutique'), puppy : _('Distro Boutique'), tiny : _('Distro Boutique'), hsuite : _('App Spotlight'), henv : _('App Spotlight')}

descList = [opera, chrome, web, firefox, vivaldi, edge, wps, libreoffice, onlyoffice, officeonline, gsuite, freeoffice, gedit, emacs, code, atom, stext, geany, skype, discord, telegram, signal, hexchat, franz, ad, tux, lutris, pol, steam, minecraft, tuxkart, popsicle, woeusb, wine, vbox, gparted, gestures, audacity, deja, timeshift, teamv, box, barrier, mint, ubuntu, solus, deepin, elementary, steamos, debian, fedora, opensuse, arch, gentoo, lfs, drauger, slax, pepper, bodhi, sparky, puppy, tiny, hsuite, henv]

webDict = {mint : _('https://www.linuxmint.com'), ubuntu : _('https://ubuntu.com'), solus : _('https://getsol.us/home/'), deepin : _('https://www.deepin.org/en/'), elementary : _('https://elementary.io'), steamos : _('https://store.steampowered.com/steamos/'), debian : _('https://www.debian.org'), fedora : _('https://getfedora.org'), opensuse : _('https://www.opensuse.org'), arch : _('https://www.archlinux.org'), gentoo : _('https://www.gentoo.org'), lfs : _('http://www.linuxfromscratch.org'), drauger : _('https://draugeros.org/'), slax : _('https://www.slax.org'), pepper : _('https://peppermintos.com'), bodhi : _('https://www.bodhilinux.com'), sparky : _('https://sparkylinux.org'), puppy : _('http://puppylinux.com'), tiny : _('http://tinycorelinux.net')}

vidDict = {mint : 'https://distrotest.net/Linux%20Mint', ubuntu : 'https://distrotest.net/Ubuntu', solus : 'https://distrotest.net/Solus', deepin : 'https://distrotest.net/deepin', elementary : 'https://distrotest.net/elementaryOS', steamos : 'https://youtu.be/1saebgKGLuY', debian : 'https://distrotest.net/Debian', fedora : 'https://distrotest.net/Fedora%20Workstation', opensuse : 'https://distrotest.net/openSUSE', arch : 'https://distrotest.net/Archlinux', gentoo : 'https://distrotest.net/Gentoo/20160704', lfs : 'https://youtu.be/qZJzbI6ZJ34', drauger : 'https://youtu.be/BSUbP2pUovU', slax : 'https://distrotest.net/Slax', pepper : 'https://distrotest.net/PeppermintOS', bodhi : 'https://distrotest.net/Bodhi', sparky : 'https://distrotest.net/SparkyLinux', puppy : 'https://distrotest.net/Puppy%20Linux', tiny : 'https://distrotest.net/Tiny%20Core'}

descLen = len(descList)