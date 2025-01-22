import { baseURL } from '@/utils/constants';
import useFetch from '@/hooks/useFetch';
import '@/App.css'

interface MessageData {
  message: string;
}

function App() {
  const { data, loading, error } = useFetch<MessageData>(`${baseURL}`);

  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error.message}</div>;

  return (
    <>
      <div>
        <h1>Today's Weather</h1>
        <p>Message from backend: {data?.message}</p>
      </div>
    </>
  )
}

export default App
