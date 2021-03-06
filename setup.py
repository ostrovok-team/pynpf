import glob
import os
import shutil
from setuptools import setup
from setuptools.command.develop import develop
from subprocess import check_call

DESCRIPTION = 'Python wrapper for npf (http://github.com/4u/npf'

def install_deps():
    print "Installing dependencies"
    cdir = os.path.abspath(os.path.dirname(__file__))
    os.chdir(cdir)
    shutil.rmtree('pynpf/npf', ignore_errors=True)
    check_call(['git', 'submodule', 'update', '--init', '--recursive', '--force'])
    os.chdir(os.path.join(cdir, 'pynpf/npf'))
    for filename in glob.glob('.git*'):
        if os.path.isfile(filename):
            os.remove(filename)
        else:
            shutil.rmtree(filename)
    os.chdir(cdir)

class do_develop(develop):
    def run(self):
        install_deps()
        develop.run(self)


setup(
    cmdclass={'develop': do_develop,},
    name='pynpf',
    version='0.1.5',
    packages=['pynpf'],
    package_dir={'pynpf': '.'},
    package_data={'pynpf': ['pynpf/*']},
    author='Yasha Borevich',
    author_email='j.borevich@gmail.com',
    url='http://github.com/ostrovok-team/pynpf',
    description=DESCRIPTION,
    long_description=DESCRIPTION,
    platforms='any',
    classifiers = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ],
)
