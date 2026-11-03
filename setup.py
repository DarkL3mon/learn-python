from Cython.Build import cythonize
from setuptools import Extension, setup
from setuptools.command.build_py import build_py


class BuildPyWithoutCompiledSource(build_py):
    def find_package_modules(self, package, package_dir):
        modules = super().find_package_modules(package, package_dir)
        return [
            module for module in modules
            if (module[0]) != ("main")
            if (module[0], module[1]) != ("algorithms", "basicMath")
        ]


setup(
    ext_modules=cythonize(
        [
            Extension("main", ["src/main.py"]),
            Extension("algorithms.basicMath", ["src/algorithms/basicMath.py"])
        ],
        build_dir="build/cython",
        compiler_directives={"language_level": "3"},
    ),
    cmdclass={"build_py": BuildPyWithoutCompiledSource},
)
