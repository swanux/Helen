# -*- mode: python3 ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['/home/daniel/GitRepos/hsuite/DEV_FILES/HSuite.py'],
             pathex=['/home/daniel/GitRepos'],
             binaries=[],
             datas=[ ('osLayer.py', '.'), ('details.py', '.'), ('colors.css', '.'), ('pacman.conf', '.'), ('config.yml', '.'), ('hsuite.glade', '.'), ('icons', 'icons'), ('fusuma.desktop', '.'), ('hsuite.desktop', '.'), ('hsuite', '.'), ('translations', 'translations') ],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='HSuite',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='HSuite')
