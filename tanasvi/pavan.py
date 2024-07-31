import ctypes
import os
import sys
import winreg

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def set_windows_timezone(timezone_name):
    try:
        # Open the registry key for time zones
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, 'SYSTEM\\CurrentControlSet\\Control\\TimeZoneInformation', 0, winreg.KEY_SET_VALUE)

        # Set the time zone information
        winreg.SetValueEx(key, 'TimeZoneKeyName', 0, winreg.REG_SZ, timezone_name)

        # Close the registry key
        winreg.CloseKey(key)

        print(f"System time zone set to: {timezone_name}")
    except Exception as e:
        print(f"Error setting system time zone: {e}")

if is_admin():
    # Set the desired time zone
    desired_timezone = 'Eastern Standard Time'  # Change this to the desired time zone

    # Set the Windows time zone
    set_windows_timezone(desired_timezone)
else:
    # Re-run the script with admin privileges
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
