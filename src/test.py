import os
import time

arr = []

pid = os.fork()

if pid:
  print('Child')

if not pid:
  print("parent")