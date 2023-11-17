<img src="website/source/_static/images/harbor-logo.svg" alt="hamiparm" align="center">

<h4 align="center">Where data is safe and researchers set sail</h4>

This repository provides a robust, standardized framework that streamlines research projects and adheres to open science principles.
Everything is included, from reproducible Python environments to an automated website pipeline.
Join us in advancing open science, promoting transparency, and accelerating innovation by adopting this comprehensive toolkit.

## Communication

> No research should be done alone.

We use [this repository's issues](https://github.com/oasci/harbor/issues) as our todo list.
Asynchronous conversations about any of the tasks should be included as issue comments.
Synchronous meetings happening in-person or virtually should have meeting minutes stored in the [appropriate directory](01-management/03-meetings).

## Deploying

We use [bump-my-version](https://github.com/callowayproject/bump-my-version) to release a new version.
This will create a git tag that is used by [poetry-dynamic-version](https://github.com/mtkennerly/poetry-dynamic-versioning) to generate version strings.

However, we are using [Calendar Versioning](https://calver.org/) which means we need to manually specify new versions.
For example, to bump the version to November 8, 2024, you would run the following command after activating the relevant conda environment.

```bash
bump-my-version bump --new-version 2024.11.8
```

After releasing a new version, you need to push and include all tags.

```bash
git push --follow-tags
```

## License

Code contained in this project is released under the [MIT license][mit] as specified in `LICENSE.md`.
All other data, information, documentation, and associated content provided within this project are released under the [CC BY 4.0 license][cc-by-4.0] as specified in `LICENSE_INFO.md`.

[mit]: https://spdx.org/licenses/MIT.html
[cc-by-4.0]: https://creativecommons.org/licenses/by/4.0/
