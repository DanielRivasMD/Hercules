/*
Copyright © 2023 danielrivasmd@gmail.com

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
*/
package cmd

////////////////////////////////////////////////////////////////////////////////////////////////////

import (
	"fmt"
	"strconv"
	"strings"

	"github.com/gocolly/colly"
	"github.com/spf13/cobra"
)

////////////////////////////////////////////////////////////////////////////////////////////////////

// default
var perPage = 10

// arguments
var (
	address         string
	authorFirstName string
	authorLastName  string
	noArticles      string
)

// declarations
var (
	pages      string
	articles   []article
	TmpArticle article
	Authors    string
	Journal    string
)

type article struct {
	authors string
	journal string
}

////////////////////////////////////////////////////////////////////////////////////////////////////

// pubmedCmd represents the pubmed command
var pubmedCmd = &cobra.Command{
	Use:   "pubmed",
	Short: "A brief description of your command",
	Long: `A longer description that spans multiple lines and likely contains examples
and usage of using your command. For example:

Cobra is a CLI library for Go that empowers applications.
This application is a tool to generate the needed files
to quickly create a Cobra application.`,

	////////////////////////////////////////////////////////////////////////////////////////////////////

	Run: func(cmd *cobra.Command, args []string) {
		// noArt := pager(address, authorFirstName, authorLastName)

		// cast
		noArt, _ := strconv.Atoi(noArticles)

		// scrap data
		scrap(address, authorFirstName, authorLastName, noArt)
	},
}

////////////////////////////////////////////////////////////////////////////////////////////////////

func scrap(url, authorFirstName, authorLastName string) {
// func pager(url, authorFirstName, authorLastName string) int {

	// c := colly.NewCollector(
	// // colly.AllowedDomains(url),
	// )
// 	var noArt int

	// c.OnRequest(func(r *colly.Request) {
	// 	// r.Headers.Set("User-Agent", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/118.0")
	// 	fmt.Println("Visiting", r.URL)
	// })
// 	c := colly.NewCollector(
// 	// colly.AllowedDomains(url),
// 	)

	// c.OnResponse(func(r *colly.Response) {
	// 	fmt.Println("Response Code", r.StatusCode)
	// })
// 	// collect article number
// 	c.OnHTML("h3", func(h *colly.HTMLElement) {
// 		h.ForEach("span", func(_ int, h *colly.HTMLElement) {
// 			// fmt.Println(h.Text)
// 			noArt, _ = strconv.Atoi(h.Text)
// 		})
// 	})

	// c.OnError(func(r *colly.Response, err error) {
	// 	fmt.Println("error", err.Error())
	// })
// 	searchUrl := url + "?term=" + authorLastName + "+" + authorFirstName + "[" + "author" + "]"
// 	c.Visit(searchUrl)

	// // collect article number
	// c.OnHTML("h3", func(h *colly.HTMLElement) {
	// 	h.ForEach("span", func(_ int, h *colly.HTMLElement) {
	// 		// fmt.Println(h.Text)
	// 		noArticles, _ = strconv.Atoi(h.Text)
	// 	})
	// })
// 	return noArt

	// searchUrl := url + "?term=" + authorLastName + "+" + authorFirstName + "[" + "author" + "]"
	// c.Visit(searchUrl)
// }

	pgs := 4

	for i := 1; i <= pgs; i++ {
		// fmt.Println("iteration", i)

		sc := colly.NewCollector(
		// colly.AllowedDomains(url),
		)

		sc.OnHTML("span.full-authors", func(h *colly.HTMLElement) {
			Authors = h.Text
			Authors = strings.ReplaceAll(Authors, ", ", ",")
			Authors = strings.ReplaceAll(Authors, "; ", ",")
			for _, a := range strings.Split(Authors, ",") {
				fmt.Println(a)
			}
		})

		// sc.OnHTML("span.short-journal-citation", func(h *colly.HTMLElement) {
		// 	Journal = h.Text
		// 	fmt.Println(Journal)
		// })

		// TmpArticle = article{
		// 	authors: Authors,
		// 	journal: Journal,
		// }

		// fmt.Println("Tmp Article", TmpArticle)

		// articles := append(articles, TmpArticle)

		// page := noArticles / perPage
		// fmt.Println(page, noArticles, perPage)
		// modulus := noArticles % perPage
		// if modulus == 0 {
		// 	pages = strconv.Itoa(page)
		// } else {
		// 	pages = strconv.Itoa(page + 1)
		// }

		// hardcoded
		pages = strconv.Itoa(i)

		// fmt.Println(pages)
		fullUrl := url + "?term=" + authorLastName + "+" + authorFirstName + "[" + "author" + "]" + "&page=" + pages
		sc.Visit(fullUrl)

	}
	// fmt.Println(articles)
	// fmt.Println(noArticles)

}

////////////////////////////////////////////////////////////////////////////////////////////////////

func init() {
	rootCmd.AddCommand(pubmedCmd)

	// persistent flags
	pubmedCmd.PersistentFlags().StringVarP(&address, "address", "a", "https://pubmed.ncbi.nlm.nih.gov/", "Website address")
	pubmedCmd.PersistentFlags().StringVarP(&authorFirstName, "first", "f", "", "Author first name")
	pubmedCmd.PersistentFlags().StringVarP(&authorLastName, "last", "l", "", "Author last name")
	pubmedCmd.PersistentFlags().StringVarP(&noArticles, "number", "n", "", "Number of articles")

}

////////////////////////////////////////////////////////////////////////////////////////////////////
