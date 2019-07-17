#!/usr/bin/env sh
git config --global alias.lg "log --color --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset%n  %s %Cgreen(%cr) %C(bold blue)<%an>%Creset%n'"

uname="$(uname -s)"
case "${uname}" in
    Linux* | Darwin* )
        echo 'it config --global credential.helper "cache --timeout=28800"'
        git config --global credential.helper "cache --timeout=28800"
        ;;
    CYGWIN* | MINGW* )
        echo git config --global credential.helper wincred
        git config --global credential.helper wincred
        ;;
    *) echo "Cannot detect OS... git credential setup ignored.";;
esac
