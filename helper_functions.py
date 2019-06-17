import textwrap
import time
import os

''' Textwrap wrapper'''
def WrappedTextOutput(p_text, p_width=70):
  wrapped_text = textwrap.wrap(p_text, p_width)
  for s in wrapped_text:
    print(s)
    
def clear_screen():
  if os.name == 'nt':
    _ = os.system('cls')
  else:
    _ = os.system('clear')
  
  print('\n'*50)
  time.sleep(0.1)
