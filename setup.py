from distutils.core import setup
import py2exe

setup(
    name="numerical_methods",
    version="1.0",
    description="Numerical Methods",
    author="Juan Carlos Monreal Romero & Jordy Lagunas Higuera",
    author_email="jcmonrealr@gmail.com",
    url="https://github.com/Crxwler/Numerical-Methods",
    license="GNU General Public License v2.0",
    scripts=["Menu.py", "Interpolation.py", "Newton.py"],
    console=["Menu.py", "Interpolation.py", "Newton.py"],
    options={"py2exe": {"includes": ["decimal", "Tkinter", "numpy", "Matplotlib", "pandas", "scipy", "sympy"], "bundle_files": 1}},
    zipfile=None,
)
