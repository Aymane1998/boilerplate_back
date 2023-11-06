# Setup GitLab

- [Setup GitLab](#setup-gitlab)
- [Git branch strategy](#git-branch-strategy)
- [Pull/Merge Template](#pullmerge-template)
- [Pull/Merge Request Labelling System](#pullmerge-request-labelling-system)
- [GitLab CI/CD](#gitlab-cicd)

---

# Git branch strategy

We uses GitLab Flow as our git branching strategy because GitLab Flow offers more flexibility and control, which might be necessary for larger teams or more complex applications that require rigorous testing and release processes before features reach the end-users.

**[Git branch strategy](git_branch_strategy.md)**

---

# Pull/Merge Template

In GitLab, a merge request template is used to provide a predefined structure for contributors to follow when opening a new merge request. the template is stored in the default branch on **[.gitlab/merge_request_templates/feature_request_template.md](../.gitlab/merge_request_templates/feature_request_template.md)**

you should fill the template on each of the new merge requests.

---

# Pull/Merge Request Labelling System

For managing merge requests (MRs) in GitLab (since GitLab refers to "pull requests" as "merge requests"), a simple label system helps in categorizing and tracking the progress of changes. Here's a straightforward labeling system you can consider:

1. **Status Labels**:
    - `Status: Work In Progress` - For MRs actively being worked on.
    - `Status: Review Needed` - For MRs that need to be reviewed by peers or maintainers.
    - `Status: Changes Requested` - For MRs where reviewers have asked for additional changes before merging.
2. **Priority Labels**:
    - `Priority: Low` - For changes that are not urgent.
    - `Priority: Medium` - For normal priority changes.
    - `Priority: High` - For changes that should be addressed as soon as possible.
    - `Priority: Critical` - For urgent changes that may affect production or release deadlines.
3. **Type Labels**:
    - `Type: Bug` - For MRs related to bug fixes.
    - `Type: Feature` - For MRs introducing new features.
    - `Type: Improvement` - For MRs improving existing features.
    - `Type: Documentation` - For MRs related only to documentation updates.
    - `Type: Refactor` - For MRs involving code refactoring without changing behavior.
4. **Size Labels** (to give an idea about the MR size):
    - `Size: XS` - Extra small changes, like typo fixes.
    - `Size: S` - Small changes that affect only a few lines or files.
    - `Size: M` - Medium changes that affect a moderate part of the system.
    - `Size: L` - Large changes that introduce significant modifications.
    - `Size: XL` - Extra large changes that could potentially affect the system as a whole.

This set of labels should provide enough information for managing your MRs effectively. Labels for type, status, priority, and size are typically sufficient for many projects. you should apply multiple labels to the same merge request (MR) in GitLab to provide as much context as needed.

---

# GitLab CI/CD

We use GitLab CI/CD pipelines to trigger on each push to test, build and deploy. you can see **[.gitlab-ci.yml](../.gitlab-ci.yml)** yaml file that contains the configuration for your CI/CD pipeline.