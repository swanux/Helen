#! /usr/bin/env python3

import sys, os
from gi.repository import GObject, Gio, Polkit

def on_tensec_timeout(loop):
  print("Ten seconds have passed. Now exiting.")
  loop.quit()
  return False

def check_authorization_cb(authority, res, loop):
    try:
        result = authority.check_authorization_finish(res)
        if result.get_is_authorized():
            print("Authorized")
            os.system('whoami')
        elif result.get_is_challenge():
            print("Challenge")
        else:
            print("Not authorized")
    except GObject.GError as error:
         print("Error checking authorization")
        
    print("Authorization check has been cancelled "
          "and the dialog should now be hidden.\n"
          "This process will exit in ten seconds.")
    GObject.timeout_add(10000, on_tensec_timeout, loop)

def do_cancel(cancellable):
    print("Timer has expired; cancelling authorization check")
    cancellable.cancel()
    return False

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: %s <action_id>" % sys.argv[0])
        sys.exit(1)
    action_id = sys.argv[1]

    mainloop = GObject.MainLoop()
    authority = Polkit.Authority.get()
    subject = Polkit.UnixProcess.new(os.getppid())

    cancellable = Gio.Cancellable()
    GObject.timeout_add(10 * 1000, do_cancel, cancellable)

    authority.check_authorization(subject,
        action_id, #"org.freedesktop.policykit.exec",
        None,
        Polkit.CheckAuthorizationFlags.ALLOW_USER_INTERACTION,
        cancellable,
        check_authorization_cb,
        mainloop)

    mainloop.run()