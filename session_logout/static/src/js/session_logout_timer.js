/** @odoo-module **/

import { browser } from "@web/core/browser/browser";
import { session } from "@web/session";
import { registry } from "@web/core/registry";
import { patch } from "@web/core/utils/patch";
import { FormController } from "@web/views/form/form_controller";

const sessionTimerService = {
    start() {
        const enabled = session.timer_enable;
        const minutes = session.timer_set_time || 0;

        const el = document.getElementById("session_timer_display");

        if (!enabled || minutes <= 0) {
            if (el) {
                el.style.display = "none";
            }
            return;
        }

        let secondsLeft = minutes * 60;

        let intervalId = null;

        function formatTime(sec) {
            const d = Math.floor(sec / (3600 * 24));
            const h = Math.floor(sec / 3600);
            const m = Math.floor((sec % 3600) / 60);
            const s = sec % 60;
            if(d>0){
              return `${d}d ${h}h ${m}m ${s}s`;
              }
            else{
            return `${h}h ${m}m ${s}s`;
            }
        }

        function updateUI() {
            const displayEl = document.getElementById("session_timer_display");
            if (displayEl) {
                displayEl.innerText = "Session: " + formatTime(secondsLeft);
            }
        }

        function resetTimer() {
            secondsLeft = minutes * 60;
            updateUI();
        }

        function startTimer() {
            if (intervalId) return;

            updateUI();
            intervalId = setInterval(() => {
                secondsLeft--;
                updateUI();

                if (secondsLeft <= 0) {
                    clearInterval(intervalId);
                    browser.location.href = "/web/session/logout";
                }
            }, 1000);
        }

        ["mousemove", "keydown", "click", "scroll"].forEach(event => {
            window.addEventListener(event, resetTimer);
        });

        startTimer();
    },
};

const reloadService = {
    dependencies: ["bus_service"],
    start(env, { bus_service }) {

        bus_service.subscribe("reload_page", (loading) => {
            if (loading.refresh) {
                console.log("Timer settings changed. Reloading...");
                browser.location.reload();
            }
        });
    },
};
registry.category("services").add("reloadService", reloadService)
registry.category("services").add("sessionTimerService", sessionTimerService);
