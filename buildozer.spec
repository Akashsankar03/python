[app]

# Title of your application
title = My Application

# Package name
package.name = myapp

# Package domain (needed for Android/iOS packaging)
package.domain = org.test

# Source directory where the main.py lives
source.dir = .

# Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# Application versioning
version = 0.1

# Application requirements
requirements = python3,kivy,kivymd,pillow

# Supported orientations
orientation = portrait

# Android specific settings
fullscreen = 0
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True

# Log level
log_level = 2
warn_on_root = 1
