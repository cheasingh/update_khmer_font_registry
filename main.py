import winreg


def set_run_key(key, value):
    reg_key = winreg.OpenKey(
        winreg.HKEY_LOCAL_MACHINE, r'SOFTWARE\Microsoft\Windows NT\CurrentVersion\FontSubstitutes',
        0,
        winreg.KEY_ALL_ACCESS
    )

    with reg_key:
        if value is None:
            print('key not found, please check your path')
        else:
            winreg.SetValueEx(reg_key, key, 0,
                              winreg.REG_SZ, value)
            print(f"update successfully {key} with value {value}")


set_run_key("MS Shell Dlg 2", "Khmer OS")
