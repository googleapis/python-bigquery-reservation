# Changelog

## [1.3.0](https://www.github.com/googleapis/python-bigquery-reservation/compare/v1.2.2...v1.3.0) (2021-09-02)


### Features

* Deprecated SearchAssignments in favor of SearchAllAssignments ([#157](https://www.github.com/googleapis/python-bigquery-reservation/issues/157)) ([dacdf5a](https://www.github.com/googleapis/python-bigquery-reservation/commit/dacdf5ac37a802f0d00a30468720a3ce1f294985))


### Documentation

* samples for managing reservations ([#144](https://www.github.com/googleapis/python-bigquery-reservation/issues/144)) ([27b2564](https://www.github.com/googleapis/python-bigquery-reservation/commit/27b256440b2565369c900cd4728e38676f82fcfe))

### [1.2.2](https://www.github.com/googleapis/python-bigquery-reservation/compare/v1.2.1...v1.2.2) (2021-07-27)


### Bug Fixes

* enable self signed jwt for grpc ([#138](https://www.github.com/googleapis/python-bigquery-reservation/issues/138)) ([1d3f927](https://www.github.com/googleapis/python-bigquery-reservation/commit/1d3f927b12268c07e724ed44f1b3373a7c64e999))


### Documentation

* add Samples section to CONTRIBUTING.rst ([#132](https://www.github.com/googleapis/python-bigquery-reservation/issues/132)) ([c59d238](https://www.github.com/googleapis/python-bigquery-reservation/commit/c59d2383413ef5c57d72877d76514853f6271b00))


### Miscellaneous Chores

* release as 1.2.2 ([#139](https://www.github.com/googleapis/python-bigquery-reservation/issues/139)) ([96fbeba](https://www.github.com/googleapis/python-bigquery-reservation/commit/96fbeba273eb1776994f41400163788cf7b5e786))

### [1.2.1](https://www.github.com/googleapis/python-bigquery-reservation/compare/v1.2.0...v1.2.1) (2021-07-20)


### Bug Fixes

* **deps:** pin 'google-{api,cloud}-core', 'google-auth' to allow 2.x versions ([#131](https://www.github.com/googleapis/python-bigquery-reservation/issues/131)) ([9a011b6](https://www.github.com/googleapis/python-bigquery-reservation/commit/9a011b604ffc2256b89d2fd6909a7219c0bcc88b))

## [1.2.0](https://www.github.com/googleapis/python-bigquery-reservation/compare/v1.1.0...v1.2.0) (2021-06-30)


### Features

* add always_use_jwt_access ([#123](https://www.github.com/googleapis/python-bigquery-reservation/issues/123)) ([3123e99](https://www.github.com/googleapis/python-bigquery-reservation/commit/3123e99e8e288dcfb3627f77610c90060654bee4))
* support self-signed JWT flow for service accounts ([4d52ed9](https://www.github.com/googleapis/python-bigquery-reservation/commit/4d52ed91ae9eaa7ec6091138c134e682c9434853))


### Bug Fixes

* add async client to %name_%version/init.py ([4d52ed9](https://www.github.com/googleapis/python-bigquery-reservation/commit/4d52ed91ae9eaa7ec6091138c134e682c9434853))
* disable always_use_jwt_access ([32b279f](https://www.github.com/googleapis/python-bigquery-reservation/commit/32b279f0666a55c66e87c347ed7e913c2a9267a7))
* disable always_use_jwt_access ([#126](https://www.github.com/googleapis/python-bigquery-reservation/issues/126)) ([32b279f](https://www.github.com/googleapis/python-bigquery-reservation/commit/32b279f0666a55c66e87c347ed7e913c2a9267a7))
* exclude docs and tests from package ([#117](https://www.github.com/googleapis/python-bigquery-reservation/issues/117)) ([4f90792](https://www.github.com/googleapis/python-bigquery-reservation/commit/4f90792c26c8e47aad5a52267c713723e661efa3))
* require google-api-core >= 1.22.2 ([#90](https://www.github.com/googleapis/python-bigquery-reservation/issues/90)) ([3f0fff7](https://www.github.com/googleapis/python-bigquery-reservation/commit/3f0fff779d880df0648b7bcf59df01c4cacd4ca3))


### Documentation

* omit mention of Python 2.7 in 'CONTRIBUTING.rst' ([#1127](https://www.github.com/googleapis/python-bigquery-reservation/issues/1127)) ([#120](https://www.github.com/googleapis/python-bigquery-reservation/issues/120)) ([7d65f87](https://www.github.com/googleapis/python-bigquery-reservation/commit/7d65f877f6814aed37f68116b52e200585587c58)), closes [#1126](https://www.github.com/googleapis/python-bigquery-reservation/issues/1126)
* Update the README to reflect that this library is GA ([#112](https://www.github.com/googleapis/python-bigquery-reservation/issues/112)) ([7bca7a9](https://www.github.com/googleapis/python-bigquery-reservation/commit/7bca7a9b6d73d8c8ee522c8ac930192fad49da57))

## [1.1.0](https://www.github.com/googleapis/python-bigquery-reservation/compare/v1.0.1...v1.1.0) (2021-03-09)


### Features

* add `client_cert_source_for_mtls` argument to transports ([#78](https://www.github.com/googleapis/python-bigquery-reservation/issues/78)) ([5df0f09](https://www.github.com/googleapis/python-bigquery-reservation/commit/5df0f0965c541ca546d3851be1ab7782dc80a11b))

### [1.0.1](https://www.github.com/googleapis/python-bigquery-reservation/compare/v1.0.0...v1.0.1) (2021-01-14)


### Bug Fixes

* remove gRPC send/recv limit ([#60](https://www.github.com/googleapis/python-bigquery-reservation/issues/60)) ([4115f1e](https://www.github.com/googleapis/python-bigquery-reservation/commit/4115f1ee6b67be5ce409122a44faa47ac53112bf))


### Documentation

* document enum values with `undoc-members` option ([#69](https://www.github.com/googleapis/python-bigquery-reservation/issues/69)) ([2acdeb7](https://www.github.com/googleapis/python-bigquery-reservation/commit/2acdeb782521c01a4e1fa01e42fdd1ce79dbf13d))

## [1.0.0](https://www.github.com/googleapis/python-bigquery-reservation/compare/v0.4.0...v1.0.0) (2020-10-29)


### ⚠ BREAKING CHANGES

* update package names to avoid conflict with google-cloud-bigquery

### Bug Fixes

* update package names to avoid conflict with google-cloud-bigquery ([#47](https://www.github.com/googleapis/python-bigquery-reservation/issues/47)) ([dc2172f](https://www.github.com/googleapis/python-bigquery-reservation/commit/dc2172fa8c540efca01c81fdd7f40880e087f66d))

## [0.4.0](https://www.github.com/googleapis/python-bigquery-reservation/compare/v0.3.0...v0.4.0) (2020-10-28)


### Features

* add path formatting helper methods ([362e0fe](https://www.github.com/googleapis/python-bigquery-reservation/commit/362e0fe51364101bd770cce851d986eea6c56e6a))
* implement mtls env variables mentioned in aip.dev/auth/4114 ([#39](https://www.github.com/googleapis/python-bigquery-reservation/issues/39)) ([21bff87](https://www.github.com/googleapis/python-bigquery-reservation/commit/21bff87047519754a01983c9a4551cb534bcb88c))

## [0.3.0](https://www.github.com/googleapis/python-bigquery-reservation/compare/v0.2.0...v0.3.0) (2020-08-26)


### Features

* add support for new client options ([#23](https://www.github.com/googleapis/python-bigquery-reservation/issues/23)) ([a0e818d](https://www.github.com/googleapis/python-bigquery-reservation/commit/a0e818d526dc60f0eb24787333e1041b02f26816))

## [0.2.0](https://www.github.com/googleapis/python-bigquery-reservation/compare/v0.1.0...v0.2.0) (2020-05-27)


### Features

* add helper methods to parse resource paths (via synth) ([#7](https://www.github.com/googleapis/python-bigquery-reservation/issues/7)) ([8fc54cb](https://www.github.com/googleapis/python-bigquery-reservation/commit/8fc54cb70be698f6d265f60d7b8ee4561d12d2c9))

## 0.1.0 (2020-05-12)


### Features

* generate v1 ([6293404](https://www.github.com/googleapis/python-bigquery-reservation/commit/6293404e47ca2efdcb5f702e248f43250060eb8c))
