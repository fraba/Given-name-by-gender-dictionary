Compile dictionary of given names with gender attribution
=============

The script will parse Wiktionary categories [Male_given_names_by_language](http://en.wiktionary.org/wiki/Category:Male_given_names_by_language) and [Female_given_names_by_language] (http://en.wiktionary.org/wiki/Category:Female_given_names_by_language) down to all subcategories and store all names it will found categorised in the pages in a comma-separated values text file in the form

```
Andries,male
Johan,male
Jonnie,male
```

Note: The script is set to download a page every 20-30 seconds and it is my assumption that it complies with [Wiktionary's directives](http://en.wiktionary.org/robots.txt) for web-agents. (If you think it does not please let me know). In any case, a copy of the given name dictionary is also in the repository, so you don't really need to reparse it. . 
