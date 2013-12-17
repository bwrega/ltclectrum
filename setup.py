#!/usr/bin/python

# python setup.py sdist --format=zip,gztar

from setuptools import setup
import os
import sys
import platform
import imp


version = imp.load_source('version', 'lib/version.py')
util = imp.load_source('version', 'lib/util.py')

if sys.version_info[:3] < (2, 6, 0):
    sys.exit("Error: LTCLectrum requires Python version >= 2.6.0...")

usr_share = '/usr/share'
if not os.access(usr_share, os.W_OK):
    usr_share = os.getenv("XDG_DATA_HOME", os.path.join(os.getenv("HOME"), ".local", "share"))

data_files = []
if (len(sys.argv) > 1 and (sys.argv[1] == "sdist")) or (platform.system() != 'Windows' and platform.system() != 'Darwin'):
    print "Including all files"
    data_files += [
        (os.path.join(usr_share, 'applications/'), ['ltclectrum.desktop']),
        (os.path.join(usr_share, 'app-install', 'icons/'), ['icons/ltclectrum.png'])
    ]
    if not os.path.exists('locale'):
        os.mkdir('locale')
    for lang in os.listdir('locale'):
        if os.path.exists('locale/%s/LC_MESSAGES/electrum.mo' % lang):
            data_files.append((os.path.join(usr_share, 'locale/%s/LC_MESSAGES' % lang), ['locale/%s/LC_MESSAGES/electrum.mo' % lang]))

appdata_dir = util.appdata_dir()
if not os.access(appdata_dir, os.W_OK):
    appdata_dir = os.path.join(usr_share, "ltclectrum")

data_files += [
    (appdata_dir, ["data/README"]),
    (os.path.join(appdata_dir, "cleanlook"), [
        "data/cleanlook/name.cfg",
        "data/cleanlook/style.css"
    ]),
    (os.path.join(appdata_dir, "sahara"), [
        "data/sahara/name.cfg",
        "data/sahara/style.css"
    ]),
    (os.path.join(appdata_dir, "dark"), [
        "data/dark/background.png",
        "data/dark/name.cfg",
        "data/dark/style.css"
    ])
]


setup(
    name="LTCLectrum",
    version=version.ELECTRUM_VERSION,
    install_requires=['slowaes', 'ecdsa>=0.9'],
    package_dir={
        'ltclectrum': 'lib',
        'ltclectrum_gui': 'gui',
        'ltclectrum_plugins': 'plugins',
    },
    scripts=['ltclectrum'],
    data_files=data_files,
    py_modules=[
        'ltclectrum.account',
        'ltclectrum.bitcoin',
        'ltclectrum.blockchain',
        'ltclectrum.bmp',
        'ltclectrum.commands',
        'ltclectrum.i18n',
        'ltclectrum.interface',
        'ltclectrum.mnemonic',
        'ltclectrum.msqr',
        'ltclectrum.network',
        'ltclectrum.plugins',
        'ltclectrum.pyqrnative',
        'ltclectrum.simple_config',
        'ltclectrum.socks',
        'ltclectrum.transaction',
        'ltclectrum.util',
        'ltclectrum.verifier',
        'ltclectrum.version',
        'ltclectrum.wallet',
        'ltclectrum.wallet_bitkey',
        'ltclectrum.wallet_factory',
        'ltclectrum_gui.gtk',
        'ltclectrum_gui.qt.__init__',
        'ltclectrum_gui.qt.amountedit',
        'ltclectrum_gui.qt.console',
        'ltclectrum_gui.qt.history_widget',
        'ltclectrum_gui.qt.icons_rc',
        'ltclectrum_gui.qt.installwizard',
        'ltclectrum_gui.qt.lite_window',
        'ltclectrum_gui.qt.main_window',
        'ltclectrum_gui.qt.network_dialog',
        'ltclectrum_gui.qt.password_dialog',
        'ltclectrum_gui.qt.qrcodewidget',
        'ltclectrum_gui.qt.receiving_widget',
        'ltclectrum_gui.qt.seed_dialog',
        'ltclectrum_gui.qt.transaction_dialog',
        'ltclectrum_gui.qt.util',
        'ltclectrum_gui.qt.version_getter',
        'ltclectrum_gui.stdio',
        'ltclectrum_gui.text',
        'ltclectrum_plugins.aliases',
        'ltclectrum_plugins.exchange_rate',
        'ltclectrum_plugins.labels',
        'ltclectrum_plugins.pointofsale',
        'ltclectrum_plugins.qrscanner',
        'ltclectrum_plugins.virtualkeyboard',
    ],
    description="Lightweight Litecoin Wallet",
    author="bwrega",
    author_email="wregab@github",
    license="GNU GPLv3",
    url="http://ltclectrum.org",
    long_description="""Lightweight Litecoin Wallet"""
)
