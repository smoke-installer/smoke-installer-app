#!/bin/python3

import os
import platform

def main():
	if platform.machine == 'x86_64':
		os.rename('x86_64-Smoke_Installer', '/bin/Smoke_Installer')
		# Before Smoke Installer was released it was called Ludum before it had a normal name
		# Forgot to change file paths in the source code so the etc directory will be ludum for now
		os.rename('etc/', '/etc/ludum/')
	else if patform.machine == 'aarch64':
		os.rename('aarch64-Smoke_Installer', '/bin/Smoke_Installer')
		os.rename('etc/', '/etc/ludum/')
	else:
		print("Sorry Smoke Installer doesn't support your architecture yet")

if __name__ == '__main__':
	main()

