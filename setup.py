from distutils.core import setup
import py2exe

setup(
    name = "numerical_methods",
    version= "1.0",
    description="Numerical Methods",
    author="Juan Carlos Monreal Romero & Jordy Lagunas Higuera",
    author_email="jcmonrealr@gmail.com",
    url="https://github.com/Crxwler/Numerical-Methods",
    license="GNU General Public License v2.0",
    scripts=["Newton.py"],
    console=["Newton.py"],
    options={"py2exe": {"bundle_files": 1}},
    zipfile=None,
)