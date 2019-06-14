import textwrap
import time

''' Textwrap wrapper'''
def WrappedTextOutput(p_text, p_width=70):
  wrapped_text = textwrap.wrap(p_text, p_width)
  for s in wrapped_text:
    print(s)
    
def clear_screen():
  print('\033[H\033[J')
  print('\n'*250)
  print('\033[J\033[H') #moves the cursor back to the top
  time.sleep(0.1)


