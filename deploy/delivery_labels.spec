# deploy/delivery_labels.spec
import os

# Pega o diretório atual (deploy/, por causa do cd deploy)
base_path = os.path.abspath(os.getcwd())  # deploy/
# Ajusta pra raiz do projeto subindo um nível
base_path = os.path.abspath(os.path.join(base_path, '..'))

a = Analysis(
    [os.path.join(base_path, 'delivery_labels.py')],  # Caminho correto na raiz
    pathex=[base_path],
    binaries=[],
    datas=[
        (os.path.join(base_path, 'templates', '*.zpl'), 'templates'),
        (os.path.join(base_path, 'resources', 'icons', '*.ico'), 'resources/icons'),
    ],
    hiddenimports=['pywin32'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='delivery_labels',
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
    icon=os.path.join(base_path, 'resources', 'icons', 'barcode.ico'),
)

coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='delivery_labels',
)