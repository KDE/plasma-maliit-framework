/* * This file is part of Maliit framework *
 *
 * Copyright (C) 2013 Jolla Ltd.
 *
 * Contact: maliit-discuss@lists.maliit.org
 *
 * This library is free software; you can redistribute it and/or
 * modify it under the terms of the GNU Lesser General Public
 * License version 2.1 as published by the Free Software Foundation
 * and appearing in the file LICENSE.LGPL included in the packaging
 * of this file.
 */

#include "lipstickplatform.h"

#include <QGuiApplication>
#include <qpa/qplatformnativeinterface.h>

namespace Maliit
{

void LipstickPlatform::setupInputPanel(QWindow* window, Maliit::Position)
{
    QPlatformNativeInterface *native = QGuiApplication::platformNativeInterface();
    window->create();
    native->setWindowProperty(window->handle(), QLatin1String("CATEGORY"), QString("overlay"));
}

void LipstickPlatform::setInputRegion(QWindow* window, const QRegion& region)
{
    QPlatformNativeInterface *native = QGuiApplication::platformNativeInterface();
    window->create();
    native->setWindowProperty(window->handle(), QLatin1String("MOUSE_REGION"), QVariant(region));
}

} // namespace Maliit
