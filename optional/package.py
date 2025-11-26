# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install spack-exercise
#
# You can edit this file again by typing:
#
#     spack edit spack-exercise
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class SpackExercise(CMakePackage):
    """SSE WS 2025/26 spack exercise by FelixKimmerle"""

    homepage = "https://simulation-software-engineering.github.io/homepage/"
    url = "https://github.com/FelixKimmerle/spack-exercise/archive/refs/tags/v0.3.1.tar.gz"
    git = "https://github.com/FelixKimmerle/spack-exercise.git"

    maintainers("FelixKimmerle")

    license("MIT", checked_by="FelixKimmerle")

    version("0.3.2", sha256="00d30369539a123eac09350b55f8f1283ae0379a25105646df86ec3fc54f3a5b")

    depends_on("cxx", type="build")
    depends_on("c", type="build")
    variant("boost", default=True, description="Enable support for boost")
    depends_on("boost@1.65.1:", when="+boost @0.2.0:")
    variant("yamlcpp", default=True, description="Enable support for yaml-cpp")
    depends_on("yaml-cpp@0.7.0:", when="+yamlcpp @0.3.0:")

    def cmake_args(self):
        #args = []
        #args.append(self.define("WITH_BOOST", "boost" in self.spec))
        #args.append(self.define("WITH_YAML", "yamlcpp" in self.spec))
        args = [
            self.define_from_variant("WITH_BOOST", "boost"),
            self.define_from_variant("WITH_YAML", "yamlcpp")
        ] 
        return args
