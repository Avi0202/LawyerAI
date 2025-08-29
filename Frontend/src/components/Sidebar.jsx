import React, { useState } from "react";
import {FiChevronLeft, FiChevronRight} from "react-icons/fi"
import "./Sidebar.css";
const Sidebar = () => {

  const [isOpen, setIsOpen] = useState(false);
  const toggleSidebar = () => {
    setIsOpen(!isOpen);
  };
  return (
    <div className={`sidebar ${isOpen?"open":""}`}>
      <button className="collapse-btn" onClick={toggleSidebar}>
        {isOpen?<FiChevronRight/>:<FiChevronLeft/>}</button>
      
    </div>
  );
};

export default Sidebar;