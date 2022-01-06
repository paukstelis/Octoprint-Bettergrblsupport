/*
 * View model for OctoPrint-Bettergrblsupport
 *
 * Author: Shell M. Shrader
 * License: Apache 2.0
 */
$(function() {
    function BettergrblsupportViewModel(parameters) {
      var self = this;
      var fs = false;

      var $body = $('body');
      var framingPanel = $('#framing_panel');
      var controlPanel = $('#control_panel');
      var overridesPanel = $('#overrides_panel');
      var webcam_div = $('#webcam_div');
      var webcam_image_framing = $('#webcam_image_framing');

      var container;

      if($(".webcam_fixed_ratio").length > 0) {
        $container = $('.webcam_fixed_ratio');
        // $fullscreenContainer = $("#webcam_rotator");
      } else {
        $container = $('#webcam_rotator_framing');
        // $fullscreenContainer = $("#webcam_container");
      }

      // assign the injected parameters, e.g.:
      self.settings = parameters[0];
      self.loginState = parameters[1];

      self.length = ko.observable("100");
      self.width = ko.observable("100");

      self.origin_axes = ko.observableArray(["Z", "Y", "X", "XY", "ALL"]);
      self.origin_axis = ko.observable("XY");

      self.operator = ko.observable("=");
      self.distances = ko.observableArray([.1, 1, 5, 10, 50, 100]);
      self.distance = ko.observable(100);

      self.is_printing = ko.observable(false);
      self.is_operational = ko.observable(false);

      self.mode = ko.observable("N/A");
      self.state = ko.observable("N/A");
      self.xPos = ko.observable("N/A");
      self.yPos = ko.observable("N/A");
      self.zPos = ko.observable("N/A");
      self.power = ko.observable("N/A");
      self.speed = ko.observable("N/A");

      self.feedRate = ko.observable(undefined);
      self.plungeRate = ko.observable(undefined);
      self.powerRate = ko.observable(undefined);


      tab = document.getElementById("tab_plugin_bettergrblsupport_link");
      tab.innerHTML = tab.innerHTML.replace("Better Grbl Support", "Grbl Control");

      self.webcamFrameRatioClass = ko.pureComputed(function() {
          if (self.settings.webcam_streamRatio() == "4:3") {
              return "ratio43";
          } else {
              return "ratio169";
          }
      });

      self.doFrame = function() {
        var o;
        var x = document.getElementsByName("frameOrigin");
        var i;

        for (i = 0; i < x.length; i++) {
          if (x[i].checked) {
            o = x[i].id;
            break;
          }
        }

        $.ajax({
          url: API_BASEURL + "plugin/bettergrblsupport",
          type: "POST",
          dataType: "json",
          data: JSON.stringify({
            command: "frame",
            length: self.length(),
            width: self.width(),
            origin: o
          }),
          contentType: "application/json; charset=UTF-8",
          error: function (data, status) {
            new PNotify({
              title: "Framing failed!",
              text: data.responseText,
              hide: true,
              buttons: {
                sticker: false,
                closer: true
              },
              type: "error"
            });
          }
        });
      };

      self.toggleWeak = function() {
        $.ajax({
          url: API_BASEURL + "plugin/bettergrblsupport",
          type: "POST",
          dataType: "json",
          data: JSON.stringify({
            command: "toggleWeak"
          }),
          contentType: "application/json; charset=UTF-8",
          success: function(data) {
            var btn = document.getElementById("grblLaserButton");
            btn.innerHTML = btn.innerHTML.replace(btn.innerText, data["res"]);
          },
          error: function (data, status) {
            new PNotify({
              title: "Laser action failed!",
              text: data.responseText,
              hide: true,
              buttons: {
                sticker: false,
                closer: true
              },
              type: "error"
            });
          }
        });
      };

      self.distanceClicked = function(distance) {
        var operator;
        if (self.operator() == "+") {
          operator = 1;
        } else {
          if (self.operator() == "-") {
            operator = -1;
          } else {
            operator = 0;
          }
        }

        if (operator != 0) {
          self.distance(parseFloat(self.distance()) + (parseFloat(distance) * operator));
        } else {
          self.distance(parseFloat(distance));
        }
      };

      self.operatorClicked = function() {
        if (self.operator() == "+") {
          self.operator("-");
        } else {
          if (self.operator() == "-") {
            self.operator("=");
          } else {
            if (self.operator() == "=") {
              self.operator("+");
            }
          }
        }
      };

      self.moveHead = function(direction) {
        // if (direction == "probez") {
        //   OctoPrint.control.sendGcode("G91 G21 G38.2 F100 Z-50 ?");
        //   OctoPrint.control.sendGcode("G92 Z" + self.settings.settings.plugins.bettergrblsupport.zProbeOffset() + " G0 Z5");
        //
        //   return
        // }

        $.ajax({
          url: API_BASEURL + "plugin/bettergrblsupport",
          type: "POST",
          dataType: "json",
          data: JSON.stringify({
            command: "move",
            direction: direction,
            distance: self.distance(),
            axis: self.origin_axis()
          }),
          contentType: "application/json; charset=UTF-8",
          success: function(data) {
            if (data["res"] && data["res"].length > 0) {
              new PNotify({
                title: "Unable to Move!",
                text: data["res"],
                hide: true,
                buttons: {
                  sticker: false,
                  closer: true
                },
                type: "error"
              });
            }
          },
          error: function (data, status) {
            new PNotify({
              title: "Move Head failed!",
              text: data.responseText,
              hide: true,
              buttons: {
                sticker: false,
                closer: true
              },
              type: "error"
            });
          }
        });
      };

      self.sendCommand = function(command) {
        if (command == "unlock") {
          new PNotify({
                title: "Unlock Machine",
                text: "GRBL prefers you re-home your machine rather than unlock it.  Are you sure you want to unlock your machine?",
                type: "notice",
                hide: false,
                animation: "fade",
                animateSpeed: "slow",
                sticker: false,
                closer: true,
                confirm: {
                    confirm: true,
                    buttons: [
                        {
                            text: "CONFIRM",
                            click: function(notice) {
                                          $.ajax({
                                            url: API_BASEURL + "plugin/bettergrblsupport",
                                            type: "POST",
                                            dataType: "json",
                                            data: JSON.stringify({
                                              command: command
                                            }),
                                            contentType: "application/json; charset=UTF-8",
                                            error: function (data, status) {
                                              new PNotify({
                                                title: "Unable to unlock machine!",
                                                text: data.responseText,
                                                hide: true,
                                                buttons: {
                                                  sticker: false,
                                                  closer: true
                                                },
                                                type: "error"
                                              });
                                            }
                                          });
                                          notice.remove();
                            }
                        },
                        {
                            text: "CANCEL",
                            click: function(notice) {
                                notice.remove();
                            }
                        },
                    ]
                },
          });
          return;
        }

        $.ajax({
          url: API_BASEURL + "plugin/bettergrblsupport",
          type: "POST",
          dataType: "json",
          data: JSON.stringify({
            command: command,
            origin_axis: self.origin_axis(),
            feed_rate: self.feedRate(),
            plunge_rate: self.plungeRate(),
            power_rate: self.powerRate()
          }),
          contentType: "application/json; charset=UTF-8",
          success: function(data) {
            if (command == "feedRate") self.feedRate(undefined);
            if (command == "plungeRate") self.plungeRate(undefined);
            if (command == "powerRate") self.powerRate(undefined);
          },
          error: function (data, status) {
            new PNotify({
              title: "Unable to send command: " + command,
              text: data.responseText,
              hide: true,
              buttons: {
                sticker: false,
                closer: true
              },
              type: "error"
            });
          }
        });
      };

      self.onBeforeBinding = function() {
        self.length(self.settings.settings.plugins.bettergrblsupport.frame_length());
        self.width(self.settings.settings.plugins.bettergrblsupport.frame_width());

        self.distance(self.settings.settings.plugins.bettergrblsupport.distance());

        self.is_printing(self.settings.settings.plugins.bettergrblsupport.is_printing());
        self.is_operational(self.settings.settings.plugins.bettergrblsupport.is_operational());

        var x = document.getElementsByName("frameOrigin");

        var i;
        for (i = 0; i < x.length; i++) {
          if (x[i].id == self.settings.settings.plugins.bettergrblsupport.frame_origin()) {
            x[i].checked = true;
            break;
          }
        }

        if (self.settings.settings.webcam.webcamEnabled()) {
          document.getElementById("webcam_image_framing").src = self.settings.settings.webcam.streamUrl() + "&nonce=" + Math.floor(Math.random() * 1000000);
        }
      };

      self.onTabChange = function (current, previous) {
          if (self.settings.settings.webcam.webcamEnabled()) {
            if (current == "#tab_plugin_bettergrblsupport") {
                document.getElementById("webcam_image_framing").src = self.settings.settings.webcam.streamUrl() + "&nonce=" + Math.floor(Math.random() * 1000000);
            } else if (previous == "#tab_plugin_bettergrblsupport") {
                document.getElementById("webcam_image_framing").src = "about:blank";
            }
          }
      };

      self.fromCurrentData = function (data) {
          self._processStateData(data.state);
      };

      self.fromHistoryData = function (data) {
          self._processStateData(data.state);
      };

      self._processStateData = function (data) {
          self.is_printing(data.flags.printing);
          self.is_operational(data.flags.operational);
      };


      self.onDataUpdaterPluginMessage = function(plugin, data) {
        if (plugin == 'bettergrblsupport' && data.type == 'grbl_state') {
          if (data.mode != undefined) self.mode(data.mode);
          if (data.state != undefined) self.state(data.state);
          if (data.x != undefined) self.xPos(Number.parseFloat(data.x).toFixed(2));
          if (data.y != undefined) self.yPos(Number.parseFloat(data.y).toFixed(2));
          if (data.z != undefined) self.zPos(Number.parseFloat(data.z).toFixed(2));
          if (data.speed != undefined) self.speed(data.speed);

          if (data.state != "Run" && data.power != "N/A" && !self.is_printing()) {
            var btn = document.getElementById("grblLaserButton");

            if (btn != null) {
              if (data.power == "0" && self.power() != "0") {
                btn.innerHTML = btn.innerHTML.replace(btn.innerText, "Weak Laser");
              } else {
                if (self.power() == "0" && data.power != "0") {
                  btn.innerHTML = btn.innerHTML.replace(btn.innerText, "Laser Off");
                }
              }
            }
          }

          if (data.power != undefined) self.power(data.power);
          // console.log("mode=" + data.mode + " state=" + data.state + " x=" + data.x + " y=" + data.y + " z=" + data.z + " power=" + data.power + " speed=" + data.speed);
          return
        }

        if (plugin == 'bettergrblsupport' && data.type == 'grbl_frame_size') {
          width = Number.parseFloat(data.width).toFixed(0);
          length = Number.parseFloat(data.length).toFixed(0);

          self.width(width);
          self.length(length);

          new PNotify({
            title: "Frame Size Computed",
            text: "Dimensions are " + length + "L x " + width + "W",
            hide: true,
            animation: "fade",
            animateSpeed: "slow",
            mouseReset: true,
            delay: 10000,
            buttons: {
              sticker: true,
              closer: true
            },
            type: "success"
          });

          console.log("frame length=" + data.length + " width=" + data.width);
          return
        }

        if (plugin == 'bettergrblsupport' && data.type == 'simple_notify') {
          new PNotify({
            title: data.title,
            text: data.text,
            hide: data.hide,
            animation: "fade",
            animateSpeed: "slow",
            mouseReset: true,
            delay: data.delay,
            buttons: {
              sticker: true,
              closer: true
            },
            type: data.type,
          });
          return
        }

        if (plugin == 'bettergrblsupport' && data.type == 'restart_required') {
          new PNotify({
            title: "Restart Required",
            text: "Octoprint may need to be restarted for your changes to take full effect.",
            hide: false,
            animation: "fade",
            animateSpeed: "slow",
            mouseReset: true,
            buttons: {
              sticker: true,
              closer: true
            },
            type: "notice"
          });
          return
        }

        if (plugin == 'bettergrblsupport' && data.type == 'send_notification') {
          $.ajax({
            url: API_BASEURL + "plugin/action_command_notification",
            type: "POST",
            dataType: "json",
            data: JSON.stringify({
              command: "add",
              message: data.message
            }),
            contentType: "application/json; charset=UTF-8",
            error: function (data, status) {
              new PNotify({
                title: "Unable to add notification",
                text: data.responseText,
                hide: true,
                buttons: {
                  sticker: false,
                  closer: true
                },
                type: "error"
              });
            }
          });
        }

      };

      self.fsClick = function () {
        // console.log("fsClick");

        $body.toggleClass('inlineFullscreen');
        $container.toggleClass("inline fullscreen");
        // streamImg.classList.toggle("fullscreen");

        var progressBar = document.getElementById("state");

        if (progressBar.style.visibility == "" || progressBar.style.visibility == "visible") {
          progressBar.style.visibility = "hidden";
        } else {
          progressBar.style.visibility = "visible";
        }

        if (framingPanel.is(':visible')) {
          framingPanel.hide();
        } else {
          framingPanel.show();
        }

        if (controlPanel.is(':visible')) {
          controlPanel.hide();
        } else {
          controlPanel.show();
        }

        if (overridesPanel.is(':visible')) {
          overridesPanel.hide();
        } else {
          overridesPanel.show();
        }
      }

      self.onWebcamFrameErrored = function() {
        // alert("webcam frame error");
         webcam_div.hide();
         webcam_image_framing.src = self.settings.settings.webcam.streamUrl() + "&nonce=" + Math.floor(Math.random() * 1000000);
      }
      self.onWebcamFrameLoaded= function() {
        // alert("webcam frame error");
        webcam_div.show();
      }
    }

    self.feedRateResetter = ko.observable();
    self.resetFeedRateDisplay = function () {
        self.cancelFeedRateDisplayReset();
        self.feedRateResetter(
            setTimeout(function () {
                self.feedRate(undefined);
                self.feedRateResetter(undefined);
            }, 5000)
        );
    };
    self.cancelFeedRateDisplayReset = function () {
        var resetter = self.feedRateResetter();
        if (resetter) {
            clearTimeout(resetter);
            self.feedRateResetter(undefined);
        }
    };

    self.plungeRateResetter = ko.observable();
    self.resetPlungeRateDisplay = function () {
        self.cancelPlungeRateDisplayReset();
        self.plungeRateResetter(
            setTimeout(function () {
                self.plungeRate(undefined);
                self.plungeRateResetter(undefined);
            }, 5000)
        );
    };
    self.cancelPlungeRateDisplayReset = function () {
        var resetter = self.plungeRateResetter();
        if (resetter) {
            clearTimeout(resetter);
            self.plungeRateResetter(undefined);
        }
    };

    self.powerRateResetter = ko.observable();
    self.resetPowerRateDisplay = function () {
        self.cancelPowerRateDisplayReset();
        self.powerRateResetter(
            setTimeout(function () {
                self.powerRate(undefined);
                self.powerRateResetter(undefined);
            }, 5000)
        );
    };
    self.cancelPowerRateDisplayReset = function () {
        var resetter = self.powerRateResetter();
        if (resetter) {
            clearTimeout(resetter);
            self.powerRateResetter(undefined);
        }
    };
 

    // cute little hack for removing "Print" from the start button
    $('#job_print')[0].innerHTML = "<i class=\"fas\" data-bind=\"css: {'fa-print': !isPaused(), 'fa-undo': isPaused()}\"></i> <span data-bind=\"text: (isPaused() ? 'Restart' : 'Start')\">Start</span>"

    // cute hack for changing printer to machine for the action notify sidebar plugin
    var x = document.getElementById("sidebar_plugin_action_command_notification_wrapper");
    if (x != undefined) {
      x.firstElementChild.firstElementChild.innerText = x.firstElementChild.firstElementChild.innerText.replace("Printer", "Machine");
    }


    OCTOPRINT_VIEWMODELS.push([
      BettergrblsupportViewModel,
        [ "settingsViewModel", "loginStateViewModel" ],
        [ "#tab_plugin_bettergrblsupport" ]
      ]);
});
