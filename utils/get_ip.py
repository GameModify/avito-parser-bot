from aiohttp_socks import ProxyConnector
import aiohttp

async def get_ip_via_proxy(proxy_url: str) -> str:
    connector = ProxyConnector.from_url(proxy_url)
    try:
        async with aiohttp.ClientSession(connector=connector) as session:
            async with session.get("https://ipwhois.app/json/") as resp:
                data = await resp.json()
                print(f"🌐 Ваш IP: {data.get('ip')}")
                return data.get("ip")
    except Exception as e:
        print(f"❌ Ошибка при проверке IP: {e}")
        return f"ERROR: {e}"

async def get_ip_via_proxy_direct() -> str:
    import aiohttp
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get("https://ipwhois.app/json/") as resp:
                data = await resp.json()
                print(f"🌐 Ваш IP напрямую: {data.get('ip')}")
                return data.get("ip")
    except Exception as e:
        print(f"❌ Ошибка при проверке IP напрямую: {e}")
        return f"ERROR: {e}"