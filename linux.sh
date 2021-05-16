#!/bin/bash

sudo mkdir /etc/smoke-installer/
cp -r etc/* /etc/smoke-installer/
cp -r linux_smoke-installer /bin/Smoke_Installer
echo "Run 'Smoke_Installer' to run Smoke Installer v0.1.0-beta"
