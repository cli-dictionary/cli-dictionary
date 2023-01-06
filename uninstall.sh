#!/usr/bin/env bash

if [[ $EUID -ne 0 ]]; then
	echo "You need to run as root"
	exit 1
fi

rm /usr/bin/cli-dictionary

echo "cli-dictionary has been successfully uninstalled."
