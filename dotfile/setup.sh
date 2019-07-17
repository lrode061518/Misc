#!/usr/bin/sh

SCRIPT_PATH=$(dirname $(readlink -f $0))
echo $SCRIPT_PATH


ln -s $SCRIPT_PATH/.tmux.conf ~/.tmux.conf
ln -s $SCRIPT_PATH/.vimrc ~/.vimrc
ln -s $SCRIPT_PATH/.bash_profile ~/.bash_profile
