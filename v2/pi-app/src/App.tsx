import { useEffect, useState } from "react";
import { listen } from "@tauri-apps/api/event";

type Status = {
  inMeeting: boolean;
  droneOn: boolean;
  videoOn: boolean;
};

export default function App() {
  const [status, setStatus] = useState<Status | null>(null);

  // 🅰️ Pull initial status once
  useEffect(() => {
    fetch("http://localhost:5000/status")
      .then((res) => res.json())
      .then((data) => {
        console.log("✅ Got status from backend:", data);
        setStatus(data);
      })
      .catch((err) => {
        console.error("❌ Failed to fetch status:", err);
      });
  }, []);
  

  // 🅱️ Subscribe to updates
  useEffect(() => {
    const unlisten = listen<Status>("status_changed", (event) => {
      setStatus(event.payload);
    });

    return () => {
      unlisten.then((off) => off());
    };
  }, []);

  return (
    <div style={{ fontSize: "2rem", textAlign: "center", paddingTop: "20vh" }}>
      {status ? (
        <pre>{JSON.stringify(status, null, 2)}</pre>
      ) : (
        <p>Waiting for status...</p>
      )}
    </div>
  );
}
