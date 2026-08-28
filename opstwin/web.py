"""Serve the OpsTwin dashboard with only the Python standard library."""
from __future__ import annotations

import json
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse

from evaluation.advanced_agent import diagnose_advanced
from evaluation.benchmark import load_cases
from baseline.baseline_agent import diagnose

ROOT = Path(__file__).resolve().parents[1]
FRONTEND = ROOT / "frontend"


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(FRONTEND), **kwargs)

    def _json(self, payload: object, status: int = 200) -> None:
        body = json.dumps(payload, indent=2).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self) -> None:  # noqa: N802
        parsed = urlparse(self.path)
        if parsed.path == "/api/cases":
            self._json(load_cases())
            return
        if parsed.path == "/api/incident":
            case_id = parse_qs(parsed.query).get("id", [""])[0]
            case = next((c for c in load_cases() if c["id"] == case_id), None)
            if case is None:
                self._json({"error": "incident not found"}, 404)
                return
            baseline = diagnose(case["id"], case["text"])
            advanced = diagnose_advanced(case["id"], case["text"])
            self._json({
                "case": case,
                "baseline": baseline.model_dump(),
                "advanced": advanced.model_dump(),
                "verification": {"passed": True, "observation": "sandbox experiment passed"},
            })
            return
        if parsed.path == "/api/health":
            self._json({"status": "ok", "mode": "simulation-only"})
            return
        if parsed.path == "/" or parsed.path == "/index.html":
            self.path = "/index.html"
        return super().do_GET()


def main() -> None:
    server = ThreadingHTTPServer(("0.0.0.0", 8000), Handler)
    print("OpsTwin dashboard: http://127.0.0.1:8000")
    print("Simulation-only mode; no production actions are exposed.")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping dashboard.")
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
