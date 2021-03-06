# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyMarkupsafe(PythonPackage):
    """MarkupSafe is a library for Python that implements a unicode
    string that is aware of HTML escaping rules and can be used to
    implement automatic string escaping. It is used by Jinja 2, the
    Mako templating engine, the Pylons web framework and many more."""

    homepage = "http://www.pocoo.org/projects/markupsafe/"
    url      = "https://pypi.io/packages/source/M/MarkupSafe/MarkupSafe-1.0.tar.gz"

    import_modules = ['markupsafe']

    version('1.0',  sha256='a6be69091dac236ea9c6bc7d012beab42010fa914c459791d627dad4910eb665')
    version('0.23', sha256='a4ec1aff59b95a14b45eb2e23761a0179e98319da5a7eb76b56ea8cdc7b871c3')
    version('0.22', sha256='7642852b6d1e55c9e12e00a552c0b8943880f2172e55141ccb41eb5f8675dfa5')
    version('0.21', sha256='c6465cd6ed2b96509ef0100e7fff8718ed52c2affab1860ed5a9b67f604dd59a')
    version('0.20', sha256='f6cf3bd233f9ea6147b21c7c02cac24e5363570ce4fd6be11dab9f499ed6a7d8')
    version('0.19', sha256='62fcc5d641df8b5ad271ebbd6b77a19cd92eceba1e1a990de4e96c867789f037')

    depends_on('py-setuptools', type='build')
