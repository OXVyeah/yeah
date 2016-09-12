import win32gui
import win32ui
import win32con
import win32api
def run(**args):
    print("screenshotter=============!!!!!!!!!!!")
    # grab a handle to the main desktop window
    hdesktop = win32gui.GetDesktopWindow()

    print("1")
    # determine the size of all monitors in pixels
    width = win32api.GetSystemMetrics(win32con.SM_CXVIRTUALSCREEN)
    height = win32api.GetSystemMetrics(win32con.SM_CYVIRTUALSCREEN)
    left = win32api.GetSystemMetrics(win32con.SM_XVIRTUALSCREEN)
    top = win32api.GetSystemMetrics(win32con.SM_YVIRTUALSCREEN)

    print("2")
    # create a device context
    desktop_dc = win32gui.GetWindowDC(hdesktop)
    img_dc = win32ui.CreateDCFromHandle(desktop_dc)

    print("3")
    # create a memory based device context
    mem_dc = img_dc.CreateCompatibleDC()

    print("4")
    # create a bitmap object
    screenshot = win32ui.CreateBitmap()
    screenshot.CreateCompatibleBitmap(img_dc, width, height)
    mem_dc.SelectObject(screenshot)

    print("5")
    # copy the screen into our memory device context
    mem_dc.BitBlt((0, 0), (width, height), img_dc, (left, top), win32con.SRCCOPY)

    print("6")
    # save the bitmap to a file
    screenshot.SaveBitmapFile(mem_dc, 'c:\\pyworks\\before\\screenshot.bmp')
    print("7")
    img=mem_dc
    # free our objects
    mem_dc.DeleteDC()
    print("8")
    win32gui.DeleteObject(screenshot.GetHandle())
    print("screenshotter OVER!!!!!!!!!!!")
    return str(mem_dc)
