import { NextRequest, NextResponse } from "next/server";

const API = process.env.NEXT_PUBLIC_API_URL ?? "http://127.0.0.1:8000";

export async function POST(req: NextRequest) {
  try {
    const form = await req.formData();
    const file = form.get("file");
    if (!(file instanceof Blob)) {
      return NextResponse.json({ error: "No file provided" }, { status: 400 });
    }

    // forward as multipart to FastAPI
    const fwd = new FormData();
    fwd.append("file", file, (file as any).name ?? "upload.jpg");

    const r = await fetch(`${API}/predict`, { method: "POST", body: fwd });
    const text = await r.text();
    if (!r.ok) {
      return NextResponse.json({ error: text || "Upstream error" }, { status: r.status });
    }
    return new NextResponse(text, { status: 200, headers: { "content-type": "application/json" } });
  } catch (e: any) {
    return NextResponse.json({ error: e?.message || "Proxy failed" }, { status: 500 });
  }
}
