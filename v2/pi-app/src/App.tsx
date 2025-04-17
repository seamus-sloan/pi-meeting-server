import { useEffect, useState } from "react";
import { listen } from "@tauri-apps/api/event";
import '../../shared-ui/assets/fonts/Orbitron-VariableFont_wght.ttf';

import "./App.css";

type Status = {
  in_meeting: boolean;
  drone_on: boolean;
  video_on: boolean;
  message?: string | null;
};

export default function App() {
  const [status, setStatus] = useState<Status | null>(null);

  // Fetch initial status
  useEffect(() => {
    fetch("http://localhost:5000/status")
      .then((res) => res.json())
      .then(setStatus)
      .catch((err) => console.error("Failed to fetch status", err));
  }, []);

  // Subscribe to updates
  useEffect(() => {
    const unlisten = listen<Status>("status_changed", (event) => {
      setStatus(event.payload);
    });

    return () => {
      unlisten.then((off) => off());
    };
  }, []);

  if (!status) {
    return <div className="status-screen">Loading status...</div>;
  }

  return (
    <div className={`status-screen ${status.in_meeting ? "meeting" : "available"}`}>
      <div className="status-center-content">
        <div className="status-title">
          {status.in_meeting ? "In Meeting" : "Available"}
        </div>


      { status.message && (
          <div className="status-message">
            {status.message}
          </div>
        )}
  
        <div className="status-detail-row">
          <div className="status-detail">
            🛸 Drone:{" "} 
            <span className={`status-value ${status.drone_on ? "on" : ""}`}>
              {status.drone_on ? "ON" : "OFF"}
            </span>
          </div>
          <div className="divider" />
          <div className="status-detail">
            📹 Video:{" "}
            <span className={`status-value ${status.video_on ? "on" : ""}`}>
              {status.video_on ? "ON" : "OFF"}
            </span>
          </div>
        </div>
      </div>
    </div>
  );
}
