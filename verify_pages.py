import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        # Verify index.html
        await page.goto('file:///app/index.html')
        await page.screenshot(path='/home/jules/verification/index_screenshot.png', full_page=True)
        print("Screenshot of index.html saved to /home/jules/verification/index_screenshot.png")

        await browser.close()

if __name__ == '__main__':
    asyncio.run(main())
