# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['mainn.py'],
    pathex=['G:\\xiangmu\\justMonika\\venv\\lib\\site-packages\\cv2\\'],
    binaries=[],
    datas=[
        ('bgm', 'bgm'),
        ('font', 'font'),
        ('png', 'png'),
        ('set.json', '.'),
        ('a.ico', '.')
    ],
    hiddenimports=['win32api', 'win32con', 'win32gui'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['_gtkagg', '_tkagg', 'bsddb', 'curses', 'pywin.debugger', 'pywin.debugger.dbgcon',
             'pywin.dialogs', 'tcl', 'Tkconstants', 'Tkinter', 'pydoc', 'doctest', 'test', 'sqlite3',
             'email', 'unittest', 'xml', 'PyQt4', 'PyQt5', 'sip', 'PyQt4.QtGui', 'PyQt5.QtGui', 'matplotlib'],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='mainn',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='mainn',
)
