import { useEffect, useState } from 'react'
import './App.css'

function App() {
  const [wines, setWines] = useState([]);

  const fetchWines = async () => {
    try {
      const winesPath = 'api/list';
      const response = await fetch('http://127.0.0.1:8000/' + winesPath);
      const data = await response.json();
      setWines(data);

      if (!response.ok) {
        throw new Error('Network response was not ok');
      }

    } catch (error) {
      console.error('Error:', error);
    }
  }

  useEffect(() => {
    fetchWines();
  }, []);

  return (
    <>
      <div>Liste des vins</div>
      {wines.map((wine: any) => (
        <div key={wine.id}>{wine.name} - {wine.year} ({wine.appellation})</div>
      ))}
    </>
  );
}

export default App
