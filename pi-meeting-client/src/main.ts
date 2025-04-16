type Status = {
  inMeeting: boolean;
  droneOn: boolean;
  videoOn: boolean;
};

const endpoint = "http://192.168.1.45:5000/status";

const toggles = {
  inMeeting: document.getElementById("toggle-inMeeting") as HTMLInputElement,
  droneOn: document.getElementById("toggle-droneOn") as HTMLInputElement,
  videoOn: document.getElementById("toggle-videoOn") as HTMLInputElement,
};

Object.entries(toggles).forEach(([key, input]) => {
  input.addEventListener("change", () => {
    const newStatus: Status = {
      inMeeting: toggles.inMeeting.checked,
      droneOn: toggles.droneOn.checked,
      videoOn: toggles.videoOn.checked,
    };
    sendStatus(newStatus);
  });
});

async function sendStatus(status: Status) {
  try {
    await fetch(endpoint, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(status),
    });
  } catch (err) {
    showToast("Error sending status");
    console.error("POST error:", err);
  }
}

async function pollStatus() {
  try {
    const res = await fetch(endpoint);
    const data: Status = await res.json();
    updateUI(data);
  } catch (err) {
    console.error("GET error:", err);
  }
}

function updateBodyBackground(inMeeting: boolean) {
  document.body.classList.remove("meeting-true", "meeting-false");
  document.body.classList.add(`meeting-${inMeeting}`);
}

function updateUI(status: Status) {
  toggles.inMeeting.checked = status.inMeeting;
  toggles.droneOn.checked = status.droneOn;
  toggles.videoOn.checked = status.videoOn;
  updateBodyBackground(status.inMeeting);
}

function showToast(message: string) {
  const toast = document.createElement("div");
  toast.className = "toast";
  toast.textContent = message;

  const container = document.getElementById("toast-container");
  container?.appendChild(toast);

  // Remove the toast after the animation ends (3.6s total)
  setTimeout(() => {
    toast.remove();
  }, 3600);
}

setInterval(pollStatus, 2000);
pollStatus();
