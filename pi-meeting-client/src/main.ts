import { invoke } from "@tauri-apps/api/core";

let greetInputEl: HTMLInputElement | null;
let greetMsgEl: HTMLElement | null;

async function greet() {
  if (greetMsgEl && greetInputEl) {
    // Learn more about Tauri commands at https://tauri.app/develop/calling-rust/
    greetMsgEl.textContent = await invoke("greet", {
      name: greetInputEl.value,
    });
  }
}

window.addEventListener("DOMContentLoaded", () => {
  greetInputEl = document.querySelector("#greet-input");
  greetMsgEl = document.querySelector("#greet-msg");
  document.querySelector("#greet-form")?.addEventListener("submit", (e) => {
    e.preventDefault();
    greet();
  });
});


const endpoint = "http://192.168.1.45:5000/status";

document.getElementById("btn1")?.addEventListener("click", () =>
  sendStatus({ droneOn: true, videoOn: false, inMeeting: false })
);

document.getElementById("btn2")?.addEventListener("click", () =>
  sendStatus({ droneOn: false, videoOn: true, inMeeting: false })
);

document.getElementById("btn3")?.addEventListener("click", () =>
  sendStatus({ droneOn: true, videoOn: true, inMeeting: true })
);

async function sendStatus(body: object) {
  try {
    const res = await fetch(endpoint, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(body),
    });

    if (!res.ok) {
      console.error("Failed:", res.statusText);
    } else {
      console.log("Success:", await res.text());
    }
  } catch (err) {
    console.error("Error:", err);
  }
}