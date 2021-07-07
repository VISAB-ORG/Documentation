# Documentation

Dependencies required: [DocFx](https://dotnet.github.io/docfx/)

When changes were made to the source of Projects that are part of the documentation do the following steps
1. Make sure the repositories that have changed are in the same directory as Documentation
2. Run `generate_docfx.py` whilst inside generation/
3. Copy the contents of docfx_project/_site into your clone of the `VISAB/visab-org.github.io` repository
4. Create a new commit inside `VISAB/visab-org.github.io` and push it.

The new version of the site should be hosted within a couple minutes.

If you want to add pages to the documentation manually, integrate them into docfx_project as markdown files.\
Then do steps 2-4.
