#!/usr/bin/python
#

import getopt, fnmatch, string, glob
import sys
import re
import os
import subprocess
import csv
import time
import shutil

#-------------------------------------------------------------------------------
def akaMain(argv):

    argc = len(argv)

    #i=1
    #CONF_DOXY4UG        =sys.argv[i]; i=i+1

    VIDEO_PROJECTS  ='c:\\Git\\video_projects\\'

    PATH_VIDEO_PROJECTS   =os.path.normpath(VIDEO_PROJECTS)

    print "PATH_VIDEO_PROJECTS = ",PATH_VIDEO_PROJECTS  



    #for root, dirs, files in os.walk(top, topdown=False):
    #    for name in files:
    #        os.remove(os.path.join(root, name))
    #    for name in dirs:
    #        os.rmdir(os.path.join(root, name))



    for root, dirs, files in os.walk(PATH_VIDEO_PROJECTS):
        #for pathname in files:
            #print "+++ pathname = ",pathname  
        for dirname in dirs:
             
            if     'Adobe Premiere Pro' in dirname  \
                or 'Adobe After Effects' in dirname \
                or 'Motion Graphics' in dirname:

                print "--- del dirname = ",os.path.join(root, dirname) 
                shutil.rmtree(os.path.join(root, dirname))
            #else:
            #    print "+++ dirname = ",dirname  



#-------------------------------------------------------------------------------
# main module stub to prevent auto execute
#

if __name__ == '__main__':
    akaMain(sys.argv)
    sys.exit(0)

