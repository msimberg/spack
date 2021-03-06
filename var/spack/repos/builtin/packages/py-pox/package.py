# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyPox(PythonPackage):
    """Utilities for filesystem exploration and automated builds."""

    homepage = "https://github.com/uqfoundation/pox"
    url      = "https://pypi.io/packages/source/p/pox/pox-0.2.3.zip"

    version('0.2.3', sha256='d3e8167a1ebe08ae56262a0b9359118d90bc4648cd284b5d10ae240343100a75')
    version('0.2.2', sha256='c0b88e59ef0e4f2fa4839e11bf90d2c32d6ceb5abaf01f0c8138f7558e6f87c1')
    version('0.2.1', sha256='580bf731fee233c58eac0974011b5bf0698efb7337b0a1696d289043b4fcd7f4')

    depends_on('python@2.5:2.8,3.1:')

    depends_on('py-setuptools@0.6:', type='build')
