import os
import sys
from setuptools import setup, find_packages


# References
#   numpy's setup.py
#   https://github.com/numpy/numpy/blob/943695bddd1ca72f3047821309165d26224a3d12/setup.py

def setup_package():
    src_path = os.path.dirname(os.path.abspath(sys.argv[0]))
    old_path = os.getcwd()
    os.chdir(src_path)
    sys.path.insert(0, src_path)

    with open('README.md') as f:
        readme = f.read()

    metadata = dict(
        name='brainbite',
        version='0.1.0',
        description='A python bit my brain.',
        long_description=readme,
        author='LouiSakaki',
        author_email='e1352207@outlook.jp',
        url='https://github.com/LouiS0616/brainbite',
        license=license,
        packages=find_packages(),

        package_data={
            'brainbite': ['sample/*.py']
        }
    )

    try:
        setup(**metadata)
    finally:
        del sys.path[0]
        os.chdir(old_path)
    return


if __name__ == '__main__':
    setup_package()
