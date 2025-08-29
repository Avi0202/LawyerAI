import React, { useState } from "react";
import "./Sidebar.css";
const Sidebar = () => {

  const [isOpen, setIsOpen] = useState(false);
  const toggleSidebar = () => {
    setIsOpen(!isOpen);
  };
  return (
    <div className={`sidebar ${isOpen?"open":""}`}>
      <button className="collapse-btn" onClick={toggleSidebar}>
        {isOpen?">>":"<<"}</button>
      
    </div>
  );
};

export default Sidebar;