# -*- mode: python -*-
a = Analysis(['bindit.py'],
             pathex=['/Users/thomaseffland/Development/projects/Brett'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='bindit',
          debug=False,
          strip=None,
          upx=True,
          console=True )
