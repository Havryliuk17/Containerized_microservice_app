from fastapi import FastAPI
import httpx, asyncio, os

app = FastAPI()

TARGET = os.getenv("TARGET_URL", "http://client:8000/health")

@app.on_event("startup")
async def poll_forever() -> None:
    async def loop():
        async with httpx.AsyncClient() as c:
            while True:
                try:
                    r = await c.get(TARGET, timeout=5)
                    print(f"[Scheduler] {r.status_code=} {r.text[:80]=}")
                except Exception as e:
                    print(f"[Scheduler] error: {e}")
                await asyncio.sleep(10)
    asyncio.create_task(loop())

@app.get("/")
def info():
    return {"msg": f"Scheduler is polling {TARGET} every 10 s"}
