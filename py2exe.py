# -*- coding: utf-8 -*-

"""
Desc: 将python脚本转换成windows下exe可执行文件
"""

import os
import shutil
import sys

class Py2Exe:
   def py2exe(self,argv=None):
        if argv==None:
            FileName = raw_input('Input Python file name:').strip()
        else:
            FileName = argv[1].strip()

        if FileName[0]=='\"' or FileName[0]=='\'':   # 去除引号
            FileName = FileName[1:-1]
        FileName = FileName.split('\\')[-1]    # 截取文件名

        # 生成exe文件
        CurrentPath = os.getcwd()
        PyInstaller = sys.path[0]+"\\InstallPackage\\PyInstaller-3.2.1\\pyinstaller.py"   # 安装器位置
        PyFile_1 = sys.path[0]+'\\'+FileName              # 转换文件
        SpecFile = CurrentPath+'\\'+FileName[:-3]+'.spec'     # 要删除的spec文件
        ExeFile_1 = "%s.exe"%(FileName[:-3])        # 生成的exe文件名
        ExePath_1 = "%s\\dist\\%s"%(CurrentPath,ExeFile_1)  # exe文件所在目录
        CopyPath_1 = "%s\\%s"%(CurrentPath,ExeFile_1)        # exe文件复制目录

        if os.path.exists(sys.path[0]+'\\'+ExeFile_1):
            print "%s exists，no need to turn!"%(ExeFile_1)
            return False
        else:
            # 转换开始
            os.system('python "%s" --console --onefile "%s"'%(PyInstaller,PyFile_1))


        # 移动exe文件，删除多余文件
        if os.path.exists(ExePath_1):
            print u'exe生成完毕'
            print u'复制文件%s到%s……' % (ExePath_1,CopyPath_1)
            shutil.copy(ExePath_1,CopyPath_1)
            if argv != None:
                print u'复制文件%s到%s……' % (CopyPath_1,sys.path[0]+'\\'+ExeFile_1)
                shutil.move(CopyPath_1,sys.path[0]+'\\'+ExeFile_1)
        else:
            print u'exe生成失败'
            print u'文件%s不存在'%(ExePath_1)
            return False

        if os.path.exists(CurrentPath+"\\dist"):
            print u'删除目录%s……' % (CurrentPath+"\\dist")
            shutil.rmtree(CurrentPath+"\\dist")
        else:
            print u'目录%s不存在'%(CurrentPath+"\\dist")
            return False

        if os.path.exists(CurrentPath+"\\build"):
            print u'删除目录%s……' % (CurrentPath+"\\build")
            shutil.rmtree(CurrentPath+"\\build")
        else:
            print u'目录%s不存在'%(CurrentPath+"\\build")
            return False

        if os.path.exists(SpecFile):
            print u'删除文件%s……' % (SpecFile)
            os.remove(SpecFile)
        else:
            print u'文件%s不存在'%(SpecFile)
            return False
        return True


if __name__=='__main__':
    # 判断是否是在直接运行该.py文件
    if len(sys.argv)==1:
        Py2Exe().py2exe()
    elif len(sys.argv)==2:
        Py2Exe().py2exe(sys.argv)
    else:
        print u'ERROR:Wrong Input!\n'
    raw_input('\nPress "Enter" to quit!')