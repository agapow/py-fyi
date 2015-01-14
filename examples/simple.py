"""
A trivial example of using fyi.
"""

print "Starting ..."
import fyi


def notify_all_levels():
   print "Notifying on all levels:"
   fyi.critical ('a message')
   fyi.error ('a message')
   fyi.warning ('a message')
   fyi.info ('a message')
   fyi.debug ('a message')


print "\nUsing default notification level:"
notify_all_levels()

print "\nSetting level to everything:"
fyi.set_level (fyi.EVERYTHING)
notify_all_levels()

print "\nSetting level to nothing:"
fyi.set_level (fyi.NOTHING)
notify_all_levels()

print "\nSetting level to warning:"
fyi.set_level (fyi.WARNING)
notify_all_levels()

print "\nSetting level to debug:"
fyi.set_level (fyi.DEBUG)
notify_all_levels()

