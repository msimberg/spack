# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Argobots(AutotoolsPackage):
    """Argobots, which was developed as a part of the Argo project, is
    a lightweight runtime system that supports integrated computation
    and data movement with massive concurrency. It will directly
    leverage the lowest-level constructs in the hardware and OS:
    lightweight notification mechanisms, data movement engines, memory
    mapping, and data placement strategies. It consists of an
    execution model and a memory model."""

    homepage = "http://www.argobots.org/"
    url      = "https://github.com/pmodels/argobots/releases/download/v1.0b1/argobots-1.0b1.tar.gz"
    git      = "https://github.com/pmodels/argobots.git"

    version("develop", branch="master")
    version("1.0rc1", sha256="2dc4487556dce602655a6535f501136f0edc3575708029c80b1af6dccd069ce7")
    version("1.0b1", sha256="480b85b0e8db288400088a57c2dc5639f556843b06b0492841920c38348a2a3e")
    version("1.0a1", sha256="bef93e06026ddeba8809474923176803e64d08e1425672cd7c5b424c797d5d9d")

    variant("valgrind", default=False, description="Enable Valgrind")

    depends_on("m4", type=("build"), when="@develop")
    depends_on("autoconf", type=("build"), when="@develop")
    depends_on("automake", type=("build"), when="@develop")
    depends_on("libtool", type=("build"), when="@develop")
    depends_on("valgrind", when="+valgrind")

    def configure_args(self):
        args = ["--enable-perf-opt"]
        if '+valgrind' in self.spec:
            args.append('--enable-valgrind')
        else:
            args.append('--disable-valgrind')

        return args
