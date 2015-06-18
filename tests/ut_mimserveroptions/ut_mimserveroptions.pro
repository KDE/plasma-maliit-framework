include(../common_top.pri)

include(../../src/libmaliit-plugins.pri)

# Input
HEADERS += \
    ut_mimserveroptions.h \

SOURCES += \
    ut_mimserveroptions.cpp \

QT += dbus KWaylandClient

include(../common_check.pri)
