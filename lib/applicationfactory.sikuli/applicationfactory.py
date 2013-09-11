import platform

class ApplicationFactory(object):

    def _osversion(self):
        """return sled11, opensuse123, ubuntu1210, etc."""
        pass

    def _desktop(self):
        """return gnome, gnomeshell, unity, kde3, kde4, etc."""
        pass

    @staticmethod
    def create(application, osversion=None, desktop=None):

        if osversion == None:
            osversion = self._osversion()
        if desktop == None:
            desktop = self._desktop()

        klass = None
        classname = application.capitalize()+osversion.capitalize()+desktop.capitalize()
        try:
            mod = __import__(application.lower())
            klass = getattr(mod, classname)
        except (ImportError, AttributeError):
            print "The class " + classname + " in " + application.lower() +" module has not been implemented yet."

        return klass()
