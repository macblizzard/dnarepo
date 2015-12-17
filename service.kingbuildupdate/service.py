#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import xbmc, xbmcgui

def start_king_service():
    xbmc.executebuiltin("RunAddon(service.kingbuildupdate)")
def service():
    while (not xbmc.abortRequested):
        if not (xbmc.Player().isPlaying() or xbmc.getCondVisibility('Library.IsScanningVideo')):
            if common.download_allowed(a):
                if not common.blocked(a):
                    start_king_service()
        xbmc.sleep(1000)
	