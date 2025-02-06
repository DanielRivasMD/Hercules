////////////////////////////////////////////////////////////////////////////////////////////////////

// load dependencies
import puppeteer from "npm:puppeteer";
import { parse } from "https://deno.land/std@0.224.0/cli/parse.ts";
import { writeTextFile } from "https://deno.land/std@0.224.0/fs/mod.ts";

////////////////////////////////////////////////////////////////////////////////////////////////////

// parse command-line arguments
const args = parse(Deno.args);
const inputUrl = args.input || "https://no.wikipedia.org/wiki/Norge";
const outputFile = args.output || "output.txt";

////////////////////////////////////////////////////////////////////////////////////////////////////

const scrapeWikipedia = async () => {
  const browser = await puppeteer.launch({ headless: true });
  const page = await browser.newPage();

  try {
    // navigate URL
    await page.goto(inputUrl, { waitUntil: "domcontentloaded" });

    // extract content
    const content = await page.evaluate(() => {
      const paragraph = document.querySelector("#mw-content-text");
      return paragraph ? paragraph.innerText.trim() : "No content found.";
    });

    // write output
    await writeTextFile(outputFile, content);
    console.log(`Content saved to ${outputFile}`);
  } catch (error) {
    console.error("Error scraping Wikipedia:", error);
  } finally {
    await browser.close();
  }
};

////////////////////////////////////////////////////////////////////////////////////////////////////

// execute
scrapeWikipedia();

////////////////////////////////////////////////////////////////////////////////////////////////////
