from iocbuilder import Substitution, AutoSubstitution, SetSimulation, Device, records, Architecture, IocDataStream
from iocbuilder.arginfo import *
from iocbuilder.modules.asyn import Asyn, AsynPort, AsynIP
from iocbuilder.modules.ADCore import ADCore, ADBaseTemplate, makeTemplateInstance, includesTemplates, NDDataTypes

__all__ = ['PVCam']


@includesTemplates(ADBaseTemplate)
class PVCamTemplate(AutoSubstitution):
    TemplateFile = "pvCam.template"


class PVCam(AsynPort):

    """Creates a pvCam driver."""

    Dependencies = (ADCore,)
    _SpecificTemplate = PVCamTemplate

    def __init__(self, PORT, MAXSIZEX=2048, MAXSIZEY=2048, DATATYPE=3, BUFFERS=0, MEMORY=0, **args):
        # Init the superclass
        self.__super.__init__(PORT)
        # Store the args
        self.__dict__.update(locals())
        # Make an instance of our template
        makeTemplateInstance(self._SpecificTemplate, locals(), args)

    # __init__ arguments
    ArgInfo = ADBaseTemplate.ArgInfo + _SpecificTemplate.ArgInfo + makeArgInfo(__init__,
        PORT=Simple("Port name for the detector", str),
        MAXSIZEX=Simple("Maximum image size in X", int),
        MAXSIZEY=Simple("Maximum image size in Y", int),
        DATATYPE=Enum('Datatype', NDDataTypes),
        BUFFERS=Simple("Maximum number of NDArray buffers to be created for plugin callbacks", int),
        MEMORY=Simple("Max memory to allocate, should be maxw*maxh*nbuffer for driver and all attached plugins", int))

    # Device attributes
    LibFileList = ['pvCam', 'pvcam32', 'pv_icl32']
    DbdFileList = ['pvCamSupport']

    # Copy the libraries
    MakefileStringList = ["USR_CFLAGS += -DWIN32", "USR_CXXFLAGS += -DWIN32"]

    def Initialise(self):
        print "# pvCamConfig(const char *portName, int maxSizeX, int maxSizeY, int dataType, int maxBuffers, size_t maxMemory)"
        print 'pvCamConfig("%(PORT)s", %(MAXSIZEX)d, %(MAXSIZEY)d, %(DATATYPE)d, %(BUFFERS)d, %(MEMORY)d)' % self.__dict__
