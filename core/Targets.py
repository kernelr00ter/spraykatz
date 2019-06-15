# coding: utf-8

# Author:	Lyderic LEFEBVRE
# Twitter:	@lydericlefebvre
# Mail:		lylefebvre.infosec@gmail.com
# LinkedIn:	https://www.linkedin.com/in/lydericlefebvre


# Imports
import logging, nmap
from core.Colors import *
from subprocess import Popen, PIPE
from helpers import invoke_checklocaladminaccess


def listSmbTargets(args_targets):
	strTargets = ' '.join(args_targets)
	nm = nmap.nmap.PortScanner()
	nm.scan(strTargets, arguments='-T4 -sS -Pn --open -p 135')

	if nm.all_hosts():
		return nm.all_hosts()
	else:
		logging.warning("%sNo targets with open port 135 available. Quitting." % (warningRed))
		exit(2)

def listPwnableTargets(args_targets, user):
	logging.warning("%sListing targetable machines into networks provided. Can take a while..." % (warningGre))
	pwnableTargets = []
	targets = []

	for smbTarget in listSmbTargets(args_targets):
		try:
			if invoke_checklocaladminaccess(smbTarget, user.domain, user.username, user.password, user.lmhash, user.nthash):
				logging.info("%s   %s is %spwnable%s!" % (infoYellow, smbTarget, green, white))
				pwnableTargets.append(smbTarget)
		except Exception as e:
			logging.warning("%sUnexpected Error: %s" % (warningRed, e))

	if not pwnableTargets:
		logging.warning("%sNo pwnable targets. Quitting." % (warningRed))
		exit(2)
	return pwnableTargets