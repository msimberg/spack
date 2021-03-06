# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyPyproj(PythonPackage):
    """Python interface to the PROJ.4 Library."""

    homepage = "https://github.com/pyproj4/pyproj"
    url      = "https://pypi.io/packages/source/p/pyproj/pyproj-2.2.0.tar.gz"
    git      = "https://github.com/pyproj4/pyproj.git"

    maintainers = ['citibeth', 'adamjstewart']
    import_modules = ['pyproj']

    version('2.2.0',   sha256='0a4f793cc93539c2292638c498e24422a2ec4b25cb47545addea07724b2a56e5')
    version('1.9.6',   sha256='e0c02b1554b20c710d16d673817b2a89ff94738b0b537aead8ecb2edc4c4487b')
    version('1.9.5.1', sha256='53fa54c8fa8a1dfcd6af4bf09ce1aae5d4d949da63b90570ac5ec849efaf3ea8')

    depends_on('python@:2', when='@:1.9.5.1')
    depends_on('python@3:', when='@2.3:')
    depends_on('py-setuptools', type='build')
    depends_on('py-cython', type='build')
    depends_on('py-aenum', type=('build', 'run'), when='@2.2:^python@:3.5')
    depends_on('proj')
    depends_on('proj@:5',   when='@:1')
    depends_on('proj@6.1:', when='@2.2:')
    depends_on('proj@6.0:', when='@2.0:')

    def setup_environment(self, spack_env, run_env):
        spack_env.set('PROJ_DIR', self.spec['proj'].prefix)
