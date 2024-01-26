import { Loader2 } from "lucide-react";
import React from "react";
import Auth from "../models/auth";

function HomePage() {
  const [count, setCount] = React.useState<number>(0);
  const [loading, setLoading] = React.useState<boolean>(false);
  const [auth, setAuth] = React.useState<Auth | null>(null);

  React.useEffect(() => {
    // Call the backend api to get data
    // set the data to state
    setLoading(true);
    getData();
  }, [count]);

  function handleCount() {
    setCount(count + 1);
  }

  async function getData() {
    try {
      // Make api request to backend
      const response = await fetch("http://localhost:8080/api");
      // setAuth(response.data);
    } catch (error: any) {
      console.error(error.message);
    } finally {
      setLoading(false);
    }
  }

  if (loading) {
    return (
      <div className="fixed flex items-center justify-center z-30 inset-0 backdrop-blur-md">
        <Loader2 size={50} className={"animate-spin"} />
      </div>
    );
  }

  return (
    <div className="flex flex-col items-center justify-center h-[70vh] max-w-screen-lg w-11/12 mx-auto">
      <h1>Home page</h1>
      <div className="flex items-center gap-10">
        <button
          onClick={handleCount}
          className="px-5 py-4 rounded-md bg-slate-900 text-white"
        >
          Count up!
        </button>
        {count}
      </div>
    </div>
  );
}

export default HomePage;
