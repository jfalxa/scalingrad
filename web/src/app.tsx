import { useEffect, useState } from "react";

const App = () => {
  const [loading, setLoading] = useState(false);
  const [data, setData] = useState<{ message: string } | undefined>(undefined);

  useEffect(() => {
    async function fetchData() {
      setLoading(true);

      const res = await fetch("/api/");
      const data = await res.json();

      setData(data);
      setLoading(false);
    }

    fetchData();
  }, []);

  if (loading) return <i>Loading...</i>;

  return <code className="app">{JSON.stringify(data, undefined, "  ")}</code>;
};

export default App;
