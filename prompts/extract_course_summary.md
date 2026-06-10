I need a new skill called `/extract-course-summary` which extracts some online course content and summarizes it. The skill call should be as follows:

```
# General call
/extract-course-summary folder <course-folder> config <config-file>

# Example call
/extract-course-summary folder @06_SQL_DataModelling config course_config.json
```

The <course-folder> should contain the <config-file>, which is a JSON file with the following structure:

```json
{
  "course-name": "SQL and Data Modeling for the Web with Python",
  "course-url": "https://www.udacity.com/course/sql-and-data-modeling-for-the-web--cd0046",
  "course-learning-link": "https://www.udacity.com/enrollment/cd0046",
  "assets-folder": "assets",
  "exercises-folder": "lab"
}
```

Then, the skill needs to carry out the attached instructions.

Create the skill.

---

(Skill instructions)

You need to summarize the contents of an online course for faster learning. You will find specific information represented by variables in curly brackets. The values of these variables are provided in the <config-file>. Therefore, first read the <config-file> to get the values of the variables.

The course name is the following: {course-name}.
The course public URL is the following: {course-url}.
The course learning link is the following: {course-learning-link}.

The user must log in manually in the web browser. Once the user confirms that the course learning page is authenticated and ready, analyze the page without requesting, reading, handling, entering, storing, or transmitting login secrets.

The course is organized in sections or modules, and each of them has some subsections and lectures. These lectures can contain:

- Text (and/or code) along with images and embedded videos
- Links to exercises or lab sessions in external platforms

The summary should be arranged as follows:

- Write the summary in the README.md of the course folder {course-folder}.
- Save any images in the assets folder {assets-folder} inside the course folder. Images should have descriptive names, not random strings. Then, the summary should reference them with a link where it belongs.
- Save any exercises or lab sessions in the exercises folder {exercises-folder} inside the course folder. Each exercise should have a file or a folder, prefixed with a number "01", "02", etc., according to the appearance order in the course. Then, the summary should reference it with a link where it belongs.

Tools you can use:

- Browser automation or page inspection tools to analyze the course after the user logs in manually.
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


I can imagine you could follow this plan or series of steps:

1. Open the course learning link. If it is not authenticated, ask the user to log in manually in the browser and confirm when the course page is ready.
2. Extract the table of contents of the course, including sections, subsections, and lectures. Create the section headers in the README.md of {course-folder} according to the course structure; create that README.md if it does not exist. Similarly, create the folders {assets-folder} and {exercises-folder} if they do not exist.
3. For each lecture or learning unit, extract the content as follows:
   - Extract the text, the images and the video transcripts, if available. Put the extracted information in their corresponding place: text in the README.md, images and related media in {assets-folder}, and exercises in {exercises-folder}.
   - Keep a list of the pieces you could not extract in the README.md, so that you can mention them to me; I will fetch them manually. Typically, these will be exercises or media.
   - You don't have to donwload the videos, but if they have public URLs (like YouTube or Vimeo), you can include them in the summary.
- 4. Notify me clearly when you are done and request to donwload the missing pieces.
- 5. Once I have provided you with the missing pieces, run the summarization of the README.md section by section, using the editing rules and summary format described above. For each section, replace the original text with the generated summary, but keep the section header and neighboring sections unchanged.
  - When exercises are processed (code files, notebooks, etc.), add the summary of the exercise directly below the link to the exercise in the README.md. Also, update the environment requirements files with the dependencies needed to run the exercise, if they are not already included. These will be either conda environment files, pip requirements files, or uv files, depending on the course. The root README.md should have a "setup" (or similar) section which specifies how to set up the environment.
