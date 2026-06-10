I would like to summarize the contents of an online course  for faster learning. Here I explain how I would like to be the summary, so that you can generate it for me. You will find specific information represented by variables in curly brackets. At the end of the prompt, the values of these variables are provided.

The course name is the following: {course-name}.
The course public URL is the following: {course-url}.
The course learning link is the following: {course-learning-link}.
You will find the credentials to log in in the .env file at the root level of this folder; the variables to use are {username} and {password}.

The course is organized in sections or modules, and each of them has some subsections and lectures. These lectures can contain:

- Text (and/or code) along with images and embedded videos
- Links to exercises or lab sessions in external platforms

The summary should be arranged as follows:

- Write the summary in the README.md of the course folder {course-folder}.
- Save any images in the assets folder {assets-folder} inside the course folder. Images should have descriptive names, not random strings. Then, the summary should reference them with a link where it belongs.
- Save any exercises or lab sessions in the exercises folder {exercises-folder} inside the course folder. Each exercise should have a file or a folder, prefixed with a number "01", "02", etc., according to the appearance order in the course. Then, the summary should reference it with a link where it belongs.


Tools you can use:

- Playwright MCP if you need to log in and navigate through the course to extract the information using the browser.
- Context7 MCP every time you have code snippets; check that that the code is correct and properly formatted according to the latest version of the used libraries or frameworks.
- Any other tool you consider useful.


Summary format:

- Use concise bullet points with full but short sentences.
  - Use nested bullets for hierarchy when it improves learning.
  - Use deeper nesting when several ideas belong under one parent point.
  - Use parent bullets to introduce shared phrasing.
    - Put repeated items as child bullets.
    - Write child bullets as concise fragments when the parent supplies the grammar.
  - Keep each sentence focused on one idea.
  - Allow two tightly connected ideas in one sentence if it keeps the summary compact.
  - Do not omit relevant details.
  - Do not repeat the same detail in multiple places.
  - Do not repeat concepts, sentence stems, or shared phrases across sibling bullets.
  - Expand acronyms on first use with the full phrase in parentheses.
- Do not insert blank lines between higher-level bullet points.
- Put minor explanatory details that can be represented in code as comments.
- When there is no code explained in the section, omit the code block.
- If the original section includes image links, keep them after the bullet summary and before any notebook/script link or code block.
- For every linked notebook or script found in the section, add the notebook/script summary directly below its link, if you have access to the notebook or code file.
- Summarize the linked files in concise hierarchical bullets.
- Include purpose, major steps, important inputs/outputs, assumptions, and relevant API choices.
- Note any modernization performed, but keep this brief.


Editing rules:

- Use structured parsers when practical:
  - Read `.ipynb` as JSON and preserve notebook metadata.
  - Treat Markdown links and headings structurally when reasonable.
- Keep summaries faithful to the source material, but update generic comments and code snippets to modern APIs/style when Context7 shows a newer recommended approach.
- Do not invent details that are absent from the section or linked files.
- Do not expand lists by repeating the same phrase. Prefer `Common features include:` with nested items over repeated `Common features include ...` bullets.
- Do not over-nest lists when a compact sentence with two related ideas is clearer.
- Explain acronyms on first use, then use the acronym afterward.
- Replace only the requested section text in the source file. Preserve the section heading and neighboring sections.
- Do not add blank lines between top-level bullets in generated summaries.
- If Context7 documentation conflicts with the source text, preserve the source's learning point and update only the API/style details needed to keep examples current.
- If a link is broken, mention it and continue summarizing the available section.
- If an API cannot be verified through Context7, state that verification was not available and avoid unnecessary changes.


Some additional and styling guidelines:

- A
- B

---

Here are the values of the variables:

{course-name} = SQL and Data Modeling for the Web with Python
{course-url} = https://www.udacity.com/course/sql-and-data-modeling-for-the-web--cd0046
{course-learning-link} = https://www.udacity.com/enrollment/cd0046
{username} = UDACITY_USERNAME
{password}= UDACITY_PASSWORD
{course-folder} = 06_SQL_DataModelling
{assets-folder} = assets
{exercises-folder} = lab
