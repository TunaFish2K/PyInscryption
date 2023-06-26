from setuptools import setup, find_packages

setup(
    name="py-inscryption",
    version="0.0.1",
    author="TunaFish2K",
    author_email="tunafish2k@163.com",
    description="The module to automatically generate Inscryption card with code.",
    url="https://github.com/TunaFish2K/PyInscryption", 
    packages=["py_inscryption"],
    install_requires=['Pillow>=9.5.0'],
    python_requires='>=3.6',
    include_package_data=True,
    classifiers= [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
    ]
)