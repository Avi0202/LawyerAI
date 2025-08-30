import React, { useState } from "react";
import { FiSend, FiMic } from "react-icons/fi";
import "./ChatBox.css";

const ChatBox = () => {
  const [message, setMessage] = useState("");

  const handleSend = () => {
    if (message.trim() === "") return;
    console.log("Sent:", message);
    setMessage("");
  };

  return (
    <div className="chatbox">
     
      <button className="icon-btn mic-btn">
        <FiMic />
      </button>

     
      <input
        type="text"
        className="chat-input"
        placeholder="Ask anything"
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        onKeyDown={(e) => e.key === "Enter" && handleSend()}
      />


      <button className="icon-btn send-btn" onClick={handleSend}>
        <FiSend />
      </button>
    </div>
  );
};

export default ChatBox;