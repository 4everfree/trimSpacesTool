import os

def trimSpace(dir, name):
    if name.endswith('url') or name.endswith('docx'):
        os.remove(name)
        return
    os.rename(dir + '/' + name, dir + '/' + name.strip())



if __name__ == '__main__':
    dirs = os.listdir(os.getcwd())
    for dir in dirs:
        if os.path.isdir(dir):
            filePath = os.listdir(dir)
            for name in filePath:
                trimSpace(dir, name)
        else:
            trimSpace('./', name)