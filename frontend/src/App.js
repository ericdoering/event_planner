import "./App.css";
import React, { useState } from "react";
import axios from "axios";
import ReactMarkDown from "react-markdown"

function App() {
  const [eventType, setEventType] = useState("");
  const [guests, setGuests] = useState("");
  const [budget, setBudget] = useState("");
  const [plan, setPlan] = useState("");
  const [loading, setLoading] = useState(false)

  const handleSubmit = async() => {
    if(!eventType || !guests || !budget){
      alert("Please fill out all fields.")
      return 
    }
    setLoading(true)
    setPlan("")

    try{
      const response = await axios.post(
        "http://127.0.0.1:5000/plan_event", 
        {
          event_type: eventType,
          guests,
          budget
        }
      )
      setPlan(response.data.plan);
    }
    catch{
      alert("Something went wrong.")
    }
    finally{
      setLoading(false)
    }
  }

  return (
    <div className="App">
      <h1>AI Event Party Planner</h1>
      <input type="text" placeholder="Wedding" value={eventType} onChange={(e) => setEventType(e.target.value)} />
      <input type="number" placeholder="Number of Guests" value={guests} onChange={(e) => setGuests(e.target.value)} />
      <input type="number" placeholder="Budget in USD" value={budget} onChange={(e) => setBudget(e.target.value)} />
      <button onClick={handleSubmit} disabled={loading}>
          {loading ? "Planning..." : "Generate Plan"}
      </button>

      {plan && (
        <div>
          <h2>Your AI Generated Plan</h2>
          <ReactMarkDown>{plan}</ReactMarkDown>
        </div>
      )}
      
    </div>
  );
}

export default App;
