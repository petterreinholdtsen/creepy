from distutils.core import setup
import py2exe, sys, os

sys.argv.append('py2exe')

DATA = [('imageformats', ['C:\\Python27/Lib/site-packages/PyQt4/plugins/imageformats/qjpeg4.dll',
                          'C:\\Python27/Lib/site-packages/PyQt4/plugins/imageformats/qgif4.dll',
                          'C:\\Python27/Lib/site-packages/PyQt4/plugins/imageformats/qico4.dll',
                          'C:\\Python27/Lib/site-packages/PyQt4/plugins/imageformats/qmng4.dll',
                          'C:\\Python27/Lib/site-packages/PyQt4/plugins/imageformats/qsvg4.dll',
                          'C:\\Python27/Lib/site-packages/PyQt4/plugins/imageformats/qtiff4.dll'
])]

setup(
    name='creepy',
    version='0.1.92',
    author='Yiannis Kakavas',
    author_email='jkakavas@gmail.com',
    options={'py2exe': {'bundle_files': 1, 'compressed': True, "includes": ["sip"]}},
    windows=[{'script': "CreepyMain.py"}],
    zipfile=None,
    data_files=DATA,
)