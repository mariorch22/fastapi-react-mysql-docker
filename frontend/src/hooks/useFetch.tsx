import { useEffect, useState } from "react";
import axios, { AxiosError } from "axios";

interface FetchResponse<T> {
  data: T | null;
  error: AxiosError | null;
  loading: boolean;
}

export default function useFetch<T>(url: string): FetchResponse<T> {
  const [data, setData] = useState<T | null>(null);
  const [error, setError] = useState<AxiosError | null>(null);
  const [loading, setLoading] = useState<boolean>(true);

  useEffect(() => {
    (async function () {
      try {
        setLoading(true);
        const response = await axios.get<T>(url);
        setData(response.data);
      } catch (err) {
        setError(err as AxiosError);
      } finally {
        setLoading(false);
      }
    })();
  }, [url]);

  return { data, error, loading };
}