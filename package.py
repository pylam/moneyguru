# -*- coding: utf-8 -*-
# Created By: Virgil Dupras
# Created On: 2009-12-30
# Copyright 2010 Hardcoded Software (http://www.hardcoded.net)
# 
# This software is licensed under the "HS" License as described in the "LICENSE" file, 
# which should be included with this package. The terms are also available at 
# http://www.hardcoded.net/licenses/hs_license

import sys
import os
import os.path as op
import compileall
import shutil

import yaml

from core.app import Application as MoneyGuru
from hsutil.build import build_dmg, copy_packages, build_debian_changelog

def package_windows():
    pythonpath = os.environ.get('PYTHONPATH', '')
    pythonpath = ';'.join([op.abspath('.'), pythonpath]) if pythonpath else op.abspath('.')
    os.environ['PYTHONPATH'] = pythonpath
    os.chdir('qt')
    os.system('python build.py')
    os.chdir('..')

def package_debian():
    if op.exists('build'):
        shutil.rmtree('build')
    destpath = op.join('build', 'moneyguru-{0}'.format(MoneyGuru.VERSION))
    srcpath = op.join(destpath, 'src')
    os.makedirs(destpath)
    shutil.copytree('qt', srcpath)
    copy_packages(['hsutil', 'hsgui', 'core', 'qtlib'], srcpath)
    shutil.copytree('debian', op.join(destpath, 'debian'))
    build_debian_changelog(op.join('help', 'changelog.yaml'), op.join(destpath, 'debian', 'changelog'), 'moneyguru', from_version='1.8.0')
    shutil.copytree(op.join('help', 'moneyguru_help'), op.join(srcpath, 'help'))
    shutil.copy(op.join('images', 'logo_small.png'), srcpath)
    compileall.compile_dir(srcpath)
    os.chdir(destpath)
    os.system("dpkg-buildpackage")

def main():
    conf = yaml.load(open('conf.yaml'))
    ui = conf['ui']
    dev = conf['dev']
    if dev:
        print "You can't package in dev mode"
        return
    print "Packaging moneyGuru with UI {0}".format(ui)
    if ui == 'cocoa':
        build_dmg('cocoa/build/release/moneyGuru.app', '.')
    elif ui == 'qt':
        if sys.platform == "win32":
            package_windows()
        elif sys.platform == "linux2":
            package_debian()
        else:
            print "Qt packaging only works under Windows or Linux."

if __name__ == '__main__':
    main()
