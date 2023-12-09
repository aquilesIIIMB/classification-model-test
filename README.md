# Classification Model Test
 
Testing a classification model using IRIS dataset

## Setup for GCP Projects 
### ml-framework-maas 
* **Service Accounts:**  
app-f20001fa-bf71-4938-a8d6-90@ml-framework-maas.iam.gserviceaccount.com
* **Cloud Storage Buckets:**  
iris-classification-7d27cd50-3188-4385-bb6b-ce0cd598204a
* **Bigquery Datasets:**  
iris_classification

### ml-framework-exploration 
* **Service Accounts:**  

* **Cloud Storage Buckets:**  

* **Bigquery Datasets:**  


### ml-framework-discovery 
* **Service Accounts:**  

* **Cloud Storage Buckets:**  

* **Bigquery Datasets:**  



## Project structure
```
.
├── README.md
├── cookiecutter.json
├── docs
│   └── index.md
├── fields.json
├── hooks
│   ├── post_gen_project.py
│   └── pre_gen_project.py
└── classification-model-test
    ├── LICENSE
    ├── README.md
    ├── discovery
    ├── exploration
    │   ├── cloudbuild.yaml
    │   └── experiment_setup
    │       └── experiment_0
    │           └── model_0
    │               ├── evaluation
    │               ├── inference
    │               ├── postprocessing
    │               ├── preprocessing
    │               └── training
    └── maas
        ├── mvp
        │   ├── cloudbuild.yaml
        │   └── model_0
        │       ├── inference
        │       ├── postprocessing
        │       ├── preprocessing
        │       └── training
        └── iris_classification
            ├── cloudbuild.yaml
            └── model_0
                ├── components
                │   ├── postprocessing
                │   ├── preprocessing
                │   └── training
                └── inference

```

## Git recommendations
1. Git branches should:
    * Have protection (these branches):
        * main  
        * stage 

    * Be named as follows:
      * feature/name-of-feature
      * fix/name-of-fix
      * refactor/name-of-refactor
  
    * Raise Pull Request (PR) to stage and then to main  
        [feature/name-of-feature, fix/name-of-fix, refactor/name-of-refactor] >> stage >> main

2. Commits
    * Commits should:
        * Have a message in the imperative sense – a good way to frame this tense is to finish the sentence "this commit will ...". For example:
          * Add MRR models
          * Fix typo in sessions model description
          * Update schema to v2 schema syntax
          * Upgrade project to dbt v0.13.0
        * Happen early and often! As soon as a piece of your code works, commit it! This means that if (/when), down the line, you introduce bad code, you can easily take your code back to the state it was in when it worked.

    * Commits can:
        * Be squashed on a local branch before being pushed to your remote branch, if
          you feel comfortable doing this.

3. Pull requests
    * Pull requests should:
        * Tackle a functional grouping of work. While it may be tempting to (for
          example) build MRR models _and_ add maintenance jobs in a single PR, these
          should be separate pieces of work.
        * Include a body that explains the context of the changes to the code, as well
          as what the code does. Useful things to include in a PR are:
          * Links to Jira cards
          * Links to Confluence docs that explain any new piece of functionality you 
            have introduced
          * A screenshot of the DAG for the new models you have built
          * Links to any related PRs (for example, if your BI tool will need to be
            updated to reflect the changes in your models)
          * Explanation of any breaking changes
          * Any special instructions to merge this code, e.g. whether a full-refresh
            needs to be run, or any renamed models should be dropped. You can use a PR
            template to encourage others making PRs on the repo to do the same. An example Pull Request template we often use on data science projects is included (.github/pull_request_template.md)
        * Be opened with 48 hours for the reviewer to review
        * Be merged by its _author_ when:
          * Approval has been given by at least one collaborator
          * All tests have passed

    * Pull requests can:
        * Be used to collaborate on code, as they are a great way to share the code
          you've written so far. In this scenario, use a _draft_ pull request.  

## References
...
