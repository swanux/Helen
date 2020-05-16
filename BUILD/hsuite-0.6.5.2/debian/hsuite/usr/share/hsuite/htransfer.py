#! /usr/bin/python3
# -*- coding: utf-8 -*-

import os
import sys
import time
import argparse
import shutil

class Transser:

    def reset(self):
        global filePer
        global allSize
        global currPer
        global notVir
        global yetFil
        yetFil = ""
        filePer = 0
        allSize = 0
        currPer = 0
        notVir = False

    def yes_or_no(self, question, typ):
        reply = str(input(question+' (y/n): ')).lower().strip()
        if reply[0] == 'y':
            if typ == 'dir':
                shutil.rmtree(dst, ignore_errors=True)
            else:
                os.remove(dst)
        elif reply[0] == 'n':
            print('Aborting')
            sys.exit(1)
        else:
            return self.yes_or_no("Invalid selection! : ", typ)

    def main(self, src, dst, start1):
        global currPer
        '''
        Copy a large file showing progress.
        '''
        src = src.replace('\ ', ' ')
        dst = dst.replace('\ ', ' ')
        if os.path.exists(src) is False:
            print('ERROR: file/folder does not exist: "{}"'.format(src))
            sys.exit(1)
        if os.path.exists(dst) is True:
            if os.path.isdir(dst):
                if dst.split('/')[-1] == None or dst.split('/')[-1] == "":
                    pass
                    canpass = True
                else:
                    self.yes_or_no('Destination directory already exist! Would you like to continue and remove it?', 'dir')
            else:
                self.yes_or_no('Destination file already exist! Would you like to continue and remove it?', 'file')
        if os.path.exists(dst) is True and canpass != True:
            print('ERROR: file exists, cannot overwrite it: "{}"'.format(dst))
            sys.exit(1)
        self.UP = '\x1b[1A'
        self.DEL = '\x1b[2K'
        try:
            if os.path.isdir(src):
                splitt = src.split('/')
                for i in range(len(splitt)):
                    if splitt[i] == "" and i != 0 or splitt[i] == None and i != 0:
                        break
                    else:
                        justDir = splitt[i]
                for (dirpath, dirnames, filenames) in os.walk(src):
                    dirList = dirpath.split('/')
                    newDirList = []
                    for i in range(len(dirList)):
                        if dirList[i] != justDir:
                            if dirList[i] == None or dirList[i] == "":
                                pass
                            else:
                                newDirList.append('/%s' % dirList[i])
                        else:
                            newDirList.append('/')
                            break
                    for filename in filenames:
                        f = os.path.join(dirpath, filename)
                        try:
                            relPath = dirpath.replace(''.join(newDirList), "")
                            relPath = relPath.replace(' ', '\ ')
                            relPath = relPath.replace("'", "\\'")
                            if dst.split('/')[-1] == None or dst.split('/')[-1] == "":
                                os.system('mkdir -p %s%s' % (dst, relPath))
                            else:
                                os.system('mkdir -p %s/%s' % (dst, relPath))    
                        except:
                            pass
                        relPath = relPath.replace("\\'", "'")
                        relPath = relPath.replace('\ ', ' ')
                        if dst.split('/')[-1] == None or dst.split('/')[-1] == "":
                            self.calcs(f, 10000, '%s%s/%s' % (dst, relPath, filename), allSize, currPer)
                        else:
                            self.calcs(f, 10000, '%s/%s/%s' % (dst, relPath, filename), allSize, currPer)
                if mv == True:
                    shutil.rmtree(src, ignore_errors=True)
            else:
                splitt = src.split('/')
                for i in range(len(splitt)):
                    if splitt[i] == "" and i != 0 or splitt[i] == None and i != 0:
                        break
                    else:
                        justFil = splitt[i]
                if dst.split('/')[-1] == None or dst.split('/')[-1] == "":
                    self.calcs(src, 10000, '%s%s' % (dst, justFil), allSize, currPer)
                else:
                    self.calcs(src, 10000, dst, allSize, currPer)
                if mv == True:
                    os.remove(src)
        except IOError as obj:
            print('\nERROR: {}'.format(obj))
            sys.exit(1)


    def oneFile(self, fullSize, lastPer):
        global filePer
        global notVir
        global currPer
        self.copied = 0  # bytes
        self.chunk = self.ifp.read(int(self.chunk_size))
        while self.chunk:
            # Write and calculate how much has been written so far.
            self.ofp.write(self.chunk)
            self.copied += len(self.chunk)
            per = 100. * float(self.copied) / float(self.size)
            if fullSize != 0:
                allPer = 100. * float(self.copied) / float(fullSize) + lastPer
            # Calculate the speed.
            elapsed = time.time() - self.start  # elapsed so far
            avg_byte_per_time = float(self.copied) / elapsed
            avg_mbyte_per_time = avg_byte_per_time / (1024*1024)
            if __name__ == '__main__':
                sys.stdout.write(self.UP + self.UP + self.DEL + '%s MB/s\n\n' % avg_mbyte_per_time)
            # Write out the status.
            if __name__ == '__main__':
                if fullSize != 0:
                    sys.stdout.write(self.UP + self.DEL + '%s %%\n' % allPer)
                else:
                    sys.stdout.write(self.UP + self.DEL + '%s %%\n' % per)

            # Calculate the estimated time remaining.
            avg_time_per_byte = elapsed / float(self.copied)
            if fullSize != 0:
                fullCopied = (fullSize / 100) * allPer
                remaining = fullSize - fullCopied
            else:
                remaining = self.size - self.copied
            est = remaining * avg_time_per_byte
            if __name__ == '__main__':
                sys.stdout.write(self.DEL + 'ETA: %s s\r' % est)
            if __name__ == '__main__':
                sys.stdout.flush()
                notVir = True
            # Read in the next chunk.
            self.chunk = self.ifp.read(int(self.chunk_size))
            filePer = per
            currPer = allPer

    def calcs(self, current, divisor, dest, fullSize=0, lastPer=0):
        global notVir
        global yetFil
        self.start = time.time()
        self.size = os.stat(current).st_size
        self.chunk_size = self.size / divisor
        while self.chunk_size == 0 and divisor > 10:
            divisor /= 10
            self.chunk_size = self.size / divisor
        with open(current, 'rb') as self.ifp:
            if __name__ == '__main__':
                # if notVir == True:
                #     sys.stdout.write(self.UP + self.UP + self.UP + self.DEL + 'Current file is %s\n\n\n' % current)
                #     notVir = False
                # else:
                os.system('clear')
                sys.stdout.write(self.DEL + 'Current file is %s\n\n\n' % current)
            yetFil = current
            with open(dest, 'wb') as self.ofp:
                self.oneFile(fullSize, lastPer)

    def modPre(self, modSr, modDs):
        global allSize
        dst = modDs
        src = modSr.split(', ')
        start1 = time.time()
        self.reset()
        if len(src) == 1:
            src = src[0]
            src = src.replace('\ ', ' ')
            if os.path.isdir(src):
                listOfFiles = list()
                for (dirpath, dirnames, filenames) in os.walk(src):
                    listOfFiles += [os.path.join(dirpath, file) for file in filenames]
                for i in listOfFiles:
                    allSize += os.stat(i).st_size
            else:
                allSize += os.stat(src).st_size
            self.main(src, dst, start1)
        elif len(src) >= 2:
            listOfFiles = list()
            for item in src:
                item = item.replace('\ ', ' ')
                if os.path.isdir(item):
                    for (dirpath, dirnames, filenames) in os.walk(item):
                        listOfFiles += [os.path.join(dirpath, file) for file in filenames]
                    for i in listOfFiles:
                        allSize += os.stat(i).st_size
                else:
                    allSize += os.stat(item).st_size
            for item in src:
                self.main(item, dst, start1)

if __name__ == '__main__':
    arger = argparse.ArgumentParser(description='HTransfer: python recursive file transfer backend with status indication.\nDesigned for eXternOS, by swanux')
    group = arger.add_mutually_exclusive_group(required=True)

    group.add_argument("-mv", default=None, help="Move file/folder", action="store_true")
    group.add_argument("-cp", default=None, help="Copy file/folder", action="store_true")
    arger.add_argument("-src", "--source", default=None, help="Source folder/file", required=True)
    arger.add_argument("-dst", "--destination", default=None, help="Destination folder/file", required=True)

    args = arger.parse_args()
    mv = args.mv
    cp = args.cp
    src = args.source
    dst = args.destination
    src = src.split(', ')
    start1 = time.time()
    Transser().reset()
    if len(src) == 1:
        src = src[0]
        src = src.replace('\ ', ' ')
        if os.path.isdir(src):
            listOfFiles = list()
            for (dirpath, dirnames, filenames) in os.walk(src):
                listOfFiles += [os.path.join(dirpath, file) for file in filenames]
            for i in listOfFiles:
                allSize += os.stat(i).st_size
        else:
            allSize += os.stat(src).st_size
        Transser().main(src, dst, start1)
    elif len(src) >= 2:
        listOfFiles = list()
        for item in src:
            item = item.replace('\ ', ' ')
            if os.path.isdir(item):
                for (dirpath, dirnames, filenames) in os.walk(item):
                    listOfFiles += [os.path.join(dirpath, file) for file in filenames]
                for i in listOfFiles:
                    allSize += os.stat(i).st_size
            else:
                allSize += os.stat(item).st_size
        for item in src:
            Transser().main(item, dst, start1)
    elapsed = time.time() - start1
    print('\ncopied everything in {:>.1f} s'.format(elapsed))
else:
    mv = False
    print('Module mode')