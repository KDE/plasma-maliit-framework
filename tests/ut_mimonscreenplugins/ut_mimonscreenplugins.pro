include(../common_top.pri)

# Input
HEADERS += \
    ut_mimonscreenplugins.h \

SOURCES += \
    ut_mimonscreenplugins.cpp \

QT += dbus KWaylandClient

include($$TOP_DIR/src/libmaliit-plugins.pri)
include(../common_check.pri)
