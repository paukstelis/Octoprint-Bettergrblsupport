#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Written by:  Shell M. Shrader (https://github.com/synman/Octoprint-Bettergrblsupport)
#
#                               Apache License
#                         Version 2.0, January 2004
#                      http://www.apache.org/licenses/
#
# TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION
#
# 1. Definitions.
#
#    "License" shall mean the terms and conditions for use, reproduction,
#    and distribution as defined by Sections 1 through 9 of this document.
#
#    "Licensor" shall mean the copyright owner or entity authorized by
#    the copyright owner that is granting the License.
#
#    "Legal Entity" shall mean the union of the acting entity and all
#    other entities that control, are controlled by, or are under common
#    control with that entity. For the purposes of this definition,
#    "control" means (i) the power, direct or indirect, to cause the
#    direction or management of such entity, whether by contract or
#    otherwise, or (ii) ownership of fifty percent (50%) or more of the
#    outstanding shares, or (iii) beneficial ownership of such entity.
#
#    "You" (or "Your") shall mean an individual or Legal Entity
#    exercising permissions granted by this License.
#
#    "Source" form shall mean the preferred form for making modifications,
#    including but not limited to software source code, documentation
#    source, and configuration files.
#
#    "Object" form shall mean any form resulting from mechanical
#    transformation or translation of a Source form, including but
#    not limited to compiled object code, generated documentation,
#    and conversions to other media types.
#
#    "Work" shall mean the work of authorship, whether in Source or
#    Object form, made available under the License, as indicated by a
#    copyright notice that is included in or attached to the work
#    (an example is provided in the Appendix below).
#
#    "Derivative Works" shall mean any work, whether in Source or Object
#    form, that is based on (or derived from) the Work and for which the
#    editorial revisions, annotations, elaborations, or other modifications
#    represent, as a whole, an original work of authorship. For the purposes
#    of this License, Derivative Works shall not include works that remain
#    separable from, or merely link (or bind by name) to the interfaces of,
#    the Work and Derivative Works thereof.
#
#    "Contribution" shall mean any work of authorship, including
#    the original version of the Work and any modifications or additions
#    to that Work or Derivative Works thereof, that is intentionally
#    submitted to Licensor for inclusion in the Work by the copyright owner
#    or by an individual or Legal Entity authorized to submit on behalf of
#    the copyright owner. For the purposes of this definition, "submitted"
#    means any form of electronic, verbal, or written communication sent
#    to the Licensor or its representatives, including but not limited to
#    communication on electronic mailing lists, source code control systems,
#    and issue tracking systems that are managed by, or on behalf of, the
#    Licensor for the purpose of discussing and improving the Work, but
#    excluding communication that is conspicuously marked or otherwise
#    designated in writing by the copyright owner as "Not a Contribution."
#
#    "Contributor" shall mean Licensor and any individual or Legal Entity
#    on behalf of whom a Contribution has been received by Licensor and
#    subsequently incorporated within the Work.
#
# 2. Grant of Copyright License. Subject to the terms and conditions of
#    this License, each Contributor hereby grants to You a perpetual,
#    worldwide, non-exclusive, no-charge, royalty-free, irrevocable
#    copyright license to reproduce, prepare Derivative Works of,
#    publicly display, publicly perform, sublicense, and distribute the
#    Work and such Derivative Works in Source or Object form.
#
# 3. Grant of Patent License. Subject to the terms and conditions of
#    this License, each Contributor hereby grants to You a perpetual,
#    worldwide, non-exclusive, no-charge, royalty-free, irrevocable
#    (except as stated in this section) patent license to make, have made,
#    use, offer to sell, sell, import, and otherwise transfer the Work,
#    where such license applies only to those patent claims licensable
#    by such Contributor that are necessarily infringed by their
#    Contribution(s) alone or by combination of their Contribution(s)
#    with the Work to which such Contribution(s) was submitted. If You
#    institute patent litigation against any entity (including a
#    cross-claim or counterclaim in a lawsuit) alleging that the Work
#    or a Contribution incorporated within the Work constitutes direct
#    or contributory patent infringement, then any patent licenses
#    granted to You under this License for that Work shall terminate
#    as of the date such litigation is filed.
#
# 4. Redistribution. You may reproduce and distribute copies of the
#    Work or Derivative Works thereof in any medium, with or without
#    modifications, and in Source or Object form, provided that You
#    meet the following conditions:
#
#    (a) You must give any other recipients of the Work or
#        Derivative Works a copy of this License; and
#
#    (b) You must cause any modified files to carry prominent notices
#        stating that You changed the files; and
#
#    (c) You must retain, in the Source form of any Derivative Works
#        that You distribute, all copyright, patent, trademark, and
#        attribution notices from the Source form of the Work,
#        excluding those notices that do not pertain to any part of
#        the Derivative Works; and
#
#    (d) If the Work includes a "NOTICE" text file as part of its
#        distribution, then any Derivative Works that You distribute must
#        include a readable copy of the attribution notices contained
#        within such NOTICE file, excluding those notices that do not
#        pertain to any part of the Derivative Works, in at least one
#        of the following places: within a NOTICE text file distributed
#        as part of the Derivative Works; within the Source form or
#        documentation, if provided along with the Derivative Works; or,
#        within a display generated by the Derivative Works, if and
#        wherever such third-party notices normally appear. The contents
#        of the NOTICE file are for informational purposes only and
#        do not modify the License. You may add Your own attribution
#        notices within Derivative Works that You distribute, alongside
#        or as an addendum to the NOTICE text from the Work, provided
#        that such additional attribution notices cannot be construed
#        as modifying the License.
#
#    You may add Your own copyright statement to Your modifications and
#    may provide additional or different license terms and conditions
#    for use, reproduction, or distribution of Your modifications, or
#    for any such Derivative Works as a whole, provided Your use,
#    reproduction, and distribution of the Work otherwise complies with
#    the conditions stated in this License.
#
# 5. Submission of Contributions. Unless You explicitly state otherwise,
#    any Contribution intentionally submitted for inclusion in the Work
#    by You to the Licensor shall be under the terms and conditions of
#    this License, without any additional terms or conditions.
#    Notwithstanding the above, nothing herein shall supersede or modify
#    the terms of any separate license agreement you may have executed
#    with Licensor regarding such Contributions.
#
# 6. Trademarks. This License does not grant permission to use the trade
#    names, trademarks, service marks, or product names of the Licensor,
#    except as required for reasonable and customary use in describing the
#    origin of the Work and reproducing the content of the NOTICE file.
#
# 7. Disclaimer of Warranty. Unless required by applicable law or
#    agreed to in writing, Licensor provides the Work (and each
#    Contributor provides its Contributions) on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
#    implied, including, without limitation, any warranties or conditions
#    of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A
#    PARTICULAR PURPOSE. You are solely responsible for determining the
#    appropriateness of using or redistributing the Work and assume any
#    risks associated with Your exercise of permissions under this License.
#
# 8. Limitation of Liability. In no event and under no legal theory,
#    whether in tort (including negligence), contract, or otherwise,
#    unless required by applicable law (such as deliberate and grossly
#    negligent acts) or agreed to in writing, shall any Contributor be
#    liable to You for damages, including any direct, indirect, special,
#    incidental, or consequential damages of any character arising as a
#    result of this License or out of the use or inability to use the
#    Work (including but not limited to damages for loss of goodwill,
#    work stoppage, computer failure or malfunction, or any and all
#    other commercial damages or losses), even if such Contributor
#    has been advised of the possibility of such damages.
#
# 9. Accepting Warranty or Additional Liability. While redistributing
#    the Work or Derivative Works thereof, You may choose to offer,
#    and charge a fee for, acceptance of support, warranty, indemnity,
#    or other liability obligations and/or rights consistent with this
#    License. However, in accepting such obligations, You may act only
#    on Your own behalf and on Your sole responsibility, not on behalf
#    of any other Contributor, and only if You agree to indemnify,
#    defend, and hold each Contributor harmless for any liability
#    incurred by, or claims asserted against, such Contributor by reason
#    of your accepting any such warranty or additional liability.
#
# END OF TERMS AND CONDITIONS
#
# APPENDIX: How to apply the Apache License to your work.
#
#    To apply the Apache License to your work, attach the following
#    boilerplate notice, with the fields enclosed by brackets "[]"
#    replaced with your own identifying information. (Don't include
#    the brackets!)  The text should be enclosed in the appropriate
#    comment syntax for the file format. We also recommend that a
#    file or class name and description of purpose be included on the
#    same "printed page" as the copyright notice for easier
#    identification within third-party archives.
#
# Copyright [yyyy] [name of copyright owner]
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from __future__ import absolute_import
from octoprint.events import Events
from timeit import default_timer as timer

# import sys
import time
import math
import os
import subprocess

import octoprint.plugin
import re
import logging
import json
import flask

class BetterGrblSupportPlugin(octoprint.plugin.SettingsPlugin,
                              octoprint.plugin.SimpleApiPlugin,
                              octoprint.plugin.AssetPlugin,
                              octoprint.plugin.TemplatePlugin,
                              octoprint.plugin.StartupPlugin,
                              octoprint.plugin.EventHandlerPlugin,
                              octoprint.plugin.RestartNeedingPlugin):

    def __init__(self):
        self.hideTempTab = True
        self.hideControlTab = True
        self.hideGCodeTab = True
        self.customControls = False
        self.helloCommand = "$$"
        self.statusCommand = "?"
        self.dwellCommand = "G4 P0"
        self.positionCommand = "?"
        self.suppressM114 = True
        self.suppressM400 = True
        self.suppressM105 = True
        self.suppressM115 = True
        self.suppressM110 = True
        self.disablePolling = True
        self.disableModelSizeDetection = True
        self.neverSendChecksum = True
        self.reOrderTabs = True
        self.disablePrinterSafety = True
        self.zProbeOffset = 15.00
        self.weakLaserValue = 1
        self.framingPercentOfMaxSpeed = 25

        self.overrideM8 = False
        self.overrideM9 = False
        self.m8Command = ""
        self.m9Command = ""

        self.grblMode = None
        self.grblState = None
        self.grblX = float(0)
        self.grblY = float(0)
        self.grblZ = float(0)
        self.grblSpeed = 0
        self.grblPowerLevel = 0
        self.positioning = 0

        self.timeRef = 0

        self.grblErrors = {}
        self.grblAlarms = {}
        self.grblSettingsNames = {}
        self.grblSettings = {}
        self.grblSettingsText = ""

        self.ignoreErrors = False
        self.doSmoothie = False

        self.grblCmdQueue = []
        self.notifyQueue = []

        self.customControlsJson = r'[{"layout": "horizontal", "children": [{"commands": ["$10=0", "G28.1", "G92 X0 Y0 Z0"], "name": "Set Origin", "confirm": null}, {"command": "M999", "name": "Reset", "confirm": null}, {"commands": ["G1 F4000 S0", "M5", "$SLP"], "name": "Sleep", "confirm": null}, {"command": "$X", "name": "Unlock", "confirm": null}, {"commands": ["$32=0", "M4 S1"], "name": "Weak Laser", "confirm": null}, {"commands": ["$32=1", "M5"], "name": "Laser Off", "confirm": null}], "name": "Laser Commands"}, {"layout": "vertical", "type": "section", "children": [{"regex": "<([^,]+)[,|][WM]Pos:([+\\-\\d.]+,[+\\-\\d.]+,[+\\-\\d.]+)", "name": "State", "default": "", "template": "State: {0} - Position: {1}", "type": "feedback"}, {"regex": "F([\\d.]+) S([\\d.]+)", "name": "GCode State", "default": "", "template": "Speed: {0}  Power: {1}", "type": "feedback"}], "name": "Realtime State"}]'

        self.grblVersion = "unknown"

        # fail-safe for homing if origin has not been set
        self.originSet = False

        # load up our item/value pairs for errors, warnings, and settings
        self.loadGrblDescriptions()


    # #~~ SettingsPlugin mixin
    def get_settings_defaults(self):
        return dict(
            hideTempTab = True,
            hideControlTab = True,
            hideGCodeTab = True,
            hello = "$$",
            statusCommand = "?",
            dwellCommand = "G4 P0",
            positionCommand = "?",
            suppressM114 = True,
            suppressM400 = True,
            suppressM105 = True,
            suppressM115 = True,
            suppressM110 = True,
            disablePolling = True,
            customControls = True,
            frame_length = 100,
            frame_width = 100,
            frame_origin = None,
            distance = 10,
            distances = [.1, 1, 5, 10, 50, 100],
            is_printing = False,
            is_operational = False,
            disableModelSizeDetection = True,
            neverSendChecksum = True,
            reOrderTabs = True,
            disablePrinterSafety = True,
            grblSettingsText = None,
            grblSettingsBackup = "",
            zProbeOffset = 15.00,
            weakLaserValue = 1,
            framingPercentOfMaxSpeed = 25,
            overrideM8 = False,
            overrideM9 = False,
            m8Command = "/home/pi/bin/tplink_smartplug.py -t air-assist.shellware.com -c on",
            m9Command = "/home/pi/bin/tplink_smartplug.py -t air-assist.shellware.com -c off",
            ignoreErrors = False,
            doSmoothie = False,
            grblVersion = "unknown",
            laserMode = False
        )


    def on_after_startup(self):
        # establish initial state for printer status
        self._settings.set_boolean(["is_printing"], self._printer.is_printing())
        self._settings.set_boolean(["is_operational"], self._printer.is_operational())

        # initialize all of our settings
        self.hideTempTab = self._settings.get_boolean(["hideTempTab"])
        self.hideControlTab = self._settings.get_boolean(["hideControlTab"])
        self.hideGCodeTab = self._settings.get_boolean(["hideGCodeTab"])
        self.customControls = self._settings.get_boolean(["customControls"])

        self.helloCommand = self._settings.get(["hello"])
        self.statusCommand = self._settings.get(["statusCommand"])
        self.dwellCommand = self._settings.get(["dwellCommand"])
        self.positionCommand = self._settings.get(["positionCommand"])
        self.suppressM105 = self._settings.get_boolean(["suppressM105"])
        self.suppressM114 = self._settings.get_boolean(["suppressM114"])
        self.suppressM115 = self._settings.get_boolean(["suppressM115"])
        self.suppressM110 = self._settings.get_boolean(["suppressM110"])
        self.suppressM400 = self._settings.get_boolean(["suppressM400"])
        self.disablePolling = self._settings.get_boolean(["disablePolling"])

        self.disableModelSizeDetection = self._settings.get_boolean(["disableModelSizeDetection"])
        self.neverSendChecksum = self._settings.get_boolean(["neverSendChecksum"])
        self.reOrderTabs = self._settings.get_boolean(["reOrderTabs"])

        self.overrideM8 = self._settings.get_boolean(["overrideM8"])
        self.overrideM9 = self._settings.get_boolean(["overrideM9"])
        self.m8Command = self._settings.get(["m8Command"])
        self.m9Command = self._settings.get(["m9Command"])

        self.ignoreErrors = self._settings.get(["ignoreErrors"])
        self.doSmoothie = self._settings.get(["doSmoothie"])

        self.zProbeOffset = self._settings.get(["zProbeOffset"])
        self.weakLaserValue = self._settings.get(["weakLaserValue"])
        self.framingPercentOfMaxSpeed = self._settings.get(["framingPercentOfMaxSpeed"])

        self.grblSettingsText = self._settings.get(["grblSettingsText"])
        self.grblVersion = self._settings.get(["grblVersion"])

        # hardcoded global settings -- should revisit how I manage these
        self._settings.global_set_boolean(["feature", "modelSizeDetection"], not self.disableModelSizeDetection)
        self._settings.global_set_boolean(["serial", "neverSendChecksum"], self.neverSendChecksum)

        if self.neverSendChecksum:
            self._settings.global_set(["serial", "checksumRequiringCommands"], [])

        # load a map of disabled plugins
        disabledPlugins = self._settings.global_get(["plugins", "_disabled"])
        if disabledPlugins == None:
            disabledPlugins = []

        # disable the printer safety check plugin
        if self.disablePrinterSafety:
            if "printer_safety_check" not in disabledPlugins:
                disabledPlugins.append("printer_safety_check")
        else:
            if "printer_safety_check" in disabledPlugins:
                disabledPlugins.remove("printer_safety_check")

        # disable the gcodeviewer plugin
        if self.hideGCodeTab:
            if "gcodeviewer" not in disabledPlugins:
                disabledPlugins.append("gcodeviewer")
        else:
            if "gcodeviewer" in disabledPlugins:
                disabledPlugins.remove("gcodeviewer")

        self._settings.global_set(["plugins", "_disabled"], disabledPlugins)

        # process tabs marked as disabled
        disabledTabs = self._settings.global_get(["appearance", "components", "disabled", "tab"])
        if disabledTabs == None:
            disabledTabs = []

        if self.hideTempTab:
            if "temperature" not in disabledTabs:
                disabledTabs.append("temperature")
        else:
            if "temperature" in disabledTabs:
                disabledTabs.remove("temperature")

        if self.hideControlTab:
            if "control" not in disabledTabs:
                disabledTabs.append("control")
        else:
            if "control" in disabledTabs:
                disabledTabs.remove("control")

        self._settings.global_set(["appearance", "components", "disabled", "tab"], disabledTabs)

        if not self.hideControlTab:
            controls = self._settings.global_get(["controls"])

            if self.customControls and not controls:
                self._logger.debug("injecting custom controls")
                self._settings.global_set(["controls"], json.loads(self.customControlsJson))
            else:
                if not self.customControls and controls:
                    self._logger.debug("clearing custom controls")
                    self._settings.global_set(["controls"], [])

        orderedTabs = self._settings.global_get(["appearance", "components", "order", "tab"])

        # ensure i am always the first tab
        if self.reOrderTabs:
            orderedTabs = self._settings.global_get(["appearance", "components", "order", "tab"])

            if "plugin_bettergrblsupport" in orderedTabs:
                orderedTabs.remove("plugin_bettergrblsupport")

            orderedTabs.insert(0, "plugin_bettergrblsupport")
            self._settings.global_set(["appearance", "components", "order", "tab"], orderedTabs)

        self._settings.save()
        self.loadGrblSettings()


    def get_settings_version(self):
        return 3

    def on_settings_migrate(self, target, current):
        if current == None or current != target:
            orderedTabs = self._settings.global_get(["appearance", "components", "order", "tab"])
            if "gcodeviewer" in orderedTabs:
                orderedTabs.remove("gcodeviewer")
                self._settings.global_set(["appearance", "components", "order", "tab"], orderedTabs)

            disabledTabs = self._settings.global_get(["appearance", "components", "disabled", "tab"])

            if "gcodeviewer" in disabledTabs:
                disabledTabs.remove("gcodeviewer")

            if "plugin_gcodeviewer" in disabledTabs:
                disabledTabs.remove("plugin_gcodeviewer")

            if self._settings.get(["statusCommand"]) == "?$G":
                self._settings.set(["statusCommand"], "?")
                self.statusCommand = "?"

            self._settings.remove(["showZ"])

            self._settings.global_set(["appearance", "components", "disabled", "tab"], disabledTabs)
            self._settings.save()
            self._logger.info("Migrated to settings v%d from v%d", target, 1 if current == None else current)


    def loadGrblDescriptions(self):
        path = os.path.dirname(os.path.realpath(__file__)) + os.path.sep + "static" + os.path.sep + "txt" + os.path.sep

        f = open(path + "grbl_errors.txt", 'r')

        for line in f:
            match = re.search(r"^(-?[\d\.]+)[\ ]+(-?[\S\ ]*)", line)
            if not match is None:
                self.grblErrors[int(match.groups(1)[0])] = match.groups(1)[1]
                # self._logger.debug("matching error id: [%d] to description: [%s]", int(match.groups(1)[0]), match.groups(1)[1])

        f = open(path + "grbl_alarms.txt", 'r')

        for line in f:
            match = re.search(r"^(-?[\d\.]+)[\ ]+(-?[\S\ ]*)", line)
            if not match is None:
                self.grblAlarms[int(match.groups(1)[0])] = match.groups(1)[1]
                # self._logger.debug("matching alarm id: [%d] to description: [%s]", int(match.groups(1)[0]), match.groups(1)[1])

        f = open(path + "grbl_settings.txt", 'r')

        for line in f:
            match = re.search(r"^(-?[\d\.]+)[\ ]+(-?[\S\ ]*)", line)
            if not match is None:
                self.grblSettingsNames[int(match.groups(1)[0])] = match.groups(1)[1]
                # self._logger.debug("matching setting id: [%d] to description: [%s]", int(match.groups(1)[0]), match.groups(1)[1])


    def loadGrblSettings(self):
        self.grblSettingsText = self._settings.get(["grblSettingsText"])

        if not self.grblSettingsText is None:
            for setting in self.grblSettingsText.split("||"):
                if len(setting.strip()) > 0:

                    self._logger.debug("loadGrblSettings=[{}]".format(setting))

                    set = setting.split("|")
                    if not set is None:
                        self.grblSettings.update({int(set[0]): [set[1], self.grblSettingsNames.get(int(set[0]))]})
        return


    def saveGrblSettings(self):
        ret = ""
        for id, data in sorted(self.grblSettings.items(), key=lambda x: int(x[0])):
            ret = ret + "{}|{}|{}||".format(id, data[0], data[1])

        self._logger.debug("saveGrblSettings=[{}]".format(ret))

        self.grblSettingsText = ret
        return ret


    def on_settings_save(self, data):
        self._logger.debug("saving settings")
        octoprint.plugin.SettingsPlugin.on_settings_save(self, data)

        # reload our config
        self.on_after_startup()

        # refresh our grbl settings
        if self.doSmoothie:
            self._printer.commands("Cat /sd/config")
        else:
            self._printer.commands("$$")


    # #~~ AssetPlugin mixin
    def get_assets(self):
        # Define your plugin's asset files to automatically include in the
        # core UI here.
        return dict(js=['js/bettergrblsupport.js', 'js/bettergrblsupport_settings.js'],
                    css=['css/bettergrblsupport.css', 'css/bettergrblsupport_settings.css'],
                    less=['less/bettergrblsupport.less', "less/bettergrblsupport.less"])


    # #~~ TemplatePlugin mixin
    def get_template_configs(self):
        return [
            dict(type="settings", template="bettergrblsupport_settings.jinja2", custom_bindings=True)
        ]

    # def get_template_vars(self):
    #     return dict(grblSettingsText=self.saveGrblSettings())


    # #-- EventHandlerPlugin mix-in
    def on_event(self, event, payload):
        subscribed_events = (Events.FILE_SELECTED, Events.PRINT_STARTED, Events.PRINT_CANCELLED, Events.PRINT_CANCELLING,
                            Events.PRINT_PAUSED, Events.PRINT_RESUMED, Events.PRINT_DONE, Events.PRINT_FAILED,
                            Events.PLUGIN_PLUGINMANAGER_UNINSTALL_PLUGIN, Events.UPLOAD)

        if event not in subscribed_events:
            # self._logger.debug('event [{}] received but not subscribed - discarding'.format(event))
            return

        # our plugin is being uninstalled
        if event == Events.PLUGIN_PLUGINMANAGER_UNINSTALL_PLUGIN and payload["id"] == self._identifier:
            self._logger.debug('we are being uninstalled :(')
            self.cleanUpDueToUninstall()
            self._logger.debug('uninstall cleanup completed (this house is clean)')
            return

        # 'PrintStarted'
        if event == Events.PRINT_STARTED:
            if self.grblState != "Idle":
                # we have to stop This
                self._printer.cancel_print()
                return

            self.grblState = "Run"
            return

        # Print ended (finished / failed / cancelled)
        if event == Events.PRINT_CANCELLED or event == Events.PRINT_DONE or event == Events.PRINT_FAILED:
            self.grblState = "Idle"
            return

        # Print Cancelling
        if event == Events.PRINT_CANCELLING:
            self._logger.debug("canceling job")
            self._printer.commands("!", force=True)
            self.queue_cmds_and_send(["M999"], wait=True)
            self._printer.commands("G21 G90 G1 Z5 F100")

            if self.originSet:
                self._printer.commands("G28")

        # Print Paused
        if event == Events.PRINT_PAUSED:
            self._logger.debug("pausing job")
            self._printer.commands("!", force=True)

        # Print Resumed
        if event == Events.PRINT_RESUMED:
            self._logger.debug("resuming job")
            self._printer.commands("~", force=True)

        # File uploaded
        if event == Events.UPLOAD:
            if payload["path"].endswith(".gc") or payload["path"].endswith(".nc"):
                # uploaded_file = self._settings.global_get_basefolder("uploads") + '/' + payload["path"]
                # renamed_file = uploaded_file[:len(uploaded_file) - 2] + "gcode"
                renamed_file = payload["path"][:len(payload["path"]) - 2] + "gcode"

                self._logger.debug("renaming [%s] to [%s]", payload["path"], renamed_file)

                self._file_manager.remove_file(payload["target"], renamed_file)
                self._file_manager.move_file(payload["target"], payload["path"], renamed_file)
                # os.rename(uploaded_file, renamed_file)

        # 'FileSelected'
        if event == Events.FILE_SELECTED:
            selected_file = self._settings.global_get_basefolder("uploads") + '/' + payload['path']
            f = open(selected_file, 'r')

            minX = float("inf")
            minY = float("inf")
            maxX = float("-inf")
            maxY = float("-inf")

            x = float(0)
            y = float(0)

            self.positioning = 0

            start = timer()

            for line in f:
                #T2 # HACK:
                if line.upper().lstrip().startswith("X"):
                    match = re.search(r"^X *(-?[\d.]+).*", line)
                    if not match is None:
                        command = "G01 " + line.upper().strip()
                    else:
                        command = line.upper().strip()
                else:
                    command = line.upper().strip()

                if "G90" in command.upper():
                    # absolute positioning
                    self.positioning = 0
                    continue

                if "G91" in command.upper():
                    # relative positioning
                    self.positioning = 1
                    continue

                match = re.search(r"^G([0][0123]|[0123])(\D.*[Xx]|[Xx])\ *(-?[\d.]+).*", command)
                if not match is None:
                    if self.positioning == 1:
                        x = x + float(match.groups(1)[2])
                    else:
                        x = float(match.groups(1)[2])
                    if x < minX:
                        minX = x
                    if x > maxX:
                        maxX = x

                match = re.search(r"^G([0][0123]|[0123])(\D.*[Yy]|[Yy])\ *(-?[\d.]+).*", command)
                if not match is None:
                    if self.positioning == 1:
                        y = y + float(match.groups(1)[2])
                    else:
                        y = float(match.groups(1)[2])
                    if y < minY:
                        minY = y
                    if y > maxY:
                        maxY = y

            length = math.ceil(maxY - minY)
            width = math.ceil(maxX - minX)

            self._logger.debug('finished reading file length={} width={} time={}'.format(length, width, timer() - start))

            self._plugin_manager.send_plugin_message(self._identifier, dict(type="grbl_frame_size",
                                                                            length=length,
                                                                            width=width))
            return

        if event == Events.FILE_DESELECTED:
            return

        return


    def on_plugin_pending_uninstall(self):  # this will work in some next release of octoprint
        self._logger.debug('we are being uninstalled via on_plugin_pending_uninstall :(')
        self.cleanUpDueToUninstall()
        self._logger.debug('uninstall cleanup completed (this house is clean)')


    def cleanUpDueToUninstall(self):
        self._settings.global_set_boolean(["feature", "modelSizeDetection"], self.disableModelSizeDetection)
        self._settings.global_set_boolean(["serial", "neverSendChecksum"], not self.neverSendChecksum)

        # load a map of disabled plugins
        disabledPlugins = self._settings.global_get(["plugins", "_disabled"])
        if disabledPlugins == None:
            disabledPlugins = []

        # re-enable the printer safety check plugin
        if self.disablePrinterSafety:
            if "printer_safety_check" in disabledPlugins:
                disabledPlugins.remove("printer_safety_check")

        # re-enable the gcodeviewer plugin
        if self.hideGCodeTab:
            if "gcodeviewer" in disabledPlugins:
                disabledPlugins.remove("gcodeviewer")

        self._settings.global_set(["plugins", "_disabled"], disabledPlugins)

        disabledTabs = self._settings.global_get(["appearance", "components", "disabled", "tab"])
        if disabledTabs == None:
            disabledTabs = []

        if self.hideTempTab:
            if "temperature" in disabledTabs:
                disabledTabs.remove("temperature")

        if self.hideControlTab:
            if "control" in disabledTabs:
                disabledTabs.remove("control")

        # clean up old versions since octoprint renamed gcodeviewer to plugin_gcodeviewer
        if "gcodeviewer" in disabledTabs:
            disabledTabs.remove("gcodeviewer")

        # clean up old versions since we now disable gcodeviewer instead of just hiding it
        if "plugin_gcodeviewer" in disabledTabs:
            disabledTabs.remove("plugin_gcodeviewer")

        self._settings.global_set(["appearance", "components", "disabled", "tab"], disabledTabs)

        if not self.hideControlTab:
            controls = self._settings.global_get(["controls"])
            if self.customControls and controls:
                self._settings.global_set(["controls"], [])

        orderedTabs = self._settings.global_get(["appearance", "components", "order", "tab"])

        if "plugin_bettergrblsupport" in orderedTabs:
            orderedTabs.remove("plugin_bettergrblsupport")
            self._settings.global_set(["appearance", "components", "order", "tab"], orderedTabs)

        self._settings.save()

    def get_extension_tree(self, *args, **kwargs):
    		return dict(
    			model=dict(
    				grbl_gcode=["gc", "nc"]
    			)
    		)

    # #-- gcode sending hook
    def hook_gcode_sending(self, comm_instance, phase, cmd, cmd_type, gcode, *args, **kwargs):
        # suppress comments and extraneous commands that may cause wayward
        # grbl instances to error out
        if cmd.upper().lstrip().startswith(tuple([';', '(', '%'])):
            self._logger.debug('Ignoring extraneous [%s]', cmd)
            return (None, )

        # M8 processing - work in progress
        if cmd.upper().strip() == "M8" and self.overrideM8:
            self._logger.debug('Turning ON Air Assist')
            subprocess.call(self.m8Command, shell=True)
            return (None,)

        # M9 processing - work in progress
        if cmd.upper().strip() == "M9" and self.overrideM9:
            self._logger.debug('Turning OFF Air Assist')
            subprocess.call(self.m9Command, shell=True)
            return (None,)

        # rewrite M115 as $$ (hello)
        if self.suppressM115 and cmd.upper().startswith('M115'):
            self._logger.debug('Rewriting M115 as %s' % self.helloCommand)

            if self.doSmoothie:
                return "Cat /sd/config"

            return self.helloCommand

        # suppress reset line #s
        if self.suppressM110 and cmd.upper().startswith('M110'):
            self._logger.debug('Ignoring %s', cmd)
            return (None, )

        # suppress initialize SD - M21
        if cmd.upper().startswith('M21'):
            self._logger.debug('Ignoring %s', cmd)
            return (None,)

        # suppress temperature if printer is printing
        if cmd.upper().startswith('M105'):
            if self.disablePolling and self._printer.is_printing():
                self._logger.debug('Ignoring %s', cmd)
                return (None, )
            else:
                if self.suppressM105:
                    self._logger.debug('Rewriting M105 as %s' % self.statusCommand)
                    return (self.statusCommand, )

        # Wait for moves to finish before turning off the spindle
        if self.suppressM400 and cmd.upper().startswith('M400'):
            self._logger.debug('Rewriting M400 as %s' % self.dwellCommand)
            return (self.dwellCommand, )

        # rewrite current position
        if self.suppressM114 and cmd.upper().startswith('M114'):
            self._logger.debug('Rewriting M114 as %s' % self.positionCommand)
            return (self.positionCommand, )

        # soft reset / resume (stolen from Marlin)
        if cmd.upper().startswith('M999') and not self.doSmoothie:
            self._logger.debug('Sending Soft Reset')
            self.addToNotifyQueue(["Machine has been reset"])
            return ("\x18",)

        # ignore all of these -- they do not apply to GRBL
        # M108 (heater off) M84 (disable motors) M104 (set extruder temperature)
        # M140 (set bed temperature) M106 (fan on/off)
        if cmd.upper().startswith("M108") or cmd.upper().startswith("M84") or cmd.upper().startswith("M104") or cmd.upper().startswith("M140") or cmd.upper().startswith("M106"):
            self._logger.debug("ignoring [%s]", cmd)
            return (None, )

        if "G90" in cmd.upper():
            # absolute positioning
            self.positioning = 0

        if "G91" in cmd.upper():
            # relative positioning
            self.positioning = 1

        #T2 # HACK:
        if cmd.upper().lstrip().startswith("X"):
            match = re.search(r"^X *(-?[\d.]+).*", cmd)
            if not match is None:
                command = "G01 " + cmd.upper().strip()
            else:
                command = cmd.upper().strip()
        else:
            command = cmd.upper().strip()

        # keep track of distance traveled
        # if command.startswith("G0") or command.startswith("G1") or command.startswith("G2") or command.startswith("G3") or command.startswith("M4"):
        found = False

        match = re.search(r"^G([0][0123]|[0123])(\D.*[Xx]|[Xx])\ *(-?[\d.]+).*", command)
        if not match is None:
            if self.positioning == 1:
                self.grblX = self.grblX + float(match.groups(1)[2])
            else:
                self.grblX = float(match.groups(1)[2])
            found = True

        match = re.search(r"^G([0][0123]|[0123])(\D.*[Yy]|[Yy])\ *(-?[\d.]+).*", command)
        if not match is None:
            if self.positioning == 1:
                self.grblY = self.grblY + float(match.groups(1)[2])
            else:
                self.grblY = float(match.groups(1)[2])
            found = True

        match = re.search(r"^G([0][0123]|[0123])(\D.*[Zz]|[Zz])\ *(-?[\d.]+).*", command)
        if not match is None:
            if self.positioning == 1:
                self.grblZ = self.grblZ + float(match.groups(1)[2])
            else:
                self.grblZ = float(match.groups(1)[2])
            found = True

        match = re.search(r"^[GM]([0][01234]|[01234])(\D.*[Ff]|[Ff])\ *(-?[\d.]+).*", command)
        if not match is None:
            grblSpeed = round(float(match.groups(1)[2]))

            # make sure we post all speed on / off events
            if (grblSpeed == 0 and self.grblSpeed != 0) or (self.grblSpeed == 0 and grblSpeed != 0):
                self.timeRef = 0

            self.grblSpeed = grblSpeed
            found = True

        match = re.search(r"^[GM]([0][01234]|[01234])(\D.*[Ss]|[Ss])\ *(-?[\d.]+).*", command)
        if not match is None:
            grblPowerLevel = round(float(match.groups(1)[2]))

            # make sure we post all power on / off events
            # if (grblPowerLevel == 0 and self.grblPowerLevel != 0) or (self.grblPowerLevel == 0 and grblPowerLevel != 0):
            #     self.timeRef = 0;

            self.grblPowerLevel = grblPowerLevel
            found = True

        if found:
            currentTime = int(round(time.time() * 1000))
            if currentTime > self.timeRef + 500:
                # self._logger.info("x={} y={} z={} f={} s={}".format(self.grblX, self.grblY, self.grblZ, self.grblSpeed, self.grblPowerLevel))
                self._plugin_manager.send_plugin_message(self._identifier, dict(type="grbl_state",
                                                                                mode=self.grblMode,
                                                                                state=self.grblState,
                                                                                x=self.grblX,
                                                                                y=self.grblY,
                                                                                z=self.grblZ,
                                                                                speed=self.grblSpeed,
                                                                                power=self.grblPowerLevel))
                self.timeRef = currentTime

        return (command, )


    # #-- gcode received hook (
    # original author:  https://github.com/mic159
    # source: https://github.com/mic159/octoprint-grbl-plugin)
    def hook_gcode_received(self, comm_instance, line, *args, **kwargs):

        if line.startswith('Grbl'):
            # Hack to make Arduino based GRBL work.
            # When the serial port is opened, it resets and the "hello" command
            # is not processed.
            # This makes Octoprint recognise the startup message as a successful connection.
            self._settings.set(["grblVersion"], line)
            self._settings.save()

            # force an inquiry
            self._printer.commands("?")

            # self._plugin_manager.send_plugin_message(self._identifier, dict(type="send_notification", message=line))
            return 'ok ' + line

        # look for an alarm
        if line.lower().startswith('alarm:'):
            match = re.search(r'alarm:\ *(-?[\d.]+)', line.lower())

            error = int(0)

            if not match is None:
                error = int(match.groups(1)[0])
                self._plugin_manager.send_plugin_message(self._identifier, dict(type="grbl_alarm",
                                                                                code=error,
                                                                                description=self.grblAlarms.get(error)))

                self._logger.warning("alarm received: %d: %s", error, self.grblAlarms.get(error))

            # clear out any pending queued Commands
            if len(self.grblCmdQueue) > 0:
                self._logger.debug("clearing %d commands from the command queue", len(self.grblCmdQueue))
                self.grblCmdQueue.clear()

            # put a message on our notification queue and force an inquiry
            self.addToNotifyQueue([line if error == 0 else self.grblAlarms.get(error)])
            self._printer.commands("?")

            # we need to pause if we are printing
            if self._printer.is_printing():
                self._printer.pause_print()

            return 'Error: ' + line if error == 0 else self.grblAlarms.get(error)

        # look for an error
        if not self.ignoreErrors and line.lower().startswith('error:'):
            match = re.search(r'error:\ *(-?[\d.]+)', line.lower())

            error = int(0)
            desc = line

            if not match is None:
                error = int(match.groups(1)[0])
                desc = self.grblErrors.get(error)

            self._logger.warning("error received: %d: %s", error, desc)

            # clear out any pending queued Commands
            if len(self.grblCmdQueue) > 0:
                self._logger.debug("clearing %d commands from the command queue", len(self.grblCmdQueue))
                self.grblCmdQueue.clear()

            # put a message on our notification queue and force an inquiry
            self.addToNotifyQueue([desc])
            self._printer.commands("?")

            # lets not let octoprint know if we have a gcode lock error
            if error == 9:
                self._logger.debug("not forwarding grbl error 9 to octoprint")
                return "ok " + line
            else:
                self._plugin_manager.send_plugin_message(self._identifier, dict(type="grbl_error",
                                                                                code=error,
                                                                                description=desc))
            return 'Error: ' + desc

        # forward any messages to the notification plugin_name
        if "MSG:" in line.upper():
            ignoreList = ["[MSG:'$H'|'$X' to unlock]"]

            if line.strip() not in ignoreList:
                # auto reset
                if "reset to continue" in line.lower():
                    # automatically perform a soft reset if GRBL says we need one
                    self._printer.commands("M999")
                else:
                    self.addToNotifyQueue([line.replace("[","").replace("]","").replace("MSG:","")])

            return "ok " + line

        # grbl settings
        if line.startswith("$"):
            match = re.search(r'^[$](-?[\d\.]+)=(-?[\d\.]+)', line)

            if not match is None:
                settingsId = int(match.groups(1)[0])
                settingsValue = match.groups(1)[1]

                self.grblSettings.update({settingsId: [settingsValue, self.grblSettingsNames.get(settingsId)]})
                self._logger.debug("setting id={} value={} description={}".format(settingsId, settingsValue, self.grblSettingsNames.get(settingsId)))

                if settingsId >= 132:
                    self._settings.set(["grblSettingsText"], self.saveGrblSettings())
                    self._settings.set_boolean(["laserMode"], self.isLaserMode())
                    self._settings.save()

                    self.addToNotifyQueue(["Grbl Settings sent"])

                return line

        # hack to force status updates
        if 'MPos' in line or 'WPos' in line:
             # <Idle,MPos:0.000,0.000,0.000,WPos:0.000,0.000,0.000,RX:3,0/0>
             # <Run|MPos:-17.380,-7.270,0.000|FS:1626,0>

            # match = re.search(r'[WM]Pos:(-?[\d\.]+),(-?[\d\.]+),(-?[\d\.]+)', line)
            match = re.search(r'<(-?[^,]+)[,|][WM]Pos:(-?[\d\.]+),(-?[\d\.]+),(-?[\d\.]+)', line)

            if match is None:
                self._logger.warning('Bad data %s', line.rstrip())
                return line

             # OctoPrint records positions in some instances.
             # It needs a different format. Put both on the same line so the GRBL info is not lost
             # and is accessible for "controls" to read.
            response = 'ok X:{1} Y:{2} Z:{3} E:0 {original}'.format(*match.groups(), original=line)

            self.grblMode = "MPos" if "MPos" in line else "WPos" if "WPos" in line else "N/A"
            self.grblState = str(match.groups(1)[0])
            self.grblX = float(match.groups(1)[1])
            self.grblY = float(match.groups(1)[2])
            self.grblZ = float(match.groups(1)[3])

            self._logger.debug('status [%s]', response.strip())

            match = re.search(r'.*\|FS:(-?[\d\.]+),(-?[\d\.]+)', line)
            if not match is None:
                self.grblSpeed = round(float(match.groups(1)[0]))
                self.grblPowerLevel = round(float(match.groups(1)[1]))

            self._plugin_manager.send_plugin_message(self._identifier, dict(type="grbl_state",
                                                                            mode=self.grblMode,
                                                                            state=self.grblState,
                                                                            x=self.grblX,
                                                                            y=self.grblY,
                                                                            z=self.grblZ,
                                                                            speed=self.grblSpeed,
                                                                            power=self.grblPowerLevel))

            # pop any queued commands if state is IDLE or HOLD:0
            if len(self.grblCmdQueue) > 0 and (self.grblState.upper().strip() == "IDLE" or self.grblState.upper().strip() == "HOLD:0"):
                self._logger.debug('sending queued command [%s] - depth [%d]', self.grblCmdQueue[0], len(self.grblCmdQueue))
                self._printer.commands(self.grblCmdQueue[0])
                self.grblCmdQueue.pop(0)
                return response

            # add a notification if we just homed
            if self.grblState.upper().strip() == "HOME":
                self.addToNotifyQueue(["Machine has been homed"])

            # add a notification if we just z-probed
            if self.grblState.upper().strip() == "PRB":
                self.addToNotifyQueue(["Z-Probe run completed"])

            # pop any queued notifications
            if len(self.notifyQueue) > 0:
                notification = self.notifyQueue[0]
                self._logger.debug('sending queued notification [%s] - depth [%d]', notification, len(self.notifyQueue))
                self.notifyQueue.pop(0)
                return "//action:notification " + notification

            return response

        if not line.rstrip().endswith('ok'):
            return line

        if line.startswith('{'):
             # Regular ACKs
             # {0/0}ok
             # {5/16}ok
            return 'ok'
        elif '{' in line:
             # Ack with return data
             # F300S1000{0/0}ok
            (before, _, _) = line.partition('{')
            return 'ok ' + before
        else:
            return 'ok'


    def send_frame_init_gcode(self):
        f = int(float(self.grblSettings.get(110)[0]) * (float(self.framingPercentOfMaxSpeed) * .01))

        # Linear mode, feedrate f% of max, spindle off
        self._printer.commands("G1 F{} M5".format(f))

        # turn on laser in weak mode if laser mode enabled
        if self.isLaserMode():
            self._printer.commands("M3 S{}".format(self.weakLaserValue))


    def send_frame_end_gcode(self):
        self.queue_cmds_and_send(["M5 S0 G0"], wait=True)
        self.addToNotifyQueue(["Framing operation completed"])
        self._printer.commands("?")

    def send_bounding_box_upper_left(self, y, x):
        f = int(float(self.grblSettings.get(110)[0]) * (float(self.framingPercentOfMaxSpeed) * .01))

        self._printer.commands("{}G21 G91 X{:f} F{}".format("$J=" if self.isGrblOneDotOne() else "G1 ",x, f))
        self._printer.commands("{}G21 G91 Y{:f} F{}".format("$J=" if self.isGrblOneDotOne() else "G1 ", y * -1, f))
        self._printer.commands("{}G21 G91 X{:f} F{}".format("$J=" if self.isGrblOneDotOne() else "G1 ", x * -1, f))
        self._printer.commands("{}G21 G91 Y{:f} F{}".format("$J=" if self.isGrblOneDotOne() else "G1 ", y, f))


    def send_bounding_box_upper_center(self, y, x):
        f = int(float(self.grblSettings.get(110)[0]) * (float(self.framingPercentOfMaxSpeed) * .01))

        self._printer.commands("{}G21 G91 X{:f} F{}".format("$J=" if self.isGrblOneDotOne() else "G1 ", x / 2, f))
        self._printer.commands("{}G21 G91 Y{:f} F{}".format("$J=" if self.isGrblOneDotOne() else "G1 ", y * -1, f))
        self._printer.commands("{}G21 G91 X{:f} F{}".format("$J=" if self.isGrblOneDotOne() else "G1 ", x * -1, f))
        self._printer.commands("{}G21 G91 Y{:f} F{}".format("$J=" if self.isGrblOneDotOne() else "G1 ", y, f))
        self._printer.commands("{}G21 G91 X{:f} F{}".format("$J=" if self.isGrblOneDotOne() else "G1 ", x / 2, f))


    def send_bounding_box_upper_right(self, y, x):
        f = int(float(self.grblSettings.get(110)[0]) * (float(self.framingPercentOfMaxSpeed) * .01))

        self._printer.commands("{}G21 G91 Y{:f} F{}".format("$J=" if self.isGrblOneDotOne() else "G1 ", y * -1, f))
        self._printer.commands("{}G21 G91 X{:f} F{}".format("$J=" if self.isGrblOneDotOne() else "G1 ", x * -1, f))
        self._printer.commands("{}G21 G91 Y{:f} F{}".format("$J=" if self.isGrblOneDotOne() else "G1 ", y, f))
        self._printer.commands("{}G21 G91 X{:f} F{}".format("$J=" if self.isGrblOneDotOne() else "G1 ", x, f))


    def send_bounding_box_center_left(self, y, x):
        f = int(float(self.grblSettings.get(110)[0]) * (float(self.framingPercentOfMaxSpeed) * .01))

        self._printer.commands("{}G21 G91 Y{:f} F{}".format("$J=" if self.isGrblOneDotOne() else "G1 ", y / 2, f))
        self._printer.commands("{}G21 G91 X{:f} F{}".format("$J=" if self.isGrblOneDotOne() else "G1 ", x, f))
        self._printer.commands("{}G21 G91 Y{:f} F{}".format("$J=" if self.isGrblOneDotOne() else "G1 ", y * -1, f))
        self._printer.commands("{}G21 G91 X{:f} F{}".format("$J=" if self.isGrblOneDotOne() else "G1 ", x * -1, f))
        self._printer.commands("{}G21 G91 Y{:f} F{}".format("$J=" if self.isGrblOneDotOne() else "G1 ", y / 2, f))


    def send_bounding_box_center(self, y, x):
        f = int(float(self.grblSettings.get(110)[0]) * (float(self.framingPercentOfMaxSpeed) * .01))

        self._printer.commands("{}G21 G91 X{:f} Y{:f} F{}".format("$J=" if self.isGrblOneDotOne() else "G1 ", x / 2 * -1, y / 2, f))
        self._printer.commands("{}G21 G91 X{:f} F{}".format("$J=" if self.isGrblOneDotOne() else "G1 ", x, f))
        self._printer.commands("{}G21 G91 Y{:f} F{}".format("$J=" if self.isGrblOneDotOne() else "G1 ", y * -1, f))
        self._printer.commands("{}G21 G91 X{:f} F{}".format("$J=" if self.isGrblOneDotOne() else "G1 ", x * -1, f))
        self._printer.commands("{}G21 G91 Y{:f} F{}".format("$J=" if self.isGrblOneDotOne() else "G1 ", y, f))
        self._printer.commands("{}G21 G91 X{:f} Y{:f} F{}".format("$J=" if self.isGrblOneDotOne() else "G1 ", x / 2, y / 2 * -1, f))


    def send_bounding_box_center_right(self, y, x):
        f = int(float(self.grblSettings.get(110)[0]) * (float(self.framingPercentOfMaxSpeed) * .01))

        self._printer.commands("{}G21 G91 Y{:f} F{}".format("$J=" if self.isGrblOneDotOne() else "G1 ", y / 2 * -1, f))
        self._printer.commands("{}G21 G91 X{:f} F{}".format("$J=" if self.isGrblOneDotOne() else "G1 ", x * -1, f))
        self._printer.commands("{}G21 G91 Y{:f} F{}".format("$J=" if self.isGrblOneDotOne() else "G1 ", y, f))
        self._printer.commands("{}G21 G91 X{:f} F{}".format("$J=" if self.isGrblOneDotOne() else "G1 ", x, f))
        self._printer.commands("{}G21 G91 Y{:f} F{}".format("$J=" if self.isGrblOneDotOne() else "G1 ", y / 2 * -1, f))


    def send_bounding_box_lower_left(self, y, x):
        f = int(float(self.grblSettings.get(110)[0]) * (float(self.framingPercentOfMaxSpeed) * .01))

        self._printer.commands("{}G21 G91 Y{:f} F{}".format("$J=" if self.isGrblOneDotOne() else "G1 ", y, f))
        self._printer.commands("{}G21 G91 X{:f} F{}".format("$J=" if self.isGrblOneDotOne() else "G1 ", x, f))
        self._printer.commands("{}G21 G91 Y{:f} F{}".format("$J=" if self.isGrblOneDotOne() else "G1 ", y * -1, f))
        self._printer.commands("{}G21 G91 X{:f} F{}".format("$J=" if self.isGrblOneDotOne() else "G1 ", x * -1, f))


    def send_bounding_box_lower_center(self, y, x):
        f = int(float(self.grblSettings.get(110)[0]) * (float(self.framingPercentOfMaxSpeed) * .01))

        self._printer.commands("{}G21 G91 X{:f} F{}".format("$J=" if self.isGrblOneDotOne() else "G1 ", x / 2 * -1, f))
        self._printer.commands("{}G21 G91 Y{:f} F{}".format("$J=" if self.isGrblOneDotOne() else "G1 ", y, f))
        self._printer.commands("{}G21 G91 X{:f} F{}".format("$J=" if self.isGrblOneDotOne() else "G1 ", x, f))
        self._printer.commands("{}G21 G91 Y{:f} F{}".format("$J=" if self.isGrblOneDotOne() else "G1 ", y * -1, f))
        self._printer.commands("{}G21 G91 X{:f} F{}".format("$J=" if self.isGrblOneDotOne() else "G1 ", x / 2 * -1, f))


    def send_bounding_box_lower_right(self, y, x):
        f = int(float(self.grblSettings.get(110)[0]) * (float(self.framingPercentOfMaxSpeed) * .01))

        self._printer.commands("{}G21 G91 X{:f} F{}".format("$J=" if self.isGrblOneDotOne() else "G1 ", x * -1, f))
        self._printer.commands("{}G21 G91 Y{:f} F{}".format("$J=" if self.isGrblOneDotOne() else "G1 ", y, f))
        self._printer.commands("{}G21 G91 X{:f} F{}".format("$J=" if self.isGrblOneDotOne() else "G1 ", x, f))
        self._printer.commands("{}G21 G91 Y{:f} F{}".format("$J=" if self.isGrblOneDotOne() else "G1 ", y * -1, f))


    def get_api_commands(self):
        return dict(
            frame=[],
            toggleWeak=[],
            originz=[],
            origin=[],
            move=[],
            sleep=[],
            reset=[],
            unlock=[],
            homing=[],
            updateGrblSetting=[],
            backupGrblSettings=[],
            restoreGrblSettings=[]
        )


    def on_api_command(self, command, data):
        if command == "sleep":
            self._printer.commands("$SLP")
            return

        if command == "unlock":
            if self.doSmoothie:
                self._printer.commands("M999")
            else:
                self._printer.commands("$X")

            #fail-safe for ensuring we do not home
            self.originSet = False

            return

        if command == "reset":
            self._printer.commands("M999")
            return

        if command == "updateGrblSetting":
            self._printer.commands("${}={}".format(data.get("id").strip(), data.get("value").strip()))
            self.grblSettings.update({int(data.get("id")): [data.get("value").strip(), self.grblSettingsNames.get(int(data.get("id")))]})
            self._printer.commands("$$")
            return

        if command == "backupGrblSettings":
            self._settings.set(["grblSettingsBackup"], self.saveGrblSettings())
            self._settings.save()
            return

        if command == "restoreGrblSettings":
            settings = self._settings.get(["grblSettingsBackup"])

            if settings is None or len(settings.strip()) == 0:
                return

            for setting in settings.split("||"):
                if len(setting.strip()) > 0:
                    set = setting.split("|")
                    # self._logger.info("restoreGrblSettings: {}".format(set))
                    command = "${}={}".format(set[0], set[1])
                    self._printer.commands(command)

            time.sleep(1)
            return flask.jsonify({'res' : settings})

        if command == "homing" and self._printer.is_ready() and self.grblState in "Idle,Alarm":
            self._printer.commands("$H")
            self._plugin_manager.send_plugin_message(self._identifier, dict(type="grbl_state",
                                                                            mode="MPos",
                                                                            state="Home",
                                                                            x=0,
                                                                            y=0,
                                                                            z=0,
                                                                            speed="N/A",
                                                                            power="N/A"))
            return

        # catch-all (should revisit state management) for validating printer State
        if not self._printer.is_ready() or self.grblState != "Idle":
            self._logger.debug("ignoring move related command - printer is not available")
            return

        if command == "frame":
            origin = data.get("origin").strip()

            self.send_frame_init_gcode()

            if (origin == "grblTopLeft"):
                self.send_bounding_box_upper_left(float(data.get("length")), float(data.get("width")))

            if (origin == "grblTopCenter"):
                self.send_bounding_box_upper_center(float(data.get("length")), float(data.get("width")))

            if (origin == "grblTopRight"):
                self.send_bounding_box_upper_right(float(data.get("length")), float(data.get("width")))

            if (origin == "grblCenterLeft"):
                self.send_bounding_box_center_left(float(data.get("length")), float(data.get("width")))

            if (origin == "grblCenter"):
                self.send_bounding_box_center(float(data.get("length")), float(data.get("width")))

            if (origin == "grblCenterRight"):
                self.send_bounding_box_center_right(float(data.get("length")), float(data.get("width")))

            if (origin == "grblBottomLeft"):
                self.send_bounding_box_lower_left(float(data.get("length")), float(data.get("width")))

            if (origin == "grblBottomCenter"):
                self.send_bounding_box_lower_center(float(data.get("length")), float(data.get("width")))

            if (origin == "grblBottomRight"):
                self.send_bounding_box_lower_right(float(data.get("length")), float(data.get("width")))

            self.send_frame_end_gcode()

            self._settings.set(["frame_length"], data.get("length"))
            self._settings.set(["frame_width"], data.get("width"))
            self._settings.set(["frame_origin"], data.get("origin"))

            self._settings.save()

            self._logger.debug("frame submitted l={} w={} o={}".format(data.get("length"), data.get("width"), data.get("origin")))
            return

        if command == "move":
            # do move stuff
            direction = data.get("direction")
            distance = data.get("distance")

            if distance != self._settings.get(["distance"]):
                self._settings.set(["distance"], distance)
                self._settings.save()

            self._logger.debug("move direction={} distance={}".format(direction, distance))

            if direction == "home":
                self._printer.commands("G28")
                # add a notification if we just homed
                self.addToNotifyQueue(["Machine has been (work) homed"])

                self.originSet = True

            if direction == "probez":
                # probe z using offset
                self.queue_cmds_and_send(["G91 G21 G38.2 Z-50 F100 ?",
                                          "?",
                                          "G92 Z{}".format(self.zProbeOffset),
                                          "G0 Z5"])

            if direction == "forward":
                # max Y feed rate
                f = int(float(self.grblSettings.get(111)[0]))
                self._printer.commands("{}G91 G21 Y{:f} F{}".format("$J=" if self.isGrblOneDotOne() else "G1 ", distance, f))

            if direction == "backward":
                # max Y feed rate
                f = int(float(self.grblSettings.get(111)[0]))
                self._printer.commands("{}G91 G21 Y{:f} F{}".format("$J=" if self.isGrblOneDotOne() else "G1 ", distance * -1, f))

            if direction == "left":
                # max X feed rate
                f = int(float(self.grblSettings.get(110)[0]))
                self._printer.commands("{}G91 G21 X{:f} F{}".format("$J=" if self.isGrblOneDotOne() else "G1 ", distance * -1, f))

            if direction == "right":
                # max X feed rate
                f = int(float(self.grblSettings.get(110)[0]))
                self._printer.commands("{}G91 G21 X{:f} F{}".format("$J=" if self.isGrblOneDotOne() else "G1 ", distance, f))

            if direction == "up":
                # max Z feed rate
                f = int(float(self.grblSettings.get(112)[0]))
                self._printer.commands("{}G91 G21 Z{:f} F{}".format("$J=" if self.isGrblOneDotOne() else "G1 ", distance, f))

            if direction == "down":
                # max Z feed rate
                f = int(float(self.grblSettings.get(112)[0]))
                self._printer.commands("{}G91 G21 Z{:f} F{}".format("$J=" if self.isGrblOneDotOne() else "G1 ", distance * -1, f))

            return

        if command == "origin":
            self._printer.commands(["G28.1", "G10 P1 L20 X0 Y0 Z0", "G92 X0 Y0 Z0"])
            self.addToNotifyQueue(["Work origin set"])
            return

        # this command is deprecated
        if command == "originz":
            # technically this is unnecessary - may revisit the whole need for
            # for separating Z from X/Y when managing work plane home

            self._printer.commands("G28.1")
            # i really like this zeroing feature - may need to make it configurable
            self._printer.commands("G92 Z0")

            return

        if command == "toggleWeak":
            return flask.jsonify({'res' : self.toggleWeak()})


    def toggleWeak(self):
        # only execute if laser mode enabled
        if not self.isLaserMode():
            return

        f = int(float(self.grblSettings.get(110)[0]))

        if self.grblPowerLevel == 0:
            # turn on laser in weak mode
            self._printer.commands("G1 F{} M3 S{}".format(f, self.weakLaserValue))
            self.addToNotifyQueue(["Weak laser enabled"])
            res = "Laser Off"
        else:
            self._printer.commands(["M3 S0", "M5", "G0"])
            self.addToNotifyQueue(["Weak laser disabled"])
            res = "Weak Laser"

        return res


    def queue_cmds_and_send(self, cmds, wait=False):
        for cmd in cmds:
            self._logger.debug("queuing command [%s] wait=%r", cmd, wait)
            self.grblCmdQueue.append(cmd)

        if wait:
            self._logger.debug("waiting for command queue to drain")

            while len(self.grblCmdQueue) > 0:
                time.sleep(.001)

            self._logger.debug("done waiting for command queue to drain")

    def addToNotifyQueue(self, notifications):
        for notification in notifications:
            self._logger.debug("queuing notification [%s]", notification)
            self.notifyQueue.append(notification)


    def isLaserMode(self):
        return int(float(self.grblSettings.get(32)[0])) != 0


    def isGrblOneDotOne(self):
        return "1.1" in self.grblVersion


    # #~~ Softwareupdate hook
    def get_update_information(self):
        # Define the configuration for your plugin to use with the Software Update
        # Plugin here. See https://github.com/foosel/OctoPrint/wiki/Plugin:-Software-Update
        # for details.

        return dict(bettergrblsupport=dict(  # version check: github repository
                                             # update method: pip
            displayName='Better Grbl Support',
            displayVersion=self._plugin_version,
            type='github_release',
            user='synman',
            repo='OctoPrint-Bettergrblsupport',
            current=self._plugin_version,
            stable_branch={
                    "name": "Stable",
                    "branch": "master",
                    "commitish": ["master"],
                },
            prerelease_branches=[
                    {
                        "name": "Release Candidate",
                        "branch": "rc",
                        "commitish": ["rc", "master"],
                    },
                    {
                        "name": "Development",
                        "branch": "devel",
                        "commitish": ["devel", "rc", "master"],
                    }
                ],
            pip='https://github.com/synman/OctoPrint-Bettergrblsupport/archive/{target_version}.zip'))


# If you want your plugin to be registered within OctoPrint under a different name than what you defined in setup.py
# ("OctoPrint-PluginSkeleton"), you may define that here. Same goes for the other metadata derived from setup.py that
# can be overwritten via __plugin_xyz__ control properties. See the documentation for that.

__plugin_name__ = 'Better Grbl Support'
__plugin_pythoncompat__ = ">=2.7,<4"

def __plugin_load__():
    global __plugin_implementation__
    __plugin_implementation__ = BetterGrblSupportPlugin()

    global __plugin_hooks__
    __plugin_hooks__ = \
        {'octoprint.plugin.softwareupdate.check_config': __plugin_implementation__.get_update_information,
         'octoprint.comm.protocol.gcode.sending': __plugin_implementation__.hook_gcode_sending,
         'octoprint.comm.protocol.gcode.received': __plugin_implementation__.hook_gcode_received,
         "octoprint.filemanager.extension_tree": __plugin_implementation__.get_extension_tree}
