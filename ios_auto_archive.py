#-*- coding:utf-8 -*-
#
# Copyright 2015 EricTang
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#    http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
#
#   Author  :   EricTang
#   E-mail  :   jeepxiaozi66@gmail.com
#   Date    :   2015/05/25 19:12:44
#   Desc    :   iOS自动打包分发脚本——仅供内部测试用，如作其他用途，本人不负责任何连带责任
#	Other	:	其他联系方式：QQ-994773216，新浪微博：http://weibo.com/u/1375170263
#

import os
import re
import sys
import config
import socket
import zipfile
import plistlib
import subprocess

# Xcode工程路径 - 需要手动指定
PROJECT_DIRECTORY = "Xcode工程路径"

# 应用下载地址
APP_DOWNLOAD_URL = "app下载URL"

# 生成Build的目录 - 无需手动更改
BUILD_DIRECTORY = PROJECT_DIRECTORY + "build/"

# Xcode工程中用于Daily Build的Configuration，需要在iOS的工程中添加相应的配置，”DailyBuild“是配置名
BUILD_CONFIG = "DailyBuild"

# 打包生成的Build目录 - 无需更改
BUILD_ARCHIVE = BUILD_CONFIG + "-iphoneos"

def getTargetName():
	"""
	获取当前要操作的项目的Target
	"""
	global target_name
	# 列出当前目录下所有文件
	file_list = os.listdir(PROJECT_DIRECTORY)

	# 找到Xcode的Target
	for file_name in file_list:
		if "xcodeproj" in file_name:
			target_name = file_name.split(".")[0]
#end def

def autoArchiveIpa():
	"""
	自动打包生成ipa文件
	"""
	# 组装构建命令
	archive_cmd = "xcodebuild -scheme %s  archive -archivePath %s%s.xcarchive -configuration %s " % \
	 (target_name, PROJECT_DIRECTORY, target_name, BUILD_CONFIG)
	# 切换工作目录
	os.chdir(PROJECT_DIRECTORY)
	# 开始构建
	subprocess.call(archive_cmd, shell=True)
	# 打包成ipa
	ipa_cmd = "xcodebuild -exportArchive -exportFormat ipa -archivePath %s%s.xcarchive  -exportPath %s%s.ipa" % (PROJECT_DIRECTORY, target_name, PROJECT_DIRECTORY, target_name)
	subprocess.call(ipa_cmd, shell=True)
#end def

def getPlistRoot(file_path):
	"""
	根据ipa文件获取plist节点
	"""
	print(file_path)
	if os.path.exists(file_path):
		ipa_file = zipfile.ZipFile(file_path)
		info_plist = getPlistFromZipFile(ipa_file)
		info_plist_data = ipa_file.read(info_plist)
		info_plist_root = plistlib.loads(info_plist_data)
		return info_plist_root
# end def

def getPlistFromZipFile(zip_file):
	"""
	找到ipa文件中的Info.plist文件
	"""
	file_name_list = zip_file.namelist()
	info_plist_re_pattern = re.compile(r"Payload/[^/]*.app/Info.plist")
	for file_name in file_name_list:
		match = info_plist_re_pattern.match(file_name)
		if match is not None:
			print(u"bingo，找到文件" + file_name)
			return match.group()
# end def

def generatePlist(info_plist_root, app_title, ipd_url):
	"""
	根据读取到的Info.plist文件内容生成plist文件
	"""
	print(u"应用名 : %s" % info_plist_root["CFBundleDisplayName"])
	print(u"Bundle Id : %s" % info_plist_root["CFBundleIdentifier"])
	print(u"版本号 : %s" % info_plist_root["CFBundleShortVersionString"])
	print(u"应用标题 : %s" % app_title)
	print(u"ipa文件下载地址 : %s" % ipd_url)
	# 组装要生成的plist文件
	metadata_dict = {
		"bundle-identifier" : info_plist_root["CFBundleIdentifier"],
		"bundle-version" : info_plist_root["CFBundleShortVersionString"],
		"kind" : "software",
		"title" : app_title,
	}
	pl = dict (
		items = [
			dict(
				assets = [dict(kind = "software-package", url = ipd_url)],
				metadata = metadata_dict,
				)
		],
		)
	with open(info_plist_root["CFBundleDisplayName"] + ".plist", "wb") as fp:
		plistlib.dump(pl, fp)
# end def

if __name__ == "__main__":
	# 获取项目Target名
	getTargetName()
	# 自动构建ipa文件
	autoArchiveIpa()
	# 判断target_name是否获取到
	global ipa_path
	if target_name:
		# ipa文件地址
		ipa_path = PROJECT_DIRECTORY + target_name + ".ipa"
	if os.path.exists(ipa_path):
		os.chdir(PROJECT_DIRECTORY)
		generatePlist(getPlistRoot(ipa_path), target_name, APP_DOWNLOAD_URL + target_name + ".ipa")