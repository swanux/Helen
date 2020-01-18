#!/usr/bin/env python3
# -*- coding: utf-8 -*-



# Download methods

# Disable or enable buttons based on a pattern
def toggle(self, fn):
    print(self, fn, state)
    for i in range(dlistLen):
        print("Toggle %s" % i)
        if dlist[i] != Tdownl and shDict[dlist[i]] != "PFalse":
            print(dlist[i], shDict[dlist[i]], Tdownl)
            cBut = self.builder.get_object(dlist[i])
            GLib.idle_add(cBut.set_sensitive, state)
            shDict[dlist[i]] = "%s" % state
    global scanningUrl
    scanningUrl = False

# Starting download in a background thread BUT inside the GUI class, not the thread. This is because of the nature of GTK (and other GUI toolkits) that can't handle GUI changes from outside of the main thread (gui class)
def ex_target(self, block_sz, downl, file_size, file_name, file_size_dl, u, f):
    print("DLthread...")
    # This variable shows if the thread needs to exit
    global quit
    quit = False
    while not quit:
        # Reads the downloaded bytes in blocks
        buffer = u.read(block_sz)
        if not buffer:
            # break if error occures
            break
        # Set the downloaded file size to buffer
        file_size_dl += len(buffer)
        # write this block to the downloaded file
        f.write(buffer)
        status = r"Cancel  [%3.2f%%]" % (
            file_size_dl * 100 / file_size)  # Calculate precentage
        # Place on waiting list to change the label to the actual status
        GLib.idle_add(downl.set_label, status)
    print("DLend!!")
    # Shows that no downloads are running
    global runE
    runE = False
    # Set back the button label to the original
    GLib.idle_add(downl.set_label, orig)
    print('quit: %s' % quit)
    print(orig)
    print("Label restore")
    # If the download is aborted by the user, remove the already downloaded file
    if rmE:
        os.system('rm /home/%s/Downloads/%s' % (user, file_name))
    else:
        # Set label to ready
        GLib.idle_add(downl.set_label, "Ready in ~/Downloads/")
        # Disable button
        GLib.idle_add(downl.set_sensitive, False)
        # Set the state to permanent false
        shDict[Tdownl] = "PFalse"
        print("done with it")
    quit = True

def on_downl_begin(self, url, downl):
    # Open the url
    global runE
    global state
    u = urlopen(url)
    if runE == True:                                                  # If download is already running
        # set remove flag to true
        global rmE
        rmE = True
        # tell the thread to stop
        global quit
        quit = True
        print("TruTogle")
        # set button state to enabled
        state = True
        # enable every button
        self.toggle(fn)
        return
    elif runE == False:                                               # If no downloads are running
        # toggle that now one is running
        runE = True
        # we don't need to remove the downloaded file, because it's ready
        rmE = False
        # save the original label of the button
        global orig
        orig = downl.get_label()
    file_name = url.split('/')[-1]
    f = open('/home/%s/Downloads/%s' %
                (user, file_name), 'wb')  # set download location
    print('Downloading %s' % file_name)
    print("FalsTogle")
    # disable buttons
    state = False
    # run function to do this
    self.toggle(fn)
    t1 = futures.ThreadPoolExecutor(
        max_workers=4)                    # init thread
    # start it
    f = t1.submit(self.ex_target, 8192, downl, int(
        u.getheader('Content-Length')), file_name, 0, u, f)
    # set buttons to active
    state = True
    # after done run this function
    f.add_done_callback(self.toggle)