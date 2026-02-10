export const fetchInsights = async () => {
  const res = await fetch("/api/ml-insights");

  if (!res.ok) {
    throw new Error("Failed to fetch ML insights");
  }

  return res.json();
};
