# **GitLab Flow**

This workflow combines [feature-driven development](https://en.wikipedia.org/wiki/Feature-driven_development) and [feature branches](https://martinfowler.com/bliki/FeatureBranch.html) with issue tracking.

**Main (or master):** This is the main branch where all the development comes together. your **`main`** branch remains a reliable "**source of truth**" that always contains production-ready code. We also call it as integration branch that contains the latest completed features, improvements, and bug fixes.

**Feature branches:** These are branches created from the main branch for the development of each new feature. Once the feature is complete and tested, it is merged back into main. The branch is then typically deleted to keep things tidy. You create a pull request or merge request in the GitLab or GitHub UI. This is a proposal to merge your feature branch into the main branch. (**feature/description**)

**Bugfix branches:** These are branches created for fixing bugs. Similar to feature branches, they are created from the main branch, and once the fix is complete and tested, the changes are merged back into main. (**bugfix/description**)

**Release branches:** each release has an associated release branch that is based off the main branch. After announcing a release branch, only add serious bug fixes to the branch. If possible, first merge these bug fixes into main, and then cherry-pick them into the release branch (**release/1.2**)

![**working with new features**](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/b9546257-6c69-4eed-8908-c6148900781d/git-flow.svg)

**working with new features**

![                                                          ****Release branches with GitLab Flow****](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/ecac5d5e-00f4-46b2-a5f5-58a619c0cdb3/Untitled.png)

                                                          ****Release branches with GitLab Flow****

Here’s a simplified version of the GitLab Flow, which includes the use of feature branches, testing (staging) environments, and the production environment:

### Workflow Steps:

1. **Main Branch**:
    - `main` represents the production-ready state of your code.
2. **Feature/Bugfix Branches**:
    - For new features, you create a branch from `main`, e.g., `feature/add-login`.
    - Work is done on the feature branch and tested locally.
3. **Merge Requests (MR)**:
    - Once the feature is complete, you create a **Merge Request (MR)** to merge `feature/add-login` into `main`.
    - Each MR is reviewed and, upon approval, merged into **`main`**.
4. **Continuous Integration**:
    - Every merge into **`main`** triggers the CI pipeline which runs automated tests to ensure that the integration does not break the existing build..
5. **Deployment to** **Testing/Staging**:
    - If the CI pipeline passes, The `main` branch is automatically deployed to a testing environment for further testing.
6. **Production**:
    - Once the `main` branch is tested in staging and is confirmed stable, a release is created (e.g., `release/v1.0.0)` from `main`, and the tagged branch is deployed to production. The code on this branch should not include new features after this point—only bug fixes, performance improvements, or other necessary updates.
7. **Bugfix Branches**:
    - If a critical issue is found in production, you create a bugfix branch from `main`, fix the issue, test it, and go through a similar MR process to deploy the fix.
8. **Hotfix Branches:**
    - Hotfixes for any issues discovered in production are made directly on the release branch and then merged back into **`main`** and any other active development branches to ensure that the fixes are integrated into the ongoing development work.

### Example `.gitlab-ci.yml` Configuration:

```yaml
stages:
  - test
  - deploy_staging
  - deploy_production

test:
  stage: test
  script:
    - echo "Run automated tests"
    - run-your-tests-here # Replace with your actual test commands

deploy_staging:
  stage: deploy_staging
  script:
    - echo "Deploy to staging environment"
    - deploy-to-staging-script # Replace with your actual deploy to staging commands
  environment:
    name: staging
  only:
    - main

deploy_production:
  stage: deploy_production
  script:
    - echo "Deploy to production environment"
    - deploy-to-production-script # Replace with your actual deploy to production commands
  environment:
    name: production
  when: manual
  only:
    - tags # or add release branches release/v.* 

```

In this `.gitlab-ci.yml`:

- `test` runs automated tests for merge requests, feature/bugfix branches.
- `deploy_staging` if previous job passes, deploys the `main` branch to a staging environment after the merge is complete.
- `deploy_production` is a manual job that deploys a tagged commit to the production environment.

This flow ensures that all new features are reviewed and tested before they are deployed to production. The usage of environments and tagging (release) helps manage releases in an orderly fashion, and bugfixes can be handled expediently when needed.