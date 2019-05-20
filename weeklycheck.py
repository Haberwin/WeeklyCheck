#!/usr/bin/env python
# -*-coding:utf-8-*-
import traceback

__author__ = 'zhanghuiliang@sagereal.com'

import sys
import time
import re
import base64
import smtplib
from uiautomator import device as d
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

# 这里import别的脚本里面的方法
from log import Log
from html import *

# reload(sys)
sys.setdefaultencoding('utf8')


class WeeklyCheck(object):
    def __init__(self):
        info = d.info
        self.displayWidth = info[u'displayWidth']
        self.displayHeight = info[u'displayHeight']

    def start(self):
        d.screen.on()
        d.swipe(int(self.displayWidth * 0.5), int(self.displayHeight * 0.9), int(self.displayWidth * 0.5), 0)
        d.press.home()

    def delete(self):
        d.press.recent()
        d(resourceId="com.android.systemui:id/button_remove_all").click()
        d.press.home()

    def findapk(self, apkname):
        d(resourceId="com.android.launcher3:id/all_apps_handle").click()
        while not d(text="%s" % (apkname)).exists:
            d.swipe(int(self.displayWidth * 0.5), int(self.displayHeight * 0.9), int(self.displayWidth * 0.5),
                    int(self.displayHeight * 0.2))
            time.sleep(5)

        d(text="%s" % (apkname)).click()

    @staticmethod
    def setupwizard():
        Log.Blue("start to skip setupwizard\n")
        d.watcher('start').when(resourceId="com.google.android.setupwizard:id/start").click(
            resourceId="com.google.android.setupwizard:id/start")
        d.watcher('skip').when(resourceId="com.google.android.setupwizard:id/skip_button").click(
            resourceId="com.google.android.setupwizard:id/skip_button")
        d.watcher('next').when(resourceId="com.google.android.setupwizard:id/next_button").click(
            resourceId="com.google.android.setupwizard:id/next_button")
        d.watcher('next1').when(resourceId="com.google.android.gms:id/next_button").click(
            resourceId="com.google.android.gms:id/next_button")
        d.watcher('button').when(resourceId="android:id/button1").click(resourceId="android:id/button1")
        d.watcher('accetp').when(text=u'以后再说').click(text=u'以后再说')
        d.watcher('startcn').when(resourceId="com.android.provision:id/next").click(
            resourceId="com.android.provision:id/next")
        d.watcher('startcn1').when(resourceId="com.android.provision:id/datetime_next").click(
            resourceId="com.android.provision:id/datetime_next")
        d.watcher('startcn2').when(resourceId="com.android.provision:id/btn_user").click(
            resourceId="com.android.provision:id/btn_user")

        for i in range(20):
            d.watchers.run()
            time.sleep(2)

        d.watchers.remove()

    def setting(self):
        self.start()
        Log.Blue("start to get phone info\n")
        tr = "<tr><td colspan=\"4\" style=\"width:400px\" bgcolor=\"#D4E9A9\"><B>设置</B></td></tr>"
        self.findapk("设置")

        try:
            time.sleep(5)
            d.swipe(int(self.displayWidth * 0.5), int(self.displayHeight * 0.9), int(self.displayWidth * 0.5), 0)
            d(text="系统").click()

            time.sleep(5)
            d.swipe(int(self.displayWidth * 0.5), int(self.displayHeight * 0.9), int(self.displayWidth * 0.5), 0)
            d(text="关于手机").click()

            time.sleep(5)
            d.swipe(int(self.displayWidth * 0.5), int(self.displayHeight * 0.9), int(self.displayWidth * 0.5), 0)
            d.screenshot("about_phone.png")
            tr += "<tr><td>版本信息</td><td><img src=about_phone.png  height=\"400\" width=\"300\"/></td></tr><tr></tr>"

        except BaseException as e:
            print("\n")
            Log.Warning("click settings fail\n")
            traceback.print_exc()
            d.screenshot("seterror1.png")
            # tr += "<tr><td>版本信息</td><td bgcolor=\"#FF0000\">F</td><td><img src=seterror1.png  height=\"400\" width=\"200\"/></td></tr><tr></tr>"
            tr += "<tr><td>版本信息</td><td bgcolor=\"#FF0000\">F</td>\
                   <td><img src=\"cid:imageid\"  height=\"400\" width=\"200\"/></td></tr><tr></tr>"

            img = open("seterror1.png", "rb")
            img_data = img.read()
            img.close()

        time.sleep(5)

        # 打开oem

        # 打开play权限
        try:
            Log.Blue("open google play permission \n")
            d.press.back()
            d.press.back()

            d(text="安全性和位置信息").click()
            time.sleep(5)

            if not d(text="Google Play 保护机制").exists:
                d(text="位置信息").click()
            else:
                d(text="Google Play 保护机制").click()
                d(text="关闭").click()
                d(text="关闭").click()
                tr += "<tr><td>play权限</td><td>P</td></tr>"

        except BaseException as e:
            print("\n")
            Log.Warning("open google play permission fail\n")
            traceback.print_exc()
            d.screenshot("seterror2.png")
            tr += "<tr><td>google play权限</td><td bgcolor=\"#FF0000\">F</td><td><img src=seterror2.png  height=\"400\" width=\"200\"/></td></tr><tr></tr>"

        time.sleep(5)

        # 打开wifi
        try:
            Log.Blue("connect wifi maidu_north_5g \n")
            d.press.back()
            d.press.back()

            time.sleep(5)
            d.swipe(int(self.displayWidth * 0.5), int(self.displayHeight * 0.2), int(self.displayWidth * 0.5),
                    int(self.displayHeight))

            d(text="网络和互联网").click()
            d(text="WLAN").click()

            time.sleep(5)
            if d(text="关闭").exists:
                d(text="关闭").click()

            d(text="maidu_north_5g").click()
            time.sleep(5)

            if d(text=u'确定').exists:
                d(text="确定").click()

            time.sleep(5)
            if d(text=u'允许').exists:
                d(text="允许").click()

            d(resourceId="com.android.settings:id/password").set_text("maidu2018")
            d(resourceId="android:id/button1").click()
            tr += "<tr><td>连接wifi</td><td>P</td></tr>"

        except BaseException as e:
            print("\n")
            Log.Warning("connect wifi maidu_north_5g \n")
            traceback.print_exc()
            d.screenshot("seterror3.png")
            tr += "<tr><td>连接wifi</td><td bgcolor=\"#FF0000\">F</td><td><img src=seterror3.png  height=\"400\" width=\"200\"/></td></tr><tr></tr>"

        time.sleep(5)

        # 设置休眠时间
        try:
            Log.Blue("set sleep time to 30min\n")
            d.press.back()
            d.press.back()

            time.sleep(5)
            d(text="显示").click()

            d(text="休眠").click()
            d(text="30分钟").click()
            tr += "<tr><td>设置休眠时间</td><td>P</td></tr>"

        except BaseException as e:
            print("\n")
            Log.Warning("set sleep time to 30min \n")
            traceback.print_exc()
            d.screenshot("seterror4.png")
            tr += "<tr><td>设置休眠时间</td><td bgcolor=\"#FF0000\">F</td><td><img src=seterror4.png  height=\"400\" width=\"200\"/></td></tr><tr></tr>"

        time.sleep(5)
        self.delete()
        return tr

    # 判断菜单能否正常下拉
    def drag(self):
        Log.Blue("start to test quick setting\n")
        tr = "<tr><td colspan=\"4\" style=\"width:400px\" bgcolor=\"#D4E9A9\"><B>下拉菜单</B></td></tr>"

        d.swipe(0, 0, 0, int(self.displayHeight))
        if not d(resourceId="com.android.systemui:id/settings_button").exists:
            Log.Red("can't drag quick setting \n")
            d.screenshot("quickerror1.png")
            tr += "<tr><td>下拉菜单</td><td bgcolor=\"#FF0000\">F</td><td><img src=quickerror1.png  height=\"400\" width=\"200\"/></td></tr><tr></tr>"
        else:
            tr += "<tr><td>下拉菜单</td><td>P</td></tr>"

        d.press.home()
        return tr

    def dialer(self):
        Log.Blue("start to test dialer \n")
        tr = "<tr><td colspan=\"4\" style=\"width:400px\" bgcolor=\"#D4E9A9\"><B>电话</B></td></tr>"
        self.findapk("电话")

        # 拨打电话
        try:
            d(resourceId="com.android.dialer:id/floating_action_button").click()
            d(resourceId="com.android.dialer:id/one").click()
            d(resourceId="com.android.dialer:id/zero").click()
            d(resourceId="com.android.dialer:id/zero").click()
            d(resourceId="com.android.dialer:id/eight").click()
            d(resourceId="com.android.dialer:id/six").click()
            d(resourceId="com.android.dialer:id/dialpad_floating_action_button").click()

            time.sleep(5)
            if not d(resourceId="com.android.dialer:id/incall_end_call").exists:
                Log.Red("Call failed \n")
                d.screenshot("diaerror1.png")
                tr += "<tr><td>拨打电话</td><td bgcolor=\"#FF0000\" width=\"100\">F</td><td><img src=diaerror1.png  height=\"400\" width=\"200\"/></td></tr><tr></tr>"
            else:
                tr += "<tr><td>拨打电话</td><td>P</td></tr>"
                time.sleep(5)

                d(resourceId="com.android.dialer:id/incall_third_button").click()
                tr += "<tr><td>免提</td><td>P</td></tr>"
                time.sleep(5)

                d(resourceId="com.android.dialer:id/incall_end_call").click()
                tr += "<tr><td>挂断</td><td>P</td></tr>"

        except BaseException as e:
            print("\n")
            Log.Warning("Dialing fail\n")
            traceback.print_exc()
            d.screenshot("diaerror2.png")
            tr += "<tr><td>拨打电话</td><td bgcolor=\"#FF0000\">F</td><td><img src=diaerror2.png  height=\"400\" width=\"200\"/></td></tr><tr></tr>"

        # 删除通话记录
        time.sleep(5)
        try:
            d(className="android.widget.RelativeLayout", index="1").click()
            if d(resourceId="com.android.dialer:id/empty_list_view_action").exists:
                d(resourceId="com.android.dialer:id/empty_list_view_action").click()

            d(resourceId="com.android.dialer:id/primary_action_view").click()
            d(resourceId="com.android.dialer:id/details_action").click()
            d(resourceId="com.android.dialer:id/call_detail_delete_menu_item").click()
            tr += "<tr><td>删除通话记录</td><td>P</td></tr>"
        except BaseException as e:
            print("\n")
            Log.Warning("Delete call records fail\n")
            traceback.print_exc()
            d.screenshot("diaerror3.png")
            tr += "<tr><td>删除通话记录</td><td bgcolor=\"#FF0000\">F</td><td><img src=diaerror3.png  height=\"400\" width=\"200\"/></td></tr><tr></tr>"

        self.delete()
        return tr

    def gmscontacts(self):
        Log.Blue("start to test contacts \n")
        tr = "<tr><td colspan=\"4\" style=\"width:400px\" bgcolor=\"#D4E9A9\"><B>通讯录</B></td></tr>"
        self.findapk("通讯录")

        # 添加联系人
        time.sleep(5)
        if d(text=u'跳过').exists:
            d.press.back()

        try:
            time.sleep(5)
            if d(resourceId="com.google.android.contacts:id/secondary_button").exists:
                d(resourceId="com.google.android.contacts:id/secondary_button").click()

            d(resourceId="com.google.android.contacts:id/floating_action_button").click()
            d(text="姓氏").set_text("test")
            d(text="名字").set_text("test1")

            d.swipe(int(self.displayWidth * 0.5), int(self.displayHeight * 0.5), int(self.displayWidth * 0.5),
                    int(self.displayHeight * 0.2))
            d(text="电话").set_text("10086")

            if d(resourceId="com.android.vending:id/negative_button").exists:
                d(resourceId="com.android.vending:id/negative_button").click()
            d(resourceId="com.google.android.contacts:id/menu_save").click()
            time.sleep(5)
            tr += "<tr><td>添加联系人</td><td>P</td></tr>"

        except BaseException as e:
            print("\n")
            Log.Warning("create new contacts fail\n")
            traceback.print_exc()
            d.screenshot("gconerror1.png")
            tr += "<tr><td>添加联系人</td><td bgcolor=\"#FF0000\" width=\"100\">F</td><td><img src=gconerror1.png  height=\"400\" width=\"200\"/></td></tr><tr></tr>"

        try:
            Log.Blue("Delete contacters \n")
            d.press.back()
            if d(textContains="test"):
                d(textContains="test").long_click()

                d(resourceId="com.google.android.contacts:id/menu_delete").click()
                d(text="删除").click()
                tr += "<tr><td>删除联系人</td><td>P</td></tr>"

        except BaseException as e:
            print("\n")
            Log.Warning("delete new contacts fail\n")
            traceback.print_exc()
            d.screenshot("gconerror2.png")
            tr += "<tr><td>删除联系人</td><td bgcolor=\"#FF0000\" width=\"100\">F</td><td><img src=gconerror2.png  height=\"400\" width=\"200\"/></td></tr><tr></tr>"

        self.delete()
        return tr

    def contacts(self):
        Log.Blue("start to test contacts \n")
        tr = "<tr><td colspan=\"4\" style=\"width:400px\" bgcolor=\"#D4E9A9\"><B>通讯录</B></td></tr>"
        self.findapk("通讯录")

        try:
            d(resourceId="com.android.contacts:id/floating_action_button").click()
            d(text="手机联系人").click()

            d(text="姓氏").set_text("test")
            d(text="名字").set_text("test1")
            d(text="电话").set_text("10086")

            d(resourceId="com.android.contacts:id/editor_menu_save_button").click()
            time.sleep(5)
            tr += "<tr><td>添加联系人</td><td>P</td></tr>"

        except BaseException as e:
            print("\n")
            Log.Warning("create new contacts fail\n")
            traceback.print_exc()
            d.screenshot("conerror1.png")
            tr += "<tr><td>添加联系人</td><td bgcolor=\"#FF0000\" width=\"100\">F</td><td><img src=conerror1.png  height=\"400\" width=\"200\"/></td></tr><tr></tr>"

        try:
            Log.Blue("Delete contacters \n")
            d.press.back()
            if d(textContains="test"):
                d(textContains="test").long_click()

                d(resourceId="com.android.contacts:id/menu_delete").click()
                d(text="删除").click()
                tr += "<tr><td>删除联系人</td><td>P</td></tr>"

        except BaseException as e:
            print("\n")
            Log.Warning("delete new contacts fail\n")
            traceback.print_exc()
            d.screenshot("conerror2.png")
            tr += "<tr><td>删除联系人</td><td bgcolor=\"#FF0000\" width=\"100\">F</td><td><img src=conerror2.png  height=\"400\" width=\"200\"/></td></tr><tr></tr>"

        self.delete()
        return tr

    def gmessage(self):
        Log.Blue("start to test gms message \n")
        tr = "<tr><td colspan=\"4\" style=\"width:400px\" bgcolor=\"#D4E9A9\"><B>信息</B></td></tr>"
        self.findapk("信息")

        # 发送短息
        try:
            time.sleep(5)
            d(resourceId="com.google.android.apps.messaging:id/start_new_conversation_button").click()
            d(resourceId="com.google.android.apps.messaging:id/recipient_text_view").set_text("10086")

            time.sleep(5)
            d.click(int(self.displayWidth * 0.94), int(self.displayHeight * 0.94))
            d(text="短信").set_text('11')
            d(resourceId="com.google.android.apps.messaging:id/send_message_button_container").click()
            tr += "<tr><td>gms短信</td><td>P</td></tr>"

        except BaseException as e:
            print("\n")
            Log.Warning("send gmessage fail\n")
            traceback.print_exc()
            d.screenshot("gmerror1.png")
            tr += "<tr><td>gms短信</td><td bgcolor=\"#FF0000\">F</td><td><img src=gmerror1.png  height=\"400\" width=\"200\"/></td></tr><tr></tr>"

        # 删除短信
        try:
            Log.Blue("test delete message \n")
            d.press.back()
            d.press.back()
            if d(textContains="您").exists:
                d(textContains="您").long_click()

                d(resourceId="com.google.android.apps.messaging:id/action_delete").click()
                d(text="删除").click()
                tr += "<tr><td>删除短信</td><td>P</td></tr>"

        except BaseException as e:
            print("\n")
            Log.Warning("delete gmessage fail\n")
            traceback.print_exc()
            d.screenshot("gmerror2.png")
            tr += "<tr><td>删除短信</td><td bgcolor=\"#FF0000\">F</td><td><img src=gmerror2.png  height=\"400\" width=\"200\"/></td></tr><tr></tr>"

        self.delete()
        return tr

    def message(self):
        Log.Blue("start to test message \n")
        tr = "<tr><td colspan=\"4\" style=\"width:400px\" bgcolor=\"#D4E9A9\"><B>信息</B></td></tr>"
        self.findapk("信息")

        # 发送短息
        try:
            time.sleep(5)
            d(resourceId="com.android.mms:id/action_compose_new").click()

            time.sleep(5)
            d(resourceId="com.android.mms:id/recipients_editor").set_text("10086")
            d(resourceId="com.android.mms:id/embedded_text_editor").set_text("11")

            d(resourceId="com.android.mms:id/send_button_sms").click()
            tr += "<tr><td>短信</td><td>P</td></tr>"

        except BaseException as e:
            print("\n")
            Log.Warning("send message fail\n")
            traceback.print_exc()
            d.screenshot("merror1.png")
            tr += "<tr><td>gms短信</td><td bgcolor=\"#FF0000\">F</td><td><img src=merror1.png  height=\"400\" width=\"200\"/></td></tr><tr></tr>"

        # 删除短信
        try:
            Log.Blue("test delete message \n")
            d.press.back()
            d.press.back()
            if d(textContains="10086").exists:
                d(textContains="10086").long_click()

                d(resourceId="com.android.mms:id/delete").click()
                d(text="删除").click()
                tr += "<tr><td>删除短信</td><td>P</td></tr>"

        except BaseException as e:
            print("\n")
            Log.Warning("delete gmessage fail\n")
            traceback.print_exc()
            d.screenshot("merror2.png")
            tr += "<tr><td>删除短信</td><td bgcolor=\"#FF0000\">F</td><td><img src=merror2.png  height=\"400\" width=\"200\"/></td></tr><tr></tr>"

        self.delete()
        return tr

    def camera(self):
        # start()
        Log.Blue("start to test camera \n")
        tr = "<tr><td colspan=\"4\" style=\"width:400px\" bgcolor=\"#D4E9A9\"><B>相机</B></td></tr>"
        self.findapk("相机")

        # 拍照
        try:
            d(resourceId="com.mediatek.camera:id/shutter_image").click()
            tr += "<tr><td>拍照</td><td>P</td></tr>"
        except BaseException as e:
            print("\n")
            Log.Warning("click camera fail\n")
            traceback.print_exc()
            d.screenshot("camerror.png")
            tr += "<tr><td>拍照</td><td bgcolor=\"#FF0000\">F</td><td><img src=camerror.png  height=\"400\" width=\"200\"/></td></tr><tr></tr>"

        # 闪光灯
        time.sleep(20)
        try:
            d(resourceId="com.mediatek.camera:id/flash_icon").click()
            d(resourceId="com.mediatek.camera:id/flash_on").click()
            d(resourceId="com.mediatek.camera:id/shutter_image").click()
            tr += "<tr><td>闪光灯</td><td>P</td></tr>"
        except BaseException as e:
            print("\n")
            Log.Warning("click camera fail\n")
            traceback.print_exc()
            d.screenshot("camerror.png")
            tr += "<tr><td>闪光灯</td><td bgcolor=\"#FF0000\">F</td><td><img src=camerror.png  height=\"400\" width=\"200\"/></td></tr><tr></tr>"

        # HDR
        time.sleep(5)
        try:
            d(resourceId="com.mediatek.camera:id/hdr_icon").click()
            d(resourceId="com.mediatek.camera:id/shutter_image").click()
            tr += "<tr><td>HDR</td><td>P</td></tr>"
        except BaseException as e:
            print("\n")
            Log.Warning("click camera fail\n")
            traceback.print_exc()
            d.screenshot("camerror1.png")
            tr += "<tr><td>HDR</td><td bgcolor=\"#FF0000\">F</td><td><img src=camerror1.png  height=\"400\" width=\"200\"/></td></tr><tr></tr>"

        # 视频
        time.sleep(5)
        try:
            d(text="视频").click()
            d(text="视频").click()
            d(resourceId="com.mediatek.camera:id/shutter_image").click()
            time.sleep(5)
            d(resourceId="com.mediatek.camera:id/video_stop_shutter").click()
            tr += "<tr><td>录像</td><td>P</td></tr>"
        except BaseException as e:
            print("\n")
            Log.Warning("click camera fail\n")
            traceback.print_exc()
            d.screenshot("camerror2.png")
            tr += "<tr><td>录像</td><td bgcolor=\"#FF0000\">F</td><td><img src=camerror2.png  height=\"400\" width=\"200\"/></td></tr><tr></tr>"

        d.press.back()
        self.delete()
        return tr

    def scanner(self):
        Log.Blue("start to test scanner \n")
        d(resourceId="com.android.launcher3:id/all_apps_handle").click()
        tr = "<tr><td colspan=\"4\" style=\"width:400px\" bgcolor=\"#D4E9A9\"><B>测试scanner</B></td></tr>"

        try:
            d(text="扫描头").click()
            time.sleep(5)

            d(text="开始扫描").click()
            tr += "<tr><td>扫描</td><td>P</td></tr>"

        except BaseException as e:
            print("\n")
            Log.Warning("click scanner fail\n")
            traceback.print_exc()
            d.screenshot("scaerror.png")
            tr += "<tr><td>扫描头</td><td bgcolor=\"#FF0000\">F</td><td><img src=scaerror.png  height=\"400\" width=\"200\"/></td></tr><tr></tr>"

        self.delete()
        return tr

    # 点开所有apk，查看是否有fc
    def allapk(self):
        Log.Blue("start to touch all apks\n")
        tr = "<tr><td colspan=\"4\" style=\"width:400px\" bgcolor=\"#D4E9A9\"><B>点击所有apk</B></td></tr>"

        all_list = []
        i = 0

        d.watcher('allowroot').when(text=u'允许').click(text=u'允许')
        d.watcher('OK').when(text=u'OK').click(text=u'OK')
        d.watcher('skip').when(text=u'跳过').click(text=u'跳过')
        d.watcher('keepclose').when(text=u'保持关闭状态').click(text=u'保持关闭状态')
        d.watcher('disable').when(text=u'禁用SOFTSPOT').click(text=u'禁用SOFTSPOT')
        d.watcher('exit').when(text=u'退出').click(text=u'退出')
        d.watcher('accept').when(text=u'accept').click(text=u'accept')
        d.watcher('allowp').when(resourceId="com.android.packageinstaller:id/permission_allow_button").click(
            resourceId="com.android.packageinstaller:id/permission_allow_button")

        try:
            d(resourceId="com.android.launcher3:id/all_apps_handle").click()
            time.sleep(5)

            while True:
                for a in d(resourceId="com.android.launcher3:id/icon"):
                    d.screen.on()

                    if a.text not in all_list:
                        print(a.text)
                        all_list.append(a.text)

                        if a.text == "SureFox":
                            continue
                        else:
                            a.click()

                        print(i)
                        i = i + 1
                        d.watchers.run()

                        time.sleep(10)
                        if d(resourceId="com.google.android.apps.photos:id/auto_backup_switch").exists:
                            d.press.back()

                        # 判断是否有FC
                        if d(textContains="停止运行").exists:
                            d.screenshot("error%s.png" % (a.text))
                            tr += "<tr><td>%s</td><td bgcolor=\"#FF0000\">F</td><td><img src=error%s.png  height=\"400\" width=\"200\"/></td></tr><tr></tr>" % (
                                a.text, a.text)

                        if d(textContains="没有响应").exists:
                            d.screenshot("error%s.png" % (a.text))
                            tr += "<tr><td>%s</td><td bgcolor=\"#FF0000\">F</td><td><img src=error%s.png  height=\"400\" width=\"200\"/></td></tr><tr></tr>" % (
                                a.text, a.text)

                        d.press.back()

                        tr += "<tr><td>%s</td><td>P</td></tr>" % (a.text)

                    time.sleep(5)

                print(i)
                print(all_list)

                if i % 20 == 0:
                    d.swipe(int(self.displayWidth * 0.5), int(self.displayHeight * 0.9), int(self.displayWidth * 0.5),
                            int(self.displayHeight * 0.2))
                    Log.Blue("test next page \n")
                else:
                    break

        except BaseException as e:
            print("\n")
            Log.Warning("click apk fail \n")
            traceback.print_exc()
            d.screenshot("apkerror.png")
            tr += "<tr><td>打开所有apk</td><td bgcolor=\"#FF0000\">F</td><td><img src=apkerror.png  height=\"400\" width=\"200\"/></td></tr><tr></tr>"

        self.delete()
        return tr

    def sendemail(self, html):
        subject = "每日自动化测试脚本结果"
        msg = MIMEMultipart("related")

        index_alist = [i.start() for i in re.finditer('src=', html)][::-1]
        index_blist = [i.start() for i in re.finditer('.png', html)][::-1]
        png_list = []

        if len(index_alist) != len(index_blist):
            print("html is not matched ,exit")
            sys.exit(1)

        for i in range(len(index_alist)):
            png_info = html[index_alist[i] + 4:index_blist[i]]
            html = html.replace("%s.png" % (png_info), "\"cid:%s\"" % (png_info))
            png_list.append(png_info)

        content = MIMEText(html, 'html', 'utf-8')
        msg.attach(content)

        msg['Subject'] = subject
        msg['From'] = "Jenkins<huiliang.zhang@mobiiot.com.cn>"
        recivers = ["MD-Software/RD/MobiIoT@mobiiot.com.cn", "MD-Test/RD/MobiIoT@mobiiot.com.cn"]
        # recivers = ["huiliang.zhang@mobiiot.com.cn"]
        msg['To'] = ";".join(recivers)

        for png in png_list:
            file1 = open("%s.png" % (png), "rb")
            img_data = file1.read()
            file1.close()

            img = MIMEImage(img_data)
            img.add_header('Content-ID', png)
            msg.attach(img)

        try:
            passwd = base64.decodestring("emhsMjIwNDA4")
            smtp = smtplib.SMTP(timeout=30 * 60)
            smtp.connect("mail.sagereal.com")
            smtp.login("huiliang.zhang@mobiiot.com.cn", passwd)
            smtp.sendmail("Jenkins<huiliang.zhang@mobiiot.com.cn>", recivers, msg.as_string())
            smtp.close()
            return True
        except Exception as e:
            traceback.print_exc()
            return False

    def gmsmokey(self):
        self.setupwizard()
        d.watcher('safe').when(text=u'要开启 Play 保护机制吗？').click(resourceId="com.android.vending:id/positive_button")
        # d.watcher('safe').when(text=u'要开启 Play 保护机制吗？').click(text=u'接受')
        d.watchers.run()

        tr = "<H2>Dailybuild 测试报告<H2>"
        tr += self.setting()
        tr += self.drag()
        tr += self.dialer()
        tr += self.gmscontacts()
        tr += self.gmessage()
        tr += self.camera()
        tr += self.scanner()
        tr += self.allapk()

        html = HTML % (TABLE_CSS_STYLE, tr)
        html = html.encode("utf-8")

        with open("report.html", "w") as fd:
            fd.write(html)

        self.sendemail(html)

    def cnmokey(self):
        self.setupwizard()
        tr = "<H2>Dailybuild 测试报告<H2>"
        tr += self.setting()
        tr += self.drag()
        tr += self.dialer()
        tr += self.contacts()
        tr += self.message()
        tr += self.camera()
        tr += self.scanner()
        tr += self.allapk()

        html = HTML % (TABLE_CSS_STYLE, tr)
        html = html.encode("utf-8")

        with open("report.html", "w") as fd:
            fd.write(html)

        self.sendemail(html)


if __name__ == "__main__":
    sys.stdout = sys.stderr
    mokey = WeeklyCheck()
    if sys.argv[1] == "gms":
        Log.Blue("The GMS mokey test start \n")
        mokey.gmsmokey()
    else:
        Log.Blue("The CN mokey test start \n")
        mokey.cnmokey()
