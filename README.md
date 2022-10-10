# Run template on GitHub Codespaces

## Prerequisites
Follow tutorial in : https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/creating-a-github-pages-site-with-jekyll

**GitHub Codespace defined in the repo has all tools installed***

## Theme Docs
The chosen theme is `minimal mistakes`. You can find documentation in https://mmistakes.github.io/minimal-mistakes/docs/configuration/ 

## Structure

- Main page : index.md
- Exams list page: _pages/Exams.md
- Individual exam pages: _exams/*.md
- Navigations: _data/navigation.yml


## Debug and live changes

- Open a terminal on codespaces and build the site and make it available on a local server.

    ```bundle install``` **(Only once)**


    ```bundle exec jekyll serve --livereload```

- On terminal **Ports**  make port 4000 **Public**. Changes made to markdown files will be reloaded **live** (not supported for Gemfile or _config.yml files)

## Emoticons
Taken from https://github.com/caiyongji/emoji-list

## Application Insights

/workspaces/ESI_Resources/_includes/head/custom.html change connection string.

## Certification icons
**FOR TEASER/GRID** Taken from credly profiles as they all have 600x600 format. Example: https://www.credly.com/users/unai-huete/badges
IMPORTANT TODO --> Images should be modifief to be wider for the grid container, define SIZE AND SOURCE!
**FOR EXAM PAGE** taken from specific exam pages such as: https://docs.microsoft.com/en-us/learn/certifications/exams/dp-100 and **Copy image link**