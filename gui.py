
# coding: utf-8

# In[5]:

import os
import wx
import wx.lib.agw.multidirdialog as MDD

from mtgMgr import dataMgr
from mtgMgr import treasMgr
from bloombergBooks import books as books
from washSales import washMgr

wildcard = "Python source (*.py)|*.py|"             "All files (*.*)|*.*"


# In[6]:

class Example(wx.Frame):

    def __init__(self, parent, title, *args, **kw):
        super(Example, self).__init__(parent, title=title)
        
        self.currentDirectory = os.getcwd()

        panel = wx.Panel(self)
        sizer = wx.GridBagSizer(5, 5)
        
        #----------------------------------------------------
        text1 = wx.StaticText(panel, label="Compliance Manager")
        sizer.Add(text1, pos=(0, 0), flag=wx.TOP|wx.LEFT|wx.BOTTOM,
            border=15)

        icon = wx.StaticBitmap(panel, bitmap=wx.Bitmap('C:\\Users\\XBBNQVM\\Desktop\\bny.png'))
        sizer.Add(icon, pos=(0, 4), flag=wx.TOP|wx.RIGHT|wx.ALIGN_RIGHT,
            border=5)

        line = wx.StaticLine(panel)
        sizer.Add(line, pos=(1, 0), span=(1, 5),
            flag=wx.EXPAND|wx.BOTTOM, border=10)
        #----------------------------------------------------
        
        #text next to date box
        dateText = wx.StaticText(panel, label="Date use YYYY-MM-DD Format")
        sizer.Add(dateText, pos=(2, 0), flag=wx.LEFT, border=10)
        #positing in contorl panel
        self.tc1 = wx.TextCtrl(panel)
        sizer.Add(self.tc1, pos=(2, 1), span=(1, 3), flag=wx.TOP|wx.EXPAND)
        
        #----------------------------------------------------
        #File Lcoation 
        fileLocText = wx.StaticText(panel, label="File Location")
        sizer.Add(fileLocText, pos=(3, 0), flag=wx.LEFT|wx.TOP, border=10)

        #Text box next to file location
        self.tc2 = wx.TextCtrl(panel, value='C:\\')
        sizer.Add(self.tc2, pos=(3, 1), span=(1, 3), flag=wx.TOP|wx.EXPAND,
            border=5)


        button1 = wx.Button(panel, label="Browse")
        sizer.Add(button1, pos=(3, 4), flag=wx.TOP|wx.RIGHT, border=5)
        button1.Bind(wx.EVT_BUTTON, self.onDir)

        #---------------------------------------------------
        
        text4 = wx.StaticText(panel, label="Save Location")
        sizer.Add(text4, pos=(4, 0), flag=wx.TOP|wx.LEFT, border=10)

        self.tc3 = wx.TextCtrl(panel)
        sizer.Add(self.tc3, pos=(4, 1), span=(1, 3),
            flag=wx.TOP|wx.EXPAND, border=5)

        button2 = wx.Button(panel, label="Browse...")
        sizer.Add(button2, pos=(4, 4), flag=wx.TOP|wx.RIGHT, border=5)
        button2.Bind(wx.EVT_BUTTON, self.onDirSave)
        #----------------------------------------------------

        button3 = wx.Button(panel, label='Help')
        sizer.Add(button3, pos=(7, 0), flag=wx.LEFT, border=10)

        button4 = wx.Button(panel, label="Ok")
        button4.Bind(wx.EVT_BUTTON, self.onOk)
        sizer.Add(button4, pos=(7, 3))

        #----------------------------------------------------
        
        self.radio1 = wx.RadioButton(panel, label = 'Mortgage Best Ex')
        sizer.Add(self.radio1, pos=(6,1))
        
        
        #-----------------------------------------------------
        
        self.radio2 = wx.RadioButton(panel, label = 'Treasury Best Ex')
        sizer.Add(self.radio2, pos=(6,2))
        
        
        #-------------
        self.radio3 = wx.RadioButton(panel, label = 'Wash Sale Report Bloomberg')
        sizer.Add(self.radio3, pos=(6,3))
        

        
        sizer.AddGrowableCol(2)

        panel.SetSizer(sizer)
        sizer.Fit(self)
        
        self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)

        self.SetTitle('Compliance Manager')
        self.Centre()
        #path = onDir(self)
    
    #def fileLocation(self, e):
        
        
        
    def OnCloseWindow(self, e):

        dial = wx.MessageDialog(None, 'Are you sure to quit?', 'Question',
            wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION)

        ret = dial.ShowModal()

        if ret == wx.ID_YES:
            self.Destroy()
        else:
            e.Veto()
            
    def onDir(self, event):
        """
        Show the DirDialog and print the user's choice to stdout
        """
        dlg = wx.DirDialog(self, "Choose a directory:",
                           style=wx.DD_DEFAULT_STYLE
                           #| wx.DD_DIR_MUST_EXIST
                           #| wx.DD_CHANGE_DIR
                           )
        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
            self.tc2.SetValue(path)
            
    
    def onDirSave(self, event):
        """
        Show the DirDialog and print the user's choice to stdout
        """
        dlg = wx.DirDialog(self, "Choose a directory:",
                           style=wx.DD_DEFAULT_STYLE
                           #| wx.DD_DIR_MUST_EXIST
                           #| wx.DD_CHANGE_DIR
                           )
        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
            self.tc3.SetValue(path)
            
    def onOk(self, event):
        
        if self.radio1.GetValue() == True:
            
            dlg = wx.MessageDialog(self, "Run Mortage Best Ex Rept?",
                           style=wx.DD_DEFAULT_STYLE
                           #| wx.DD_DIR_MUST_EXIST
                           #| wx.DD_CHANGE_DIR
                           )
            
            if dlg.ShowModal() == wx.ID_OK:

        
                date = self.tc1.GetValue()
                bloomy = self.tc2.GetValue() + '\\'   
                save = self.tc3.GetValue()+ "\\"
        
                mtgMgr = dataMgr(date, bloomy, save)
                mtgMgr.save()
        
        elif self.radio2.GetValue() == True:
            dlg = wx.MessageDialog(self, "Run Treasury Best Ex Rept",
                           style=wx.DD_DEFAULT_STYLE
                           #| wx.DD_DIR_MUST_EXIST
                           #| wx.DD_CHANGE_DIR
                           )
            
            if dlg.ShowModal() == wx.ID_OK:
                date = self.tc1.GetValue()
                bloomy = self.tc2.GetValue()+"\\"
                save = self.tc3.GetValue()+"\\"
                
                treasMgr1 = treasMgr(date, bloomy, save)
                treasMgr1.save()
                
        elif self.radio3.GetValue() == True:
            dlg = wx.MessageDialog(self, "Run Wash Report?",
                           style=wx.DD_DEFAULT_STYLE
                           #| wx.DD_DIR_MUST_EXIST
                           #| wx.DD_CHANGE_DIR
                           )
            
            if dlg.ShowModal() == wx.ID_OK:
                date = self.tc1.GetValue()
                bloomy = self.tc2.GetValue()+"\\"
                save = self.tc3.GetValue()+"\\"
                
                wash = washMgr(bloomy, save, date)
                wash.save()

        elif OSError:
            dlg = wx.MessageDialog(self, "File Location Incorrect",
                               style = wx.DD_DEFAULT_STYLE)
            
            dlg.ShowModal()
        
        else:
            dlg = wx.MessageDialog(self, "choose a report type",
                               style = wx.DD_DEFAULT_STYLE)
            
            dlg.ShowModal()    



def main():
    app = wx.App()
    ex = Example(None, title="Compliance manager")
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()


# In[ ]:



