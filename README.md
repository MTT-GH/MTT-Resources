# ESI Resources

In this short readme you will find all the information and processes needed to maintain this repository.

# How to run the template on GitHub Codespaces

## Prerequisites
To find out how to start setting up github pages follow the tutorial here : https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/creating-a-github-pages-site-with-jekyll

**The GitHub Codespace defined in the repo has all the necessary tools already installed**

## Theme Docs
The chosen theme is `minimal mistakes`. You can find documentation and configuration options https://mmistakes.github.io/minimal-mistakes/docs/configuration/. The theme has been updated to reflect the latest Learn branding.

## Structure

The portal structure is divided in the following 4 pages/ page types.

- Main page : index.md
- Exams list page: _pages/Exams.md
- Individual exam pages: _exams/*.md
- Navigations: _data/navigation.yml

### Main Page

In the main page you will find all information regarding exam preparation. This page represents all the links, videos and material outlined in the closing session of the course.

### Exam list Page

This is a list of all exam pages. 

### Individual Exam Pages

Each exam page is noted with its specific exam code (e.g. _exams/AZ-900.md). In the exam page you will find information and the links for the Official exam page and the Official Exam Labs as found in Github.

### Navigation

This page contains the navigation links.

### General Page guidelines

- All links in the pages should be the officially maintained aka.ms links, to avoid dead links or added maintenance
- Link addition or removal should follow the ESI program closing deck and program guidelines

## Debug and live changes

- Open a terminal on codespaces and build the site and make it available on a local server.

    ```bundle config set path 'vendor/bundle'``` **(Only once)**


    ```bundle exec jekyll serve --livereload```

- On terminal **Ports**  make port 4000 **Public**. Changes made to markdown files will be reloaded **live** (not supported for Gemfile or _config.yml files)

## Application Insights

To update the Application Insights resource change the connection string located in the following file /workspaces/ESI_Resources/_includes/head/custom.html

## Image Assets guidelines

### Emoticons
Taken from https://github.com/caiyongji/emoji-list

### Certification icons
**FOR TEASER/GRID** Taken from credly profiles as they all have 600x600 format. Example: https://www.credly.com/users/unai-huete/badges

IMPORTANT TODO --> Images should be modified to be wider for the grid container, define SIZE AND SOURCE!
**FOR EXAM PAGE** taken from specific exam pages such as: https://docs.microsoft.com/en-us/learn/certifications/exams/dp-100 and **Copy image link**

