/** @odoo-module **/

import { browser } from "@web/core/browser/browser";
import { session } from "@web/session";
import { registry } from "@web/core/registry";

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
            const h = Math.floor(sec / 3600);
            const m = Math.floor((sec % 3600) / 60);
            const s = sec % 60;
            return `${h}h ${m}m ${s}s`;
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

registry.category("services").add("sessionTimerService", sessionTimerService);
