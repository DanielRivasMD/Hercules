////////////////////////////////////////////////////////////////////////////////////////////////////

import { launch } from "jsr:@astral/astral";
import { parseArgs } from "jsr:@std/cli@1/parse-args";

////////////////////////////////////////////////////////////////////////////////////////////////////

// parse command-line arguments
const args = parseArgs(Deno.args, {
  string: ["input", "output"],
  alias: { i: "input", o: "output" },
  default: {
    input: "https://no.wikipedia.org/wiki/Norge",
    output: "output.txt",
  },
});

const inputUrl = args.input;
const outputFile = args.output;

////////////////////////////////////////////////////////////////////////////////////////////////////

const scrapeWikipedia = async () => {
  const browser = await launch({ headless: true });

  try {
    const page = await browser.newPage();

    // navigate to the URL
    await page.goto(inputUrl, { waitUntil: "domcontentloaded" });

    // extract content
    const content = await page.evaluate(() => {
      const paragraph = document.querySelector("#mw-content-text");
      return paragraph ? (paragraph as HTMLElement).innerText.trim() : "No content found.";
    });

    // write output — Deno builtin, no import needed
    await Deno.writeTextFile(outputFile, content);
    console.log(`Content saved to ${outputFile}`);
  } catch (error) {
    console.error("Error scraping Wikipedia:", error);
  } finally {
    await browser.close();
  }
};

////////////////////////////////////////////////////////////////////////////////////////////////////

// execute
await scrapeWikipedia();

////////////////////////////////////////////////////////////////////////////////////////////////////
