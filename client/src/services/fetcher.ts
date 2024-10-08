import { env } from "@env";

type Seconds = number;

export type CacheOpts = { revalidate: Seconds };

export async function fetchData<T>(
  endpoint: string,
  cache_opts: CacheOpts = { revalidate: 0 },
): Promise<T | null> {
  const API_BASE_URL = env.NEXT_PUBLIC_API_HOST;
  const cache_seconds = Math.max(
    cache_opts.revalidate,
    env.NEXT_PUBLIC_CACHE_FETCH_SECONDS,
  );
  cache_opts = { revalidate: cache_seconds };
  const res = await fetch(`${API_BASE_URL}/${endpoint}`, {
    next: cache_opts,
  });
  if (!res.ok) {
    return null;
  }
  const data: T = (await res.json()) as T;
  return data;
}
