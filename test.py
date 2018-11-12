import sys
 
class Tee(object):
    def __init__(self, *files):
        self.files = files
    def write(self, obj):
        for f in self.files:
            f.write(obj.encode('utf-8'))
 
if __name__ == "__main__":
    f = open('logfile.txt', 'w')
    original = sys.stdout
    sys.stdout = Tee(sys.stdout, f)
    print("test")  # This will go to stdout and the file out.txt
 
    #use the original
    sys.stdout = original
    print("This won't appear on file")  # Only on stdout
    f.close()