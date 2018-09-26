git config --global alias.lg "log --color --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset%n  %s %Cgreen(%cr) %C(bold blue)<%an>%Creset%n'"

uname="$(uname -s)"
case "${uname}" in
    Linux* | Darwin* ) echo git config --global credential.helper cache;;
    CYGWIN* | MINGW* ) echo git config --global credential.helper wincred;;
    *) echo "Cannot detect OS... git credential setup ignored.";;
esac
