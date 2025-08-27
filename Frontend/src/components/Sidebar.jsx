import React, { useState } from "react";

const Sidebar = ({ 
  conversations = [], 
  onSelectConversation = () => {}, 
  onNewConversation = () => {} 
}) => {
  const [collapsed, setCollapsed] = useState(false);

  const toggleSidebar = () => {
    setCollapsed((prev) => !prev);
  };

  return (
    <div className={`sidebar ${collapsed ? "collapsed" : ""}`}>
      {/* Top bar: App name + toggle */}
      <div className="sidebar-header">
        <div className="app-name">
          <h2>{collapsed ? "R" : "My RAG App"}</h2>
        </div>
        <button onClick={toggleSidebar} className="toggle-btn">
          {collapsed ? "→" : "←"}
        </button>
      </div>

      {/* New chat button (hidden if collapsed) */}
      {!collapsed && (
        <button onClick={onNewConversation}>+ New Chat</button>
      )}

      {/* Conversations */}
      <ul className="conversations-list">
        {!collapsed && conversations.length > 0 ? (
          conversations.map((conv, index) => (
            <li key={conv.id || index}>
              <button onClick={() => onSelectConversation(conv.id)}>
                {conv.title || `Conversation ${index + 1}`}
              </button>
            </li>
          ))
        ) : !collapsed && (
          <li>
            <span>No previous conversations</span>
          </li>
        )}
      </ul>
    </div>
  );
};

export default Sidebar;