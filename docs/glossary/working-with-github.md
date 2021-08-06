This guide is written with the team in mind. The majority of our projects are narrowly-focused to solving customer problems, such as Cisco Refresh or KPOM, and this set of best practices reflects that. These are a lot of lessons learned from working on large opensource projects such as Orchard Core, that influence this approach, but it is recognised that (much like in client project management) different projects come with different needs and no single set of tools or methodologies can be universally applied.

!!! Important
    The following items should be required across all repositories managed by our team. By keeping the same experience across all our repositories, it makes it easier for B Skwad and external contributors to work within any repository and operate with the same assumptions as any other B Skwad repository.

## Documentation

Maintain project documentation within the repository, in a `./docs` subfolder. This keeps everything portable and usable even when offline. There are two main varieties of documentation typically associated with open source software: usage instructions and maintenance guidelines. Most of this section focuses on maintenance guidelines to support the process you’ve outlined, as usage instructions will vary widely between projects.

!!! tip
    Documentation associated with B Skwad projects should be hosted using GitHub Pages, by writing _markdown_ files in the `./docs` subfolder. Which will be automatically built and pushed to a `gh-pages` branch that deploys to our GitHub Pages site, on a successful merge to `master`.

## Code coverage

Every feature should be accompanied with tests and all pull requests should come with associated tests, all living within a `tests` directory. While we have no intention of striving for 100% code coverage, we should aim for above 80% with above 90% being the ideal. We should also look to utilise a code coverage / automated code review tool like `Codecov` and ensure that is a pull request requirement before merging.

## Issue and PR labels

The following labels should be our standard set of labels across all repositories to help ensure we use clear and consistent labelling terminology. This will allow us to see the status and type of all issues at a glance, to help track and report on contributions across our repositories, and to provide easier ways to find issues to contribute to (e.g., all needs:ux and good-first-issues). We’re starting a minimal set of labels and will let progressive enhancement further define them for us as well as perform occasional housekeeping.

- `type:bug` - “Something isn’t working.” (color: #d73a4a)
- `type:enhancement` - “New feature or request.” (color: #a2eeef)
- `type:invalid` - “This doesn't seem right.” (color: #993299)
- `type:question` - “Further information is requested.” (color: #d876e3)
- `type:wont-fix` - “This issue or pull request already exists.” (color: #d876e3)
- `needs:code-review` - “This requires code review.” (color: #999999)
- `needs:design` - “This requires design to resolve.” (color: #999999)
- `needs:documentation` - “This requires documentation.” (color: #999999)
- `needs:feedback` - “This requires feedback to determine next steps.” (color: #999999)
- `needs:refresh` - “This requires a refreshed PR to resolve.” (color: #999999)
- `needs:tests` - “This requires tests.” (color: #999999)
- `resolution:not-applicable` - “We do not feel this issue is valid.” (color: #FFA500)
- `resolution:not-reproducible` - “We are unable to reproduce this issue.” (color: #FFFF00)
- `resolution:resolved` - “This issue has been resolved.” (color: #008000)
- `resolution:postfix` - “We do not intend to resolve this issue.” (color: #000000)

## Workflows

Standardising on a workflow is an important part of the development process. Utilising an effective workflow ensures efficient collaboration and quicker project onboarding. For this reason, we will be [using GitFlow](gitflow.md).

### Commits

Commits should be small and independent items of work, containing changes limited to a distinct idea. Distinct commits are essential in keeping features separate, pushing specific features forward, or reversing or rolling back code if necessary.

#### Commit Messages

The first line of a commit message is a brief summary of the changeset, describing the expected result of the change or what is done to affect change.

``` zsh
git log --oneline -5

# fca8925 Update commit message best practices
# 19188a0 Add a note about autoloading transients
# 9630552 Fix a typo in apply_mtu/task.yml
# 2309e04 Remove extra markdown header hash
# 5cd2604 Add h3 and h4 styling to README.md
```

This brief summary is always required. It is around 50 characters or less, always stopping at 70. The high visibility of the first line makes it critical to craft something that is as descriptive as possible within space limits. And example is given below.

``` zsh
git commit -m "Add an eos module to support MTU"
```

### Protecting the `master` Branch

All repositories are to be configured so the `master` branch is protected to prevent direct pushes. All merges should be made through a pull request, which ensures all code changes are peer reviewed before merging to prevent unintentional code reversions. Additionally, protecting branches provides the following benefits:

- Prevents the `master` branch from being accidentally deleted by other engineers
- Prevents force-pushes to the branch, overwriting the history

### New Development

The `master` branch represents a stable, released, versioned product. Ongoing development will happen in feature branches branched off a `develop` branch, which is itself branched off `master`.

All new features will treat the `develop` branch as the canonical source. Feature branches will branch off `develop` and should always have `develop` merged back into them before requesting peer code review and before deploying to any staging environments. This pattern is commonly referred to as the [GitFlow](gitflow.md).

### Semantic Versioning

As we assign version numbers to our software, we follow the Semantic Versioning pattern, wherein each version follows a **MAJOR.MINOR.PATCH** scheme:

- **MAJOR** versions are incremented when breaking changes are introduced, such as functionality being removed or otherwise major changes to the codebase.
- **MINOR** versions are incremented when new functionality is added in a backwards-compatible manner.
- **PATCH** versions are incremented for backwards-compatible bugfixes.

Imagine Erik has written a new zone parser: _parse_zone_. He might give his first public release version **1.0.0.** After releasing the module, Erik decides to add some new (backwards-compatible) features, and subsequently releases version **1.1.0**. Later, Christi finds a bug and reports it to Erik via a [GitHub Issue](https://github.com/b-skwad/duckview/issues); no functionality is added or removed, but Erik fixes the bug and releases version **1.1.1**.

Down the road, Erik decides to remove some functionality or change the way some functions are used. Since this would change how others interact with his code, he would declare this new release to be version **2.0.0**, hinting to consumers that there are breaking changes in the new version of his module.

#### Deleting or Archiving and Deleting Branches

This workflow will inevitably build up a large list of branches in the repository. To prevent a large number of unused branches living in the repository, we’ll delete or archive and delete them after feature development is complete.

### Deleting branches

When projects use non-ff merges to `master`, we can safely delete feature branches because all commits are preserved and can be located from the merge commit.

- Move to another branch (doesn’t matter which): eg. `git checkout master`
- Delete the branch (both on local and remote): `git branch -D branch-name; git push :branch-name`
