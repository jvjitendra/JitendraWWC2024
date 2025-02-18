import { useEffect, useState } from 'react';

function App() {
  const [threats, setThreats] = useState([]);

  useEffect(() => {
    fetch('http://localhost:5000/threats')
      .then(res => res.json())
      .then(data => setThreats(data));
  }, []);

  return (
    <div>
      <h2>Threat Assessment</h2>
      {threats.map((t, i) => (
        <p key={i}>{t.name} - Severity: {t.severity}</p>
      ))}
    </div>
  );
}

export default App;
