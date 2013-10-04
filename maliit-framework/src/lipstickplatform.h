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

#ifndef MALIIT_LIPSTICK_PLATFORM_H
#define MALIIT_LIPSTICK_PLATFORM_H

#include "abstractplatform.h"

namespace Maliit
{

class LipstickPlatform : public AbstractPlatform
{
    virtual void setupInputPanel(QWindow* window, Maliit::Position position);
    virtual void setInputRegion(QWindow* window, const QRegion& region);
};

} // namespace Maliit

#endif // MALIIT_UNKNOWN_PLATFORM_H
