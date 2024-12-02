import cx_Freeze

executables = [cx_Freeze.Executable('main.py')]

cx_Freeze.setup(
    name="Secretaria | CBB",
    options={'build_exe': {'packages': ['kivy', 'pandas', 'selenium']}},
    executables = executables
)