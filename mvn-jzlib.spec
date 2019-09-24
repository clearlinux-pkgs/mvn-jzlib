#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-jzlib
Version  : 1.1.1
Release  : 3
URL      : https://github.com/ymnk/jzlib/archive/1.1.1.tar.gz
Source0  : https://github.com/ymnk/jzlib/archive/1.1.1.tar.gz
Source1  : https://repo.gradle.org/gradle/libs-releases/com/jcraft/jzlib/1.1.3/jzlib-1.1.3.jar
Source2  : https://repo.gradle.org/gradle/libs-releases/com/jcraft/jzlib/1.1.3/jzlib-1.1.3.pom
Source3  : https://repo1.maven.org/maven2/com/jcraft/jzlib/1.1.1/jzlib-1.1.1.jar
Source4  : https://repo1.maven.org/maven2/com/jcraft/jzlib/1.1.1/jzlib-1.1.1.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause
Requires: mvn-jzlib-data = %{version}-%{release}
Requires: mvn-jzlib-license = %{version}-%{release}
BuildRequires : apache-maven
BuildRequires : buildreq-mvn

%description
JZlib
zlib in pure Java(TM)
by ymnk@jcraft.com, JCraft,Inc.
http://www.jcraft.com/jzlib/

%package data
Summary: data components for the mvn-jzlib package.
Group: Data

%description data
data components for the mvn-jzlib package.


%package license
Summary: license components for the mvn-jzlib package.
Group: Default

%description license
license components for the mvn-jzlib package.


%prep
%setup -q -n jzlib-1.1.1

%build

%install
mkdir -p %{buildroot}/usr/share/package-licenses/mvn-jzlib
cp LICENSE.txt %{buildroot}/usr/share/package-licenses/mvn-jzlib/LICENSE.txt
mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/jcraft/jzlib/1.1.3
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/com/jcraft/jzlib/1.1.3/jzlib-1.1.3.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/jcraft/jzlib/1.1.3
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/com/jcraft/jzlib/1.1.3/jzlib-1.1.3.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/jcraft/jzlib/1.1.1
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/com/jcraft/jzlib/1.1.1/jzlib-1.1.1.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/jcraft/jzlib/1.1.1
cp %{SOURCE4} %{buildroot}/usr/share/java/.m2/repository/com/jcraft/jzlib/1.1.1/jzlib-1.1.1.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/com/jcraft/jzlib/1.1.1/jzlib-1.1.1.jar
/usr/share/java/.m2/repository/com/jcraft/jzlib/1.1.1/jzlib-1.1.1.pom
/usr/share/java/.m2/repository/com/jcraft/jzlib/1.1.3/jzlib-1.1.3.jar
/usr/share/java/.m2/repository/com/jcraft/jzlib/1.1.3/jzlib-1.1.3.pom

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mvn-jzlib/LICENSE.txt
