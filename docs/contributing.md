<h1 align="center" style="font-weight: bold">
    Contributing to md2pdf
</h1>

First off, thanks for taking the time to contribute! ❤️

All types of contributions are encouraged and valued. See the [Table of Contents](#toc) for different ways to help and details about how this project handles them. Please make sure to read the relevant section before making your contribution. It will make it a lot easier for us maintainers and smooth out the experience for all involved. The community looks forward to your contributions. 🎉

And if you like the project, but just don't have time to contribute, that's fine. There are other easy ways to support the project and show your appreciation, which we would also be very happy about:

- Star the project
- Tweet about it
- Refer this project in your project's README
- Mention the project at local meetups and tell your friends/colleagues


<div class="toc"><h2 id="toc"><b><a href="#toc">Table of Contents</a></b></h2>
<ul><li><a href="#code-of-conduct">Code of Conduct</a></li><li><a href="#i-have-a-question">I Have a Question</a></li><li><a href="#i-want-to-contribute">I Want To Contribute</a><ul><li><a href="#i-want-to-contribute-legal-notice">Legal Notice</a></li><li><a href="#i-want-to-contribute-reporting-bugs">Reporting Bugs</a><ul><li><a href="#i-want-to-contribute-reporting-bugs-before-submitting-a-bug-report">Before Submitting a Bug Report</a></li><li><a href="#i-want-to-contribute-reporting-bugs-how-do-i-submit-a-good-bug-report">How Do I Submit a Good Bug Report?</a></li></ul></li><li><a href="#i-want-to-contribute-suggesting-enhancements">Suggesting Enhancements</a><ul><li><a href="#i-want-to-contribute-suggesting-enhancements-before-submitting-an-enhancement">Before Submitting an Enhancement</a></li><li><a href="#i-want-to-contribute-suggesting-enhancements-how-do-i-submit-a-good-enhancement-suggestion">How Do I Submit a Good Enhancement Suggestion?</a></li></ul></li><li><a href="#i-want-to-contribute-your-first-code-contribution">Your First Code Contribution</a></li><li><a href="#i-want-to-contribute-improving-the-documentation">Improving The Documentation</a></li></ul></li><li><a href="#submitting-a-pull-request">Submitting a Pull Request</a><ul><li><a href="#submitting-a-pull-request-dont-s">Dont’s</a></li></ul></li><li><a href="#style-guides">Style guides</a><ul><li><a href="#style-guides-commit-messages">Commit Messages</a></li><li><a href="#style-guides-code">Code</a></li></ul></li><li><a href="#join-the-project-team">Join The Project Team</a></li><li><a href="#attribution">Attribution</a></li></ul></div>

<h2 id="code-of-conduct"><b><a href="#code-of-conduct">Code of Conduct</a></b></h2>

This project and everyone participating in it is governed by the
[md2pdf Code of Conduct](coc.md).
By participating, you are expected to uphold this code. Please report unacceptable behavior
to <>.

<h2 id="i-have-a-question"><b><a href="#i-have-a-question">I Have a Question</a></b></h2>

> If you want to ask a question, we assume that you have read the available [Latest Documentation (0.0.x.x)](docs/0/0/index.md).

Before you ask a question, it is best to search for existing [Issues](https://github.com/whinee/md2pdf/issues) that might help you. In case you have found a suitable issue and still need clarification, you can write your question in this issue. It is also advisable to search the internet for answers first.

If you then still feel the need to ask a question and need clarification, we recommend the following:

- Open an [Issue](https://github.com/whinee/md2pdf/issues/new).
- Provide as much context as you can about what you're running into.
- Provide the following information:
    - OS name and version
        If in Linux, include linux distribution and kernel version; and
    - Python version

We will then take care of the issue as soon as possible.

<h2 id="i-want-to-contribute"><b><a href="#i-want-to-contribute">I Want To Contribute</a></b></h2>

<h2 id="i-want-to-contribute-legal-notice"><b><i><a href="#i-want-to-contribute-legal-notice">Legal Notice</a></i></b></h2>

> When contributing to this project, you must agree that you have authored 100% of the content, that you have the necessary rights to the content and that the content you contribute may be provided under the project license.

<h2 id="i-want-to-contribute-reporting-bugs"><b><i><a href="#i-want-to-contribute-reporting-bugs">Reporting Bugs</a></i></b></h2>

<h2 id="i-want-to-contribute-reporting-bugs-before-submitting-a-bug-report"><a href="#i-want-to-contribute-reporting-bugs-before-submitting-a-bug-report">Before Submitting a Bug Report</a></h2>

A good bug report shouldn't leave others needing to chase you up for more information. Therefore, we ask you to investigate carefully, collect information and describe the issue in detail in your report. Please complete the following steps in advance to help us fix any potential bug as fast as possible.

- Make sure that you are using the latest version.
- Determine if your bug is really a bug and not an error on your side e.g. using incompatible environment components/versions (Make sure that you have read the [Latest Documentation (0.0.x.x)](docs/0/0/index.md). If you are looking for support, you might want to check [this section](#i-have-a-question)).
- To see if other users have experienced (and potentially already solved) the same issue you are having, check if there is not already a bug report existing for your bug or error in the [bug tracker](https://github.com/whinee/md2pdfissues?q=label%3Abug).
- Also make sure to search the internet (including Stack Overflow) to see if users outside of the GitHub community have discussed the issue.

- Collect information about the bug
- Stack trace (Traceback)
- OS, Platform and Version (Windows, Linux, macOS, x86, ARM)
- Version of the interpreter, compiler, SDK, runtime environment, package manager, depending on what seems relevant.
- Possibly your input and the output
- Can you reliably reproduce the issue? And can you also reproduce it with older versions?

<h2 id="i-want-to-contribute-reporting-bugs-how-do-i-submit-a-good-bug-report"><a href="#i-want-to-contribute-reporting-bugs-how-do-i-submit-a-good-bug-report">How Do I Submit a Good Bug Report?</a></h2>

> You must never report security related issues, vulnerabilities or bugs including sensitive information to the issue tracker, or elsewhere in public. Instead sensitive bugs must be sent by email to <>.

We use GitHub issues to track bugs and errors. If you run into an issue with the project:

- Open an [Issue](https://github.com/whinee/md2pdf/issues/new). (Since we can't be sure at this point whether it is a bug or not, we ask you not to talk about a bug yet and not to label the issue.)
- Explain the behavior you would expect and the actual behavior.
- Please provide as much context as possible and describe the *reproduction steps* that someone else can follow to recreate the issue on their own. This usually includes your code. For good bug reports you should isolate the problem and create a reduced test case.
- Provide the information you collected in the previous section.

Once it's filed:

- The project team will label the issue accordingly.
- A team member will try to reproduce the issue with your provided steps. If there are no reproduction steps or no obvious way to reproduce the issue, the team will ask you for those steps and mark the issue as `needs-repro`. Bugs with the `needs-repro` tag will not be addressed until they are reproduced.
- If the team is able to reproduce the issue, it will be marked `needs-fix`, as well as possibly other tags (such as `critical`), and the issue will be left to be [implemented by someone](#your-first-code-contribution).

<!-- You might want to create an issue template for bugs and errors that can be used as a guide and that defines the structure of the information to be included. If you do so, reference it here in the description. -->

<h2 id="i-want-to-contribute-suggesting-enhancements"><b><i><a href="#i-want-to-contribute-suggesting-enhancements">Suggesting Enhancements</a></i></b></h2>

This section guides you through submitting an enhancement suggestion for md2pdf, **including completely new features and minor improvements to existing functionality**. Following these guidelines will help maintainers and the community to understand your suggestion and find related suggestions.

<h2 id="i-want-to-contribute-suggesting-enhancements-before-submitting-an-enhancement"><a href="#i-want-to-contribute-suggesting-enhancements-before-submitting-an-enhancement">Before Submitting an Enhancement</a></h2>

- Make sure that you are using the latest version.
- Read the [Latest Documentation (0.0.x.x)](docs/0/0/index.md) carefully and find out if the functionality is already covered, maybe by an individual configuration.
- Perform a [search](https://github.com/whinee/md2pdf/issues) to see if the enhancement has already been suggested. If it has, add a comment to the existing issue instead of opening a new one.
- Find out whether your idea fits with the scope and aims of the project. It's up to you to make a strong case to convince the project's developers of the merits of this feature. Keep in mind that we want features that will be useful to the majority of our users and not just a small subset. If you're just targeting a minority of users, consider writing an add-on/plugin library.

<h2 id="i-want-to-contribute-suggesting-enhancements-how-do-i-submit-a-good-enhancement-suggestion"><a href="#i-want-to-contribute-suggesting-enhancements-how-do-i-submit-a-good-enhancement-suggestion">How Do I Submit a Good Enhancement Suggestion?</a></h2>

Enhancement suggestions are tracked as [GitHub issues](https://github.com/whinee/md2pdf/issues).

- Use a **clear and descriptive title** for the issue to identify the suggestion.
- Provide a **step-by-step description of the suggested enhancement** in as many details as possible.
- **Describe the current behavior** and **explain which behavior you expected to see instead** and why. At this point you can also tell which alternatives do not work for you.
- You may want to **include screenshots and animated GIFs** which help you demonstrate the steps or point out the part which the suggestion is related to. You can use [this tool](https://www.cockos.com/licecap/) to record GIFs on macOS and Windows, and [this tool](https://github.com/colinkeenan/silentcast) or [this tool](https://github.com/GNOME/byzanz) on Linux. <!-- this should only be included if the project has a GUI -->
- **Explain why this enhancement would be useful** to most md2pdf users. You may also want to point out the other projects that solved it better and which could serve as inspiration.

<!-- TODO
You might want to create an issue template for enhancement suggestions that can be used as a guide and that defines the structure of the information to be included. If you do so, reference it here in the description. -->

<h2 id="i-want-to-contribute-your-first-code-contribution"><b><i><a href="#i-want-to-contribute-your-first-code-contribution">Your First Code Contribution</a></i></b></h2>
<!-- TODO
include Setup of env, IDE and typical getting started instructions?

-->

<h2 id="i-want-to-contribute-improving-the-documentation"><b><i><a href="#i-want-to-contribute-improving-the-documentation">Improving The Documentation</a></i></b></h2>
<!-- TODO
Updating, improving and correcting the documentation

-->

<h2 id="submitting-a-pull-request"><b><a href="#submitting-a-pull-request">Submitting a Pull Request</a></b></h2>

This is based on [Michael Herrmann](https://gist.github.com/mherrmann)'s gist titled [Good PRs are minimal](https://gist.github.com/mherrmann/5ce21814789152c17abd91c0b3eaadca).

Every Pull Request (hereinafter referred to as PR) should have one, and only one, unique goal. The PR should make the absolute minimum number of changes that are required to achieve this goal.

The fewer things you change, the easier it will be for the team to see what you did, and thus gain confidence that you PR makes sense.

<h2 id="submitting-a-pull-request-dont-s"><b><i><a href="#submitting-a-pull-request-dont-s">Dont’s</a></i></b></h2>

- Changing whitespace unnecessarily, eg. switching tabs and spaces.

    This leads to huge numbers of unnecessarily changed lines of code.

- Running a linter not listed in [the linters currently used by the project](docs/0/0/getting-started.md)
- Don't unnecessarily introduce new tools or dependencies. I'm sure you have your
   favorites. But don't force them on me or other contributors. Stick to those
   that are absolutely required, or come with the language.
- Obey the same code style as the library: Tabs or spaces, maximum line length,
   etc.

In short: Good PRs are minimal. You're very welcome to add several improvements.
But please make them in separate PRs.

<h2 id="style-guides"><b><a href="#style-guides">Style guides</a></b></h2>

<h2 id="style-guides-commit-messages"><b><i><a href="#style-guides-commit-messages">Commit Messages</a></i></b></h2>

This repository does not enforce a style guide on commits. However, it is highly recommended to be concise and informative when writing commit messages.

<h2 id="style-guides-code"><b><i><a href="#style-guides-code">Code</a></i></b></h2>

This project uses the following linters for the

<h2 id="join-the-project-team"><b><a href="#join-the-project-team">Join The Project Team</a></b></h2>
<!-- TODO -->

<h2 id="attribution"><b><a href="#attribution">Attribution</a></b></h2>

This guide is based on the **contributing-gen**. [Make your own](https://github.com/bttger/contributing-gen)!
