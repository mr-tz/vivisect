from setuptools import setup, find_packages


setup(
    name='vivisect',
    author='',
    author_email='',
    version='',
    url='https://github.com/vivisect/vivisect',
    py_modules=[''],
    packages=find_packages(),
    package_data={
        '': ['*.dll', '*.dylib', '*.yes', '*.cfg', '*.lyt',
             '*.c', '*.h', 'Makefile',],
        },
    entry_points={
        "console_scripts": [
            "vivbin=vivisect.vivbin:main",
            "vdbbin=vdb.vdbbin:main",
        ]
    },
    description='',
    zip_safe=False,
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python'
        'Topic :: Security',
        'Topic :: Software Development :: Debuggers',
        'Topic :: Software Development :: Disassemblers',
    ]
)
