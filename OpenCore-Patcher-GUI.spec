# -*- mode: python ; coding: utf-8 -*-

import sys, os
sys.path.append(os.path.abspath(os.getcwd()))
from resources import constants
block_cipher = None


a = Analysis(['OpenCore-Patcher-GUI.command'],
             pathex=['resources', 'data', 'gui'],
             binaries=[],
             datas=[('payloads', 'payloads')],
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
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
          a.binaries,
          a.zipfiles,
          a.datas,  
          [],
          name='OpenCore-Patcher',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None )
app = BUNDLE(exe,
             name='OpenCore-Patcher.app',
             icon="payloads/OC-Patcher.icns",
             bundle_identifier="com.dortania.opencore-legacy-patcher-wxpython",
             info_plist={
             "CFBundleShortVersionString": constants.Constants().patcher_version,
             "NSHumanReadableCopyright": "Copyright 2020-2022 Dortania",
             "LSMinimumSystemVersion": "10.10.0",
             "NSRequiresAquaSystemAppearance": False,
             "NSHighResolutionCapable": True,
             })
