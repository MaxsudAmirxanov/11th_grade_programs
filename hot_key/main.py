
# from pynput import keyboard
 
# cmb = [{keyboard.Key.shift, keyboard.Key(char='a')},{keyboard.Key.shift, keyboard.Key(char='A')}]
 
# current = set()
 
# def execute():
#   print("Detected hotkey")
 
# def on_press(key):
#   if any([key in z for z in cmb]):
#     current.add(key)
#     if any(all(k in current for k in z) for z in cmb):
#       execute()
 
# def on_release(key):
#   if any([key in z for z in cmb]):
#     current.remove(key)
 
# with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
#   listener.join()

# Keyboard module in Python
# import keyboard
# import pyautogui
 
# # press ctrl+shift+z to print "Hotkey Detected"
# def test():
#     print('12234')
#     print(pyautogui.position())
#     pyautogui.moveTo(x=442, y=828)
#     pyautogui.click()
# keyboard.add_hotkey('ctrl + q', test)
 
# keyboard.wait('esc')
# num1 = 41
# print(num1.())

a = [1963, 83, 4731,739]
b = []
for i in a:
    b.append((list(str(i))))

print(b)