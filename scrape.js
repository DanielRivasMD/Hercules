////////////////////////////////////////////////////////////////////////////////////////////////////

import puppeteer from "puppeteer";
import yargs from "yargs";
import fs from "fs";

////////////////////////////////////////////////////////////////////////////////////////////////////

const argv = yargs(process.argv.slice(2))
  .option("input", {
    alias: "i",
    type: "string",
    description: "input address",
  })
  .option("output", {
    alias: "o",
    type: "string",
    description: "output file",
  })
  .help().argv;

////////////////////////////////////////////////////////////////////////////////////////////////////

const scrapeWikipedia = async () => {
  const url = argv.input;

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

    fs.writeFileSync(argv.output, content, "utf8");
  } catch (error) {
    console.error("Error scraping Wikipedia:", error);
  } finally {
    await browser.close();
  }
};

////////////////////////////////////////////////////////////////////////////////////////////////////

scrapeWikipedia();

////////////////////////////////////////////////////////////////////////////////////////////////////
