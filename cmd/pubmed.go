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

	"github.com/gocolly/colly"
	"github.com/spf13/cobra"
)

////////////////////////////////////////////////////////////////////////////////////////////////////

// declarations
var (
	pubmed = "https://pubmed.ncbi.nlm.nih.gov/"
	jstore = "https://www.j2store.net/demo/index.php/shop"
	// authorFirstName = "SD"
	// authorLastName  = "Rivas-Carrillo"
	authorFirstName = "Evan"
	authorLastName  = "Mauceli"
	perPage         = 10
)

var (
	pages      string
	articles   []article
	noArticles int
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
		// fmt.Println("pubmed called")
		scrap(pubmed, authorFirstName, authorLastName)
		// scrap(jstore)
		// fmt.Println("scrapped!")
	},
}

////////////////////////////////////////////////////////////////////////////////////////////////////

func scrap(url, authorFirstName, authorLastName string) {

	// c := colly.NewCollector(
	// // colly.AllowedDomains(url),
	// )

	// c.OnRequest(func(r *colly.Request) {
	// 	// r.Headers.Set("User-Agent", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/118.0")
	// 	fmt.Println("Visiting", r.URL)
	// })

	// c.OnResponse(func(r *colly.Response) {
	// 	fmt.Println("Response Code", r.StatusCode)
	// })

	// c.OnError(func(r *colly.Response, err error) {
	// 	fmt.Println("error", err.Error())
	// })

	// // collect article number
	// c.OnHTML("h3", func(h *colly.HTMLElement) {
	// 	h.ForEach("span", func(_ int, h *colly.HTMLElement) {
	// 		// fmt.Println(h.Text)
	// 		noArticles, _ = strconv.Atoi(h.Text)
	// 	})
	// })

	// searchUrl := url + "?term=" + authorLastName + "+" + authorFirstName + "[" + "author" + "]"
	// c.Visit(searchUrl)

	pgs := 4

	for i := 1; i <= pgs; i++ {
		// fmt.Println("iteration", i)

		sc := colly.NewCollector(
		// colly.AllowedDomains(url),
		)

		sc.OnHTML("span.full-authors", func(h *colly.HTMLElement) {
			Authors = h.Text
			fmt.Println(Authors)
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

	// Here you will define your flags and configuration settings.

	// Cobra supports Persistent Flags which will work for this command
	// and all subcommands, e.g.:
	// pubmedCmd.PersistentFlags().String("foo", "", "A help for foo")

	// Cobra supports local flags which will only run when this command
	// is called directly, e.g.:
	// pubmedCmd.Flags().BoolP("toggle", "t", false, "Help message for toggle")
}

////////////////////////////////////////////////////////////////////////////////////////////////////
