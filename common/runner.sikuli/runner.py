# Usage:
#        $ runIDE -r runner --args $testcase_directory_path
# Example:
#        1. run 1 case
#        $ runIDE -r common/runner --args sled11sp3/libreoffice/libreoffice_hyphenation.sikuli
#        
#        2. run more cases sequentially
#        $ runIDE -r common/runner --args sled11sp3/libreoffice/libreoffice_hyphenation.sikuli sled11sp3/libreoffice/libreoffice_pyuno_bridge.sikuli sled11sp3/libreoffice/libreoffic
# e_thesaurus.sikuli

import os, sys

# every test case is to import the general settings module
import settings
reload(settings)

for tc in sys.argv[1:]:
    if not os.path.realpath(os.path.abspath(tc)) in sys.path:
        sys.path.append(os.path.realpath(os.path.abspath(tc)) + os.sep + "..")
    tcname = os.path.basename(tc).replace(".sikuli", "")
    tcmodule = __import__(tcname)

    print 
    print "Running: " + tcname
    try:    
        print "Result: " + "Pass" if tcmodule.run() else "Fail"
    except Exception, e:
        print Exception, e       
        print "Result: Fail"
        print
    print
