# -*- mode: python -*-

block_cipher = None


a = Analysis(['server.py'],
             pathex=['/Users/phillipmalboeuf/Desktop/class'],
             binaries=None,
             datas=[('/Users/phillipmalboeuf/Desktop/class/environment/lib/python3.5/site-packages/livereload/vendors/livereload.js', './livereload/vendors'),('/Users/phillipmalboeuf/Desktop/class/environment/lib/python3.5/site-packages/babeljs/static/babeljs/browser.js', './babeljs/static/babeljs'),('/Users/phillipmalboeuf/Desktop/class/environment/lib/python3.5/site-packages/babeljs/static/regenerator/runtime.js', './babeljs/static/regenerator')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='server',
          debug=False,
          strip=False,
          upx=True,
          console=False )
app = BUNDLE(exe,
             name='server.app',
             icon=None,
             bundle_identifier=None)
