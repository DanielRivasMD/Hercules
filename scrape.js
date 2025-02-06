////////////////////////////////////////////////////////////////////////////////////////////////////

import puppeteer from "puppeteer";
import fs from "fs";

////////////////////////////////////////////////////////////////////////////////////////////////////

const scrapeWikipedia = async () => {
  const url = "https://no.wikipedia.org/wiki/Norge";

  // launch a browser instance
  const browser = await puppeteer.launch({ headless: true });
  const page = await browser.newPage();

  try {
    // navigate to address
    await page.goto(url, { waitUntil: "domcontentloaded" });

    // extract content
    const content = await page.evaluate(() => {
      const paragraph = document.querySelector("#mw-content-text");
      return paragraph ? paragraph.innerText.trim() : "No content found.";
    });

    fs.writeFileSync("norsk.txt", JSON.stringify(content, null, 2));
  } catch (error) {
    console.error("Error scraping Wikipedia:", error);
  } finally {
    await browser.close();
  }
};

////////////////////////////////////////////////////////////////////////////////////////////////////

scrapeWikipedia();

////////////////////////////////////////////////////////////////////////////////////////////////////
