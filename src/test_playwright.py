from playwright.async_api import async_playwright
import asyncio

async def main():
    async with async_playwright() as p:
        try:
            # Use Firefox instead of Chromium
            browser = await p.firefox.launch(
                headless=False,
                slow_mo=50  # Add small delays between operations
            )
            
            # Add small delay after browser launch
            await asyncio.sleep(1)
            
            context = await browser.new_context()
            page = await context.new_page()
            
            # Add timeout for navigation
            page.set_default_timeout(30000)  # 30 seconds
            
            # Navigate and wait until network is idle
            await page.goto("https://www.google.com", wait_until="networkidle")
            
            # Take screenshot
            await page.screenshot(path="example.png")
            
            # Proper cleanup
            await context.close()
            await browser.close()
            
        except Exception as e:
            print(f"Error occurred: {e}")
            
        finally:
            try:
                if 'context' in locals():
                    await context.close()
                if 'browser' in locals():
                    await browser.close()
            except Exception as e:
                print(f"Error during cleanup: {e}")

if __name__ == "__main__":
    asyncio.run(main())