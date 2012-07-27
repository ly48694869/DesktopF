#!/usr/bin/env python2.7
#coding=utf-8
import pygtk
pygtk.require( '2.0')
import gtk

class DisplayWindow:
    def __init__( self):
        self.window = gtk.Window( gtk.WINDOW_TOPLEVEL)
        self.window.resize( 400, 400)
        self.window.connect( 'delete_event', self.delete_event)
        self.window.connect( 'destroy', self.destroy)
        self.window.connect( 'button_press_event', self.button_press_callback)
        self.window.connect( 'button_release_event', self.button_release_callback)
        self.window.connect( 'scroll_event', self.scroll_callback)
        self.window.connect( 'key_release_event', self.key_release_callback)
        self.window.connect( 'motion_notify_event', self.motion_callback)
        self.window.show( )
        
    def motion_callback( self, widget, event, data=None):
        print 'motion', event, data

    def button_press_callback( self, widget, event, data=None):
        print 'button pressed',event, data

    def button_release_callback( self, widget, event, data=None):
        print 'button release', event, data
        
    def scroll_callback( self, widget, event, data=None):
        print 'scroll event', event, data

    def key_release_callback( self, widget, event, data=None):
        print 'key release', event, data
                

    def fku( self, widget, data=None):
        print 'fucking ur little sister\'s ass'
    def delete_event( self, widget, event, data=None):
        print 'deleting...'
        return False
    def destroy( self, widget, data=None):
        gtk.main_quit( )
    def show( self):
        gtk.main( )
    
    

if __name__ == '__main__':
    win = DisplayWindow( )
    win.show( )
