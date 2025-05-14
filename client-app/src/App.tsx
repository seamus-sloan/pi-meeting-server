import { useState } from 'react';
import './App.css';
import '../../shared-ui/assets/fonts/Orbitron-VariableFont_wght.ttf';

function App() {
  const [inMeeting, setInMeeting] = useState(false);
  const [droneOn, setDroneOn] = useState(false);
  const [videoOn, setVideoOn] = useState(false);
  const [message, setMessage] = useState<string | null>('');

  const sendStatus = async (newState: {
    in_meeting: boolean,
    drone_on: boolean,
    video_on: boolean,
    message: string | null
  }) => {
    try {
      await fetch("http://192.168.1.45:5000/status", {
        method: "POST",
        headers: {
          "Content-Type": "text/plain",
        },
        body: JSON.stringify(newState)
      });
      console.log('Status sent:', newState);
    } catch (err) {
      console.error('Error sending status:', err);
    }
  };

  const updateAndSend = (
    updated: Partial<{ inMeeting: boolean; droneOn: boolean; videoOn: boolean; message: string | null }>
  ) => {
    const newState = {
      inMeeting: updated.inMeeting ?? inMeeting,
      droneOn: updated.droneOn ?? droneOn,
      videoOn: updated.videoOn ?? videoOn,
      message: updated.message ?? message,
    };

    setInMeeting(newState.inMeeting);
    setDroneOn(newState.droneOn);
    setVideoOn(newState.videoOn);
    setMessage(newState.message);

    sendStatus({
      in_meeting: newState.inMeeting,
      drone_on: newState.droneOn,
      video_on: newState.videoOn,
      message: newState.message === '' ? '' : newState.message || null,
    });
  };

  return (
    <div className={`status-screen ${inMeeting ? 'meeting' : 'available'}`}>
      <div className="status-center-content">
        <div className="status-title">Pi Meeting Controls</div>

        <div className="status-detail-row">
          <button className="toggle-button" onClick={() => updateAndSend({ inMeeting: !inMeeting })}>
            {inMeeting ? "🚫 IN MEETING" : "✅ AVAILABLE"}
          </button>
          <button className="toggle-button" onClick={() => updateAndSend({ droneOn: !droneOn })}>
            🛸 DRONE: {droneOn ? "ON" : "OFF"}
          </button>
          <button className="toggle-button" onClick={() => updateAndSend({ videoOn: !videoOn })}>
            📹 CAMERA: {videoOn ? "ON" : "OFF"}
          </button>
        </div>

        <input
          className="message-input"
          type="text"
          placeholder="Optional message"
          value={message ?? ''}
          onChange={(e) => updateAndSend({ message: e.target.value })}
        />
      </div>
    </div>
  );
}

export default App;
