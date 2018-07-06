import sys

sys.stdout.flush()
sys.stdout.write('Here is the line \r')
sys.stdout.flush()
sys.stdout.write('Here is the line2')
sys.stdout.write('\n')
for i in range(0, 5000000+1):
    sys.stdout.write(f'{i}\r')
sys.stdout.write('\n')
