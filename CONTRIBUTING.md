# On Github Issues and Pull Requests

Found a bug? Have a new feature to suggest? Want to contribute changes to the codebase? Make sure to read this first.

## Bug reporting

Your code doesn't work, and you have determined that the issue lies with ColabComponent? Follow these steps to report a bug.

1.  Your bug may already be fixed. Make sure to update to the current ColabComponent master branch.

2.  Search for similar issues. Make sure to delete `is:open` on the issue search to find solved tickets as well. It's possible somebody has encountered this bug already. Still having a problem? Open an issue on Github to let us know.

3.  Make sure you provide us with useful information about your configuration: what OS are you using?

4.  Provide us with a script to reproduce the issue. This script should be runnable as-is and should not require external data download (use randomly generated data if you need to run a pipline on some test data). We recommend that you use Github Gists to post your code. Any issue that cannot be reproduced is likely to be closed.

5.  If possible, take a stab at fixing the bug yourself --if you can!

The more information you provide, the easier it is for us to validate that there is a bug and the faster we'll be able to take action. If you want your issue to be resolved quickly, following the steps above is crucial.

* * *

## Requesting a Feature

You can also use Github issues to request features you would like to see in ColabComponent, or changes in the ColabComponent API.

1.  Provide a clear and detailed explanation of the feature you want and why it's important to add. Keep in mind that we want features that will be useful to the majority of our users and not just a small subset. If you're just targeting a minority of users, consider writing an add-on library for ColabComponent. It is crucial for ColabComponent to avoid bloating the API and codebase.

2.  Provide code snippets demonstrating the API you have in mind and illustrating the use cases of your feature. Of course, you don't need to write any real code at this point!

3.  After discussing the feature you may choose to attempt a Pull Request. If you're at all able, start writing some code. We always have more work to do than time to do it. If you can write some code then that will speed the process along.

* * *

## Pull Requests

**Where should I submit my pull request?**

1.  **ColabComponent improvements and bugfixes** go to the [ColabComponent `master` branch](https://github.com/PPierzc/ColabComponent/tree/master).

Please note that PRs that are primarily about **code style** (as opposed to fixing bugs, improving docs, or adding new functionality) will likely be rejected.

Here's a quick guide to submitting your improvements:

1.  Write the code (or get others to write it). This is the hard part!

2.  Make sure any new function or class you introduce has proper docstrings. Make sure any code you touch still has up-to-date docstrings and documentation. **Docstring style should be respected.** In particular, they should be formatted in MarkDown, and there should be sections for `Arguments`, `Returns`, `Raises` (if applicable). Look at other docstrings in the codebase for examples.

3.  Write tests. Your code should have full unit test coverage. If you want to see your PR merged promptly, this is crucial.

4.  Make sure all tests are passing

5.  We use PEP8 syntax conventions, but we aren't dogmatic when it comes to line length. Make sure your lines stay reasonably sized, though. To make your life easier, we recommend running a PEP8 linter:
    -   Install PEP8 packages: `pip install pep8 pytest-pep8 autopep8`
    -   Run a standalone PEP8 check: `py.test --pep8 -m pep8`
    -   You can automatically fix some PEP8 error by running: `autopep8 -i --select <errors> <FILENAME>` for example: `autopep8 -i --select E128 tests/ColabComponent`

6.  When committing, use appropriate, descriptive commit messages.

7.  Update the documentation. If introducing new functionality, make sure you include code snippets demonstrating the usage of your new feature.

8.  Submit your PR. If your changes have been approved in a previous discussion, and if you have complete (and passing) unit tests as well as proper docstrings/documentation, your PR is likely to be merged promptly.

* * *

## Adding new examples

Even if you don't contribute to the ColabComponent source code, if you have an application of ColabComponent that is concise and powerful, please consider adding it to our collection of examples. [Existing examples](https://github.com/PPierzc/ColabComponent/tree/master/examples) show idiomatic ColabComponent code: make sure to keep your own script in the same spirit.
