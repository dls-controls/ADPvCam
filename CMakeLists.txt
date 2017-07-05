cmake_minimum_required(VERSION 3.5)
project(ADPvCam)


include_directories(
    ${EPICS_BASE}/include/os/Linux)

set(ADPVCAM_SOURCE_FILES
    pvcamApp/src/pvCamAppMain.c
    pvcamApp/src/drvPVCamEpics.c
    pvcamApp/src/pvCam.cpp
    pvcamApp/src/pvCamSrc.h
    pvcamApp/src/drvPVCam.h
    pvcamSupport/pvcam.h
    pvcamSupport/pv_icl.h
    pvcamSupport/os/Linux/master.h
    pvcamSupport/os/WIN32/master.h
    pvcamSupport/os/cygwin32/master.h
    iocs/pvcamIOC/pvcamApp/src/pvCamAppMain.cpp
)

add_library(ADPvCam_source ${ADPVCAM_SOURCE_FILES})
add_custom_target(ADPvCam_build
    COMMAND $(MAKE) -C /scratch/home/AreaDetector/ADPvCam
    SOURCES ${ADPVCAM_SOURCE_FILES})
