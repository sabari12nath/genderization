"use client";

import { useEffect, useState } from "react";

const API = process.env.NEXT_PUBLIC_API_URL ?? "http://127.0.0.1:8000";

export default function GenderDetector() {
  const [file, setFile] = useState<File | null>(null);
  const [preview, setPreview] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [result, setResult] = useState<{ label: string; confidence: number } | null>(null);

  // Create & clean up preview URL whenever file changes
  useEffect(() => {
    if (!file) { setPreview(null); return; }
    const url = URL.createObjectURL(file);
    setPreview(url);
    return () => URL.revokeObjectURL(url);
  }, [file]);

  const analyze = async () => {
    if (!file) return;
    setLoading(true);
    setError(null);
    setResult(null);

    const fd = new FormData();
    fd.append("file", file);

    try {
      const res = await fetch(`${API}/analyze/`, { method: "POST", body: fd });
      const text = await res.text();
      if (!res.ok) throw new Error(`HTTP ${res.status}: ${text}`);
      const data = JSON.parse(text) as { gender: string };
      setResult({ label: data.gender, confidence: 1 });
    } catch (e: any) {
      setError(e?.message || "Failed to fetch");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="p-6 bg-white rounded-xl shadow-md max-w-md w-full">
      <h2 className="text-xl font-bold mb-4 text-black">Gender Detector</h2>

      <label className="block border-2 border-dashed p-4 text-center rounded-lg cursor-pointer text-black">
        <input
          type="file"
          accept="image/*"
          className="hidden"
          onChange={(e) => setFile(e.target.files?.[0] ?? null)}
        />
        {file ? "Change photo" : "Upload a photo"}
      </label>

      {/* 👇 Preview goes here */}
      <div className="mt-4">
        {preview ? (
          <img
            src={preview}
            alt="Preview"
            className="w-full max-h-64 object-contain rounded-lg border"
          />
        ) : (
          <div className="h-40 flex items-center justify-center rounded-lg border text-gray-500">
            No image selected
          </div>
        )}
      </div>

      {file && (
        <div className="mt-4 flex items-center gap-4">
          <button
            onClick={analyze}
            disabled={loading}
            className="px-4 py-2 bg-blue-600 text-white rounded disabled:opacity-50"
          >
            {loading ? "Analyzing…" : "Analyze"}
          </button>
        </div>
      )}

      {error && <p className="text-red-600 text-sm mt-2">{error}</p>}

      {result && (
        <div className="mt-4 p-3 bg-gray-50 rounded text-black">
          Prediction: <b>{result.label}</b>
        </div>
      )}
    </div>
  );
}
