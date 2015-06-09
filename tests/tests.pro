include(../config.pri)

CONFIG += ordered

TEMPLATE = subdirs

SUBDIRS += \
          dummyimplugin \
          dummyimplugin2 \
          dummyimplugin3 \
          dummyplugin \
          sanitychecks \
          ut_mattributeextensionmanager \
          ut_mkeyoverride \
          ft_exampleplugin \
          ut_mimsettings \
          ut_mimonscreenplugins \
          ut_minputmethodquickplugin \
          ut_mimserveroptions \

SUBDIRS += \
          ut_mimpluginmanager \
          ut_mimpluginmanagerconfig \
          ft_mimpluginmanager \

QMAKE_EXTRA_TARGETS += check
check.target = check
check.CONFIG = recursive

unix{
    tests_xml.target = tests.xml
    tests_xml.files = tests.xml
    tests_xml.path = /opt/tests/maliit-framework/
    tests_xml.CONFIG = no_check_exist
    tests_xml.commands = sed \'s%@PATH@%$${MALIIT_TEST_LIBDIR}%g\' $$PWD/tests.xml.in > $$PWD/tests.xml

    QMAKE_DISTCLEAN += tests.xml

    INSTALLS += tests_xml
}


