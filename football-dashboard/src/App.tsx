import { useState, useEffect } from 'react'
import './App.css'

function App() {
  const [data, setData] = useState(null);

  useEffect(() => {
    // This fetches the node.js API
    fetch('http://localhost:5000/api/predict')
    .then(res => res.json())
    .then(json => setData(json));
  }, []);

  return (
    <>
    <div style={{ padding: '40px', fontFamily: 'sans-serif' }}>
      <h1>Football Oracle Dashboard</h1>
      <hr />
      {data ? (
        <div style={{ background: '#f4f4f4', padding: '20px', borderRadius: '10px' }}>
          <h2>Next Match: {data.match}</h2>
          <p><strong>Oracle Prediction:</strong> {data.prediction}</p>
          <small>Generated at: {data.timestamp}</small>
        </div>
      ) : (
        <p>Consulting the Oracle...</p>
      )}
    </div>
    </>
  )
}

export default App
